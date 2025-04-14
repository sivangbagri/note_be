from typing import Tuple, Optional
import time
import os
import whisper
from pathlib import Path

SUPPORTED_LANGUAGES = {
    "en": "English",
    "zh": "Chinese (Mandarin)",
    "yue": "Cantonese"
}

# Model size options: "tiny", "base", "small", "medium", "large"
DEFAULT_MODEL_SIZE = "tiny"


def transcribe_audio(audio_path: str, language: Optional[str] = None) -> Tuple[str, float]:
    """
    Transcribes an audio file to text using Whisper.

    Args:
        audio_path: Path to the audio file
        language: Optional language code (auto-detected if None)

    Returns:
        tuple: (transcript text, processing duration in seconds)
    """
    start_time = time.time()

    # Check if file exists
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    # Load Whisper model
    print(f"Loading Whisper model ({DEFAULT_MODEL_SIZE})...")
    model = whisper.load_model(DEFAULT_MODEL_SIZE)

    # Prepare transcription options
    options = {
        "task": "translate"
    }
    if language:
        if language in SUPPORTED_LANGUAGES:
            options["language"] = language
        else:
            print(
                f"Warning: Unsupported language '{language}'. Auto-detecting instead.")

    # Perform transcription
    print(f"Transcribing audio file: {audio_path}")
    result = model.transcribe(audio_path, **options)

    # Extract transcript text
    transcript = result["text"]

    # Calculate processing duration
    duration = time.time() - start_time

    print(f"Transcription completed in {duration:.2f} seconds")
    return transcript, duration
