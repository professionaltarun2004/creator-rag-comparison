"use client"

import { useState } from "react"

import VideoCard from "../components/VideoCard"
import ChatPanel from "../components/ChatPanel"


export default function Home() {

  const [videoA, setVideoA] = useState("")

  const [videoB, setVideoB] = useState("")


  return (

    <main className="min-h-screen p-6 bg-black text-white">

      <h1 className="text-4xl font-bold mb-8">
        Creator RAG Comparison
      </h1>

      <div className="grid grid-cols-2 gap-6 mb-8">

        <VideoCard
          label="Video A"
          onVideoIngested={setVideoA}
        />

        <VideoCard
          label="Video B"
          onVideoIngested={setVideoB}
        />

      </div>

      <ChatPanel
        videoA={videoA}
        videoB={videoB}
      />

    </main>
  )
}