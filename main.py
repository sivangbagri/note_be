from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
import os
import uuid
from datetime import datetime

from modules.transcriber import transcribe_audio
from modules.summarizer import generate_summary
from modules.search import init_db, add_transcript, search_transcripts
from modules.exporter import generate_pdf


app = FastAPI(
    title="Meeting Assistant API",
    description="API for transcribing, summarizing, and searching meeting audio",
    version="1.0.0"
)

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure needed directories exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("output", exist_ok=True)

# Initialize the database on startup


@app.on_event("startup")
async def startup_event():
    init_db()  # Create DB tables if they don't exist


class TranscriptionResponse(BaseModel):
    transcript_id: str
    transcript: str
    summary: Dict[str, Any]
    duration: float


class SearchResponse(BaseModel):
    results: List[Dict[str, Any]]
    count: int


@app.post("/upload_audio", response_model=TranscriptionResponse)
async def upload_audio(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    language: Optional[str] = None
):
    """
    Uploads an audio file, transcribes it, and generates a summary.

    Parameters:
    - file: The audio file to transcribe
    - language: Optional language code (auto-detected if not provided)

    Returns:
    - Transcript ID, full transcript, summary, and processing duration
    """
    # Generate a unique ID for this transcript
    transcript_id = str(uuid.uuid4())

    # Define the path where the audio will be saved
    file_extension = file.filename.split(".")[-1]
    audio_path = f"uploads/{transcript_id}.{file_extension}"

    try:
        # Save the uploaded audio file
        with open(audio_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)

        # Transcribe the audio file
        transcript, duration = transcribe_audio(audio_path, language)

        # Generate a summary of the transcript
        summary = generate_summary(transcript, language)

        # Store the transcript in the database (in the background)
        background_tasks.add_task(add_transcript, transcript_id, transcript)

        return {
            "transcript_id": transcript_id,
            "transcript": transcript,
            "summary": summary,
            "duration": duration
        }
    except Exception as e:
        # If anything goes wrong, clean up the audio file and raise an error
        if os.path.exists(audio_path):
            os.remove(audio_path)
        raise HTTPException(
            status_code=500, detail=f"Processing error: {str(e)}")


@app.get("/search", response_model=SearchResponse)
async def search(q: str):
    """
    Searches for keywords within stored transcripts.

    Parameters:
    - q: The search query

    Returns:
    - List of matching transcript segments with context
    """
    if not q or len(q.strip()) == 0:
        return {"results": [], "count": 0}

    results = search_transcripts(q.strip())
    return {"results": results, "count": len(results)}


@app.get("/export_pdf")
async def export_pdf(transcript_id: str):
    """
    Generates and returns a PDF of the summary for a specific transcript.

    Parameters:
    - transcript_id: The ID of the transcript to export

    Returns:
    - PDF file as a download
    """
    # Search for the transcript to get its content
    results = search_transcripts(f"id:{transcript_id}")

    if not results:
        raise HTTPException(status_code=404, detail="Transcript not found")

    # Extract transcript text
    transcript = " ".join([r["text"] for r in results])

    # Generate summary
    summary = generate_summary(transcript)

    # Create PDF
    pdf_path = generate_pdf(transcript_id, transcript, summary)

    # Return the PDF file for download
    filename = f"meeting_summary_{datetime.now().strftime('%Y%m%d')}.pdf"
    return FileResponse(
        path=pdf_path,
        filename=filename,
        media_type="application/pdf"
    )

# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
