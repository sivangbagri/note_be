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


@app.get("/search", response_model=SearchResponse)
async def search(q: str):
    """
    Searches for keywords within stored transcripts.

    Parameters:
    - q: The search query

    Returns:
    - List of matching transcript segments with context
    """


@app.get("/export_pdf")
async def export_pdf(transcript_id: str):
    """
    Generates and returns a PDF of the summary for a specific transcript.

    Parameters:
    - transcript_id: The ID of the transcript to export

    Returns:
    - PDF file as a download
    """


# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
