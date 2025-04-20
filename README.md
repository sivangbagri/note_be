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
