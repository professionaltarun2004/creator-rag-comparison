# Creator RAG Comparison Platform

An AI-powered full-stack creator intelligence platform that compares social media videos using Retrieval-Augmented Generation (RAG), semantic search, metadata-aware retrieval, and conversational AI.

This project enables creators to ingest videos, analyze engagement patterns, compare hooks and storytelling strategies, and receive grounded AI-generated insights with source citations.

---

# Features

## AI-Powered Video Comparison

* Compare two creator videos side-by-side
* Analyze hooks, storytelling, engagement strategy, and retention potential
* Generate improvement suggestions using AI reasoning

## Retrieval-Augmented Generation (RAG)

* Transcript chunking and semantic embeddings
* Vector database retrieval using ChromaDB
* Metadata-aware semantic filtering
* Source-grounded responses

## Metadata Intelligence

Dynamically extracts:

* Title
* Creator
* Views
* Likes
* Comments
* Upload Date
* Duration
* Hashtags
* Engagement Rate

## Conversational Memory

* Maintains conversational context across follow-up questions
* Enables contextual creator analysis

## Streaming UX

* Simulated live AI streaming responses for better user experience

## Full-Stack Architecture

* Next.js frontend
* FastAPI backend
* LangChain orchestration
* HuggingFace embeddings
* ChromaDB vector storage

---

# Tech Stack

## Frontend

* Next.js
* React
* Tailwind CSS

## Backend

* FastAPI
* Python

## AI / RAG Stack

* LangChain
* ChromaDB
* HuggingFace Embeddings
* OpenRouter GPT-4o-mini

## Video Processing

* youtube-transcript-api
* yt-dlp

---

# System Architecture

```text
Frontend (Next.js)
        ↓
FastAPI Backend
        ↓
Transcript + Metadata Extraction
        ↓
Chunking + Embeddings
        ↓
ChromaDB Vector Store
        ↓
Metadata-Aware Retrieval
        ↓
Comparative RAG Prompting
        ↓
LLM Reasoning
        ↓
Grounded AI Response
```

---

# Project Structure

```text
creator-rag-comparison/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── rag/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── chroma_db/
│   ├── requirements.txt
│   └── .env
│
└── frontend/
    ├── app/
    ├── components/
    ├── services/
    └── package.json
```
# System Architecture

![System Architecture](./assets/System architecture creator rag system.png)
---

# Installation

## 1. Clone Repository

```bash
git clone <your-repo-url>
cd creator-rag-comparison
```

---

# Backend Setup

## 1. Navigate to backend

```bash
cd backend
```

## 2. Create virtual environment

```bash
python -m venv venv
```

## 3. Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure environment variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

## 6. Run backend server

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Frontend Setup

## 1. Navigate to frontend

```bash
cd frontend
```

## 2. Install dependencies

```bash
npm install
```

## 3. Run frontend

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

# API Endpoints

## POST `/ingest`

Ingests a YouTube video into the RAG pipeline.

### Request

```json
{
  "url": "https://youtube.com/watch?v=..."
}
```

### Response

```json
{
  "message": "Video ingested successfully",
  "video_id": "...",
  "metadata": {...}
}
```

---

## POST `/chat`

Compares two ingested videos using conversational RAG.

### Request

```json
{
  "question": "Compare the hooks of these videos",
  "video_a": "video_id_a",
  "video_b": "video_id_b"
}
```

---

# AI Pipeline

## 1. Transcript Extraction

Extracts transcripts dynamically from YouTube videos.

## 2. Metadata Extraction

Uses `yt-dlp` to retrieve:

* creator analytics
* hashtags
* engagement metrics
* thumbnails

## 3. Chunking

Transcripts are split into semantically meaningful chunks.

## 4. Embeddings

HuggingFace embeddings convert chunks into vector representations.

## 5. Vector Storage

Chunks + metadata are stored in ChromaDB.

## 6. Metadata-Aware Retrieval

Retrieval filters transcript chunks by video ID to avoid context contamination.

## 7. Comparative Reasoning

The LLM compares:

* hooks
* storytelling
* engagement strategy
* creator positioning
* content effectiveness

---

# Engineering Decisions

## Why ChromaDB?

ChromaDB was chosen because it is lightweight, fast for local development, integrates well with LangChain, and avoids unnecessary infrastructure complexity during MVP development.

## Why Metadata Filtering?

Metadata filtering prevents transcript contamination between videos and enables cleaner comparative retrieval.

## Why Chunking?

Chunking improves semantic retrieval precision and reduces irrelevant context injection into the LLM prompt.

## Why Simulated Streaming?

Frontend-side streaming simulation provides a responsive AI experience without introducing backend websocket complexity during MVP iteration.

---

# Challenges Faced

## Transcript Quality

One major challenge was inconsistent transcript quality from auto-generated captions. Since the RAG pipeline depends heavily on transcript accuracy, noisy captions directly affect retrieval quality and downstream reasoning.

Future production improvements would include:

* Whisper fallback transcription
* transcript normalization
* transcript confidence validation
* multilingual cleanup pipelines

---

# Future Improvements

* Instagram Reel ingestion
* Whisper ASR fallback
* Backend token streaming
* Deployment
* Authentication
* Persistent conversation memory
* Advanced analytics dashboard
* Multi-video creator clustering

---

# Demo Capabilities

The platform currently supports:

* side-by-side creator analysis
* semantic transcript retrieval
* grounded source citations
* conversational memory
* engagement-aware comparison
* AI-generated improvement suggestions

---

# Author

Balivada Tarun Sandilya

AI/ML Engineering | Full-Stack AI Systems | RAG Applications
