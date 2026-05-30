# Creator RAG Comparison Platform

An AI-powered full-stack creator intelligence platform that compares social media videos using Retrieval-Augmented Generation (RAG), semantic search, metadata-aware retrieval, and conversational AI.

This project enables creators to ingest videos, analyze engagement patterns, compare hooks and storytelling strategies, and receive grounded AI-generated insights with source citations.

---

# Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Key Engineering Highlights](#key-engineering-highlights)
- [Architecture Overview](#architecture-overview)
- [System Architecture Diagram](#system-architecture-diagram)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [API Endpoints](#api-endpoints)
- [AI Pipeline](#ai-pipeline)
- [Engineering Decisions](#engineering-decisions)
- [Challenges Faced](#challenges-faced)
- [Future Improvements](#future-improvements)
- [Demo Capabilities](#demo-capabilities)
- [Author](#author)

---

# Features

## AI-Powered Video Comparison
- Compare two creator videos side-by-side
- Analyze hooks, storytelling, engagement strategy, and retention potential
- Generate AI-powered improvement suggestions

## Retrieval-Augmented Generation (RAG)
- Transcript chunking and semantic embeddings
- Vector database retrieval using ChromaDB
- Metadata-aware semantic filtering
- Source-grounded responses

## Metadata Intelligence
Dynamically extracts:
- Video title
- Creator/channel name
- Views
- Likes
- Comments
- Upload date
- Duration
- Hashtags
- Engagement rate
- Video thumbnails

## Conversational AI
- Multi-turn comparative conversations
- Conversational memory support
- Context-aware creator analysis

## Streaming AI UX
- Simulated live streaming responses
- Real-time conversational feel
- Better user interaction experience

## Full-Stack Architecture
- Next.js frontend
- FastAPI backend
- LangChain orchestration
- HuggingFace embeddings
- ChromaDB vector storage

---

# Tech Stack

## Frontend
- Next.js
- React
- Tailwind CSS

## Backend
- FastAPI
- Python

## AI / RAG Stack
- LangChain
- ChromaDB
- HuggingFace Embeddings
- OpenRouter GPT-4o-mini

## Video Processing
- youtube-transcript-api
- yt-dlp

---

# Key Engineering Highlights

- Metadata-aware semantic retrieval
- Comparative RAG architecture
- Grounded source citation system
- Streaming AI response UX
- Full-stack AI orchestration
- Conversational memory handling
- Dynamic transcript chunk retrieval
- Engagement analytics pipeline

---

# Architecture Overview

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
Streaming AI Response
```

---

# System Architecture Diagram

<p align="center">
  <img src="./assets/architecture-diagram.png" alt="System Architecture" width="100%">
</p>

---

# Project Structure

```text
creator-rag-comparison/
│
├── assets/
│   └── architecture-diagram.png
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
├── frontend/
│   ├── app/
│   ├── components/
│   ├── services/
│   └── package.json
│
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd creator-rag-comparison
```

---

# Backend Setup

## 1. Navigate to Backend

```bash
cd backend
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

## 6. Run Backend Server

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Frontend Setup

## 1. Navigate to Frontend

```bash
cd frontend
```

## 2. Install Dependencies

```bash
npm install
```

## 3. Run Frontend

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
- creator analytics
- hashtags
- engagement metrics
- thumbnails

## 3. Chunking
Transcripts are split into semantically meaningful chunks.

## 4. Embeddings
HuggingFace embeddings convert chunks into vector representations.

## 5. Vector Storage
Chunks and metadata are stored in ChromaDB.

## 6. Metadata-Aware Retrieval
Retrieval filters transcript chunks by video ID to avoid context contamination.

## 7. Comparative Reasoning
The LLM compares:
- hooks
- storytelling
- engagement strategy
- creator positioning
- content effectiveness

---

# Engineering Decisions

## Why ChromaDB?
ChromaDB was chosen because it is lightweight, fast for local development, integrates cleanly with LangChain, and avoids unnecessary infrastructure overhead during MVP development.

## Why Metadata Filtering?
Metadata filtering prevents transcript contamination between videos and enables cleaner comparative retrieval.

## Why Chunking?
Chunking improves semantic retrieval precision and reduces irrelevant context injection into the LLM prompt.

## Why Simulated Streaming?
Frontend-side streaming simulation provides a responsive AI experience without introducing websocket or SSE complexity during MVP development.

---

# Challenges Faced

## Transcript Quality Variability
One major challenge was inconsistent transcript quality from auto-generated captions. Since the RAG pipeline depends heavily on transcript accuracy, noisy captions directly affect retrieval quality and downstream reasoning.

Potential production improvements include:
- Whisper fallback transcription
- Transcript normalization
- Confidence-based transcript validation
- Multilingual cleanup pipelines

---

# Future Improvements

- Instagram Reel ingestion
- Whisper ASR fallback
- Backend token streaming
- Deployment support
- Authentication
- Persistent conversation memory
- Advanced creator analytics dashboard
- Multi-video creator clustering

---

# Demo Capabilities

The platform currently supports:
- Side-by-side creator analysis
- Semantic transcript retrieval
- Grounded source citations
- Conversational memory
- Engagement-aware comparison
- AI-generated improvement suggestions
- Metadata-aware retrieval
- Streaming AI responses

---

# Author

## Balivada Tarun Sandilya

AI/ML Engineering | Full-Stack AI Systems | RAG Applications