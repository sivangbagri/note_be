# 🧠 Multilingual Note-Taking Agent – Backend (FastAPI)

This is the **backend** for a multilingual AI meeting assistant built for the **HOLON x KBI AI AGENTS Hackathon 2025**. It transcribes meeting audio, summarizes it, supports keyword search, and exports shareable PDF summaries along with sentimental analysis.

---

## 🚀 Features

- 🎙️ **Multilingual transcription** (English, Mandarin, Cantonese)
- 📝 **Structured meeting summaries** with key action items
- 🔍 **Keyword-based transcript search**
- 📄 **PDF export** of meeting summaries
- 📄 **Sentimental analysis** of the Transcript
- ⚙️ Built using **FastAPI**, **LangChain**, **Whisper**, and **SQLite**

---

## 📦 Tech Stack

| Layer      | Tool/Library              | Purpose                            |
| ---------- | ------------------------- | ---------------------------------- |
| Framework  | FastAPI                   | Web API & routing                  |
| ASR        | Whisper / Faster-Whisper  | Speech-to-text transcription       |
| Summarizer | LangChain + Qwen/DeepSeek | Extracts summaries + action points |
| Sentiment     | HuggingFace Transformers + `nlptown/bert` | Time based sentimental analysis of transcript
| Storage    | SQLite (FTS5)             | Full-text searchable transcripts   |
| PDF Export | fpdf                      | Generates PDF reports              |

---

## 🧪 Local Setup

```bash
git clone https://github.com/your-username/holon-note-agent
```
```
pip install -r requiremnents.txt
```
```
uvicorn main:app --reload
```

### Visit Swagger Docs
```
Go to: http://127.0.0.1:8000/docs
```

### API Endpoints

Endpoint Method Description
- `/upload_audio` POST Uploads and transcribes audio
- `/search?q=keyword` GET Searches transcript for keywords
- `/export_pdf` GET Exports the summary as a PDF along with sentimental analysis

``` mermaid
flowchart TD
    %% Client
    Client["Client"]:::external

    %% API Layer
    subgraph "API Layer"
        direction TB
        FastAPI["FastAPI App"]:::api
        FA1["/upload_audio"]:::api
        FA2["/search"]:::api
        FA3["/export_pdf"]:::api
    end

    %% Service Layer
    subgraph "Service Layer"
        direction TB
        Transcriber["Transcriber"]:::internal
        Summarizer["Summarizer"]:::internal
        SearchMod["Search"]:::internal
        Exporter["Exporter"]:::internal
        Sample["Pipeline Orchestrator"]:::internal
        Fonts["PDF Font Assets"]:::internal
    end

    %% Utils
    subgraph "Utils"
        direction TB
        Format["format.py"]:::internal
        Sentiments["sentiments.py"]:::internal
    end

    %% Data Layer
    subgraph "Data Layer"
        direction TB
        DB["transcripts.db\n(SQLite FTS5)"]:::datastore
    end

    %% External AI Models
    subgraph "External AI Models"
        direction TB
        WhisperModel["Whisper\n/ Faster‑Whisper"]:::external
        LangChainModel["LangChain + Qwen/DeepSeek"]:::external
    end

    %% PDF Engine
    subgraph "PDF Engine"
        direction TB
        FPDF["fpdf"]:::external
    end

    %% Output
    subgraph "Output"
        direction TB
        PDFOut["output/*.pdf"]:::output
    end

    %% Connections
    Client -->|"HTTP request"| FastAPI

    FastAPI --> FA1
    FastAPI --> FA2
    FastAPI --> FA3

    FA1 -->|"audio file"| Transcriber
    Transcriber -->|"audio file"| WhisperModel
    WhisperModel -->|"transcript text"| DB

    DB -->|"transcript text"| Summarizer
    DB -->|"transcript text"| Sentiments

    Summarizer -->|"transcript text"| LangChainModel
    LangChainModel -->|"summary & actions"| Exporter

    Sentiments -->|"sentiment data"| Exporter
    Format -->|"formatted text"| Exporter

    Exporter -->|"summary+sentiment+format"| FPDF
    FPDF -->|"PDF file"| PDFOut

    PDFOut --> FastAPI
    FastAPI -->|"PDF or JSON response"| Client

    FA2 -->|"search query"| SearchMod
    SearchMod -->|"read transcript"| DB
    SearchMod -->|"results"| FastAPI

    %% Sample orchestrator
    Sample --> Transcriber
    Sample --> Summarizer

    %% Click Events
    click FastAPI "https://github.com/sivangbagri/note_be/blob/master/main.py"
    click Transcriber "https://github.com/sivangbagri/note_be/blob/master/modules/transcriber.py"
    click Summarizer "https://github.com/sivangbagri/note_be/blob/master/modules/summarizer.py"
    click SearchMod "https://github.com/sivangbagri/note_be/blob/master/modules/search.py"
    click Exporter "https://github.com/sivangbagri/note_be/blob/master/modules/exporter.py"
    click Format "https://github.com/sivangbagri/note_be/blob/master/utils/format.py"
    click Sentiments "https://github.com/sivangbagri/note_be/blob/master/utils/sentiments.py"
    click DB "https://github.com/sivangbagri/note_be/blob/master/transcripts.db"
    click PDFOut "https://github.com/sivangbagri/note_be/tree/master/output/"
    click Sample "https://github.com/sivangbagri/note_be/blob/master/modules/sample.py"
    click Fonts "https://github.com/sivangbagri/note_be/tree/master/modules/fonts/"

    %% Styles
    classDef api fill:#d4f8d4,stroke:#333,stroke-width:1px;
    classDef internal fill:#d4e0f7,stroke:#333,stroke-width:1px;
    classDef external fill:#ffe1a8,stroke:#333,stroke-width:1px;
    classDef datastore fill:#e0e0e0,stroke:#333,stroke-width:1px;
    classDef output fill:#fff5b1,stroke:#333,stroke-width:1px;
```
