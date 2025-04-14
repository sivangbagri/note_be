import sqlite3
from typing import List, Dict, Any
import re
from datetime import datetime


DB_PATH = "transcripts.db"


def init_db() -> None:
    """
    Initialize the SQLite database and create tables if they don't exist.
    Sets up the FTS5 virtual table for full-text search.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # transcript table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transcripts (
        id TEXT PRIMARY KEY,
        title TEXT,
        created_at TIMESTAMP,
        language TEXT,
        duration REAL
    )
    ''')

    # FTS5 virtual table for transcript content

    cursor.execute('''
    CREATE VIRTUAL TABLE IF NOT EXISTS transcript_content USING fts5 (
        transcript_id,
        sentence_idx,
        text,
        timestamp_start,
        timestamp_end
    )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized")


def add_transcript(transcript_id: str, transcript: str,
                   title: str = None, language: str = None,
                   duration: float = None) -> None:
    """
    Stores a transcript in the database, splitting it into sentences for search.

    Args:
        transcript_id: Unique identifier for the transcript
        transcript: Full transcript text
        title: Optional title for the transcript
        language: Language code
        duration: Audio duration in seconds
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Add metadata record
    cursor.execute(
        "INSERT INTO transcripts (id, title, created_at, language, duration) VALUES (?, ?, ?, ?, ?)",
        (transcript_id, title or f"Transcript {transcript_id[:8]}",
         datetime.now().isoformat(), language, duration)
    )

    # Split transcript into sentences

    sentences = re.split(r'(?<=[.!?])\s+', transcript)

    # Add each sentence to the FTS table
    for idx, sentence in enumerate(sentences):
        if sentence.strip():
            cursor.execute(
                "INSERT INTO transcript_content (transcript_id, sentence_idx, text, timestamp_start, timestamp_end) VALUES (?, ?, ?, ?, ?)",
                (transcript_id, idx, sentence, None, None)
            )

    conn.commit()
    conn.close()
    print(f"Added transcript {transcript_id} with {len(sentences)} sentences")


def search_transcripts(query: str, limit: int = 50) -> List[Dict[str, Any]]:
    """
    Searches for text in stored transcripts using SQLite FTS5.

    Args:
        query: The search query text
        limit: Maximum number of results to return

    Returns:
        list: Matching sentences with context
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Special case for direct transcript ID lookup
    if query.startswith("id:"):
        transcript_id = query.split("id:")[1].strip()
        cursor.execute(
            """
            SELECT transcript_id, sentence_idx, text 
            FROM transcript_content 
            WHERE transcript_id = ?
            ORDER BY sentence_idx
            """,
            (transcript_id,)
        )
    else:

        cursor.execute(
            """
            SELECT c.transcript_id, c.sentence_idx, c.text, t.created_at, t.title
            FROM transcript_content c
            JOIN transcripts t ON c.transcript_id = t.id
            WHERE transcript_content MATCH ?
            ORDER BY t.created_at DESC, c.sentence_idx
            LIMIT ?
            """,
            (query, limit)
        )

    results = []
    for row in cursor.fetchall():
        # For a simple lookup by ID, we might have fewer columns
        if len(row) >= 5:
            transcript_id, sentence_idx, text, created_at, title = row
            results.append({
                "transcript_id": transcript_id,
                "sentence_idx": sentence_idx,
                "text": text,
                "created_at": created_at,
                "title": title
            })
        else:
            transcript_id, sentence_idx, text = row[:3]
            results.append({
                "transcript_id": transcript_id,
                "sentence_idx": sentence_idx,
                "text": text
            })

    conn.close()
    return results
