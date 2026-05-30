"use client"

import { useState } from "react"

import { ingestVideo } from "../services/api"


export default function VideoCard({

    label,
    onVideoIngested

}) {

    const [url, setUrl] = useState("")

    const [loading, setLoading] = useState(false)

    const [videoData, setVideoData] = useState(null)


    async function handleIngest() {

        if (!url) return

        setLoading(true)

        try {

            const data = await ingestVideo(url)

            setVideoData(data)

            onVideoIngested(data.metadata.video_id)

        }

        catch (error) {

            console.error(error)

            alert("Failed to ingest video")

        }

        setLoading(false)
    }


    return (

        <div className="border border-gray-700 p-4 rounded-xl">

            <h2 className="text-2xl font-semibold mb-4">
                {label}
            </h2>

            <input
                type="text"
                placeholder="Paste YouTube URL"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                className="w-full p-3 rounded-lg bg-gray-900 border border-gray-700 mb-4"
            />

            <button
                onClick={handleIngest}
                className="bg-white text-black px-4 py-2 rounded-lg font-medium"
            >
                {
                    loading
                    ? "Ingesting..."
                    : "Ingest Video"
                }
            </button>

            {
                videoData && (

                    <div className="mt-6">

    <img
        src={videoData.metadata.thumbnail}
        alt="thumbnail"
        className="w-full rounded-xl mb-4"
    />

    <div className="space-y-2">

        <p>
            <strong>Title:</strong>
            {" "}
            {videoData.metadata.title}
        </p>

        <p>
            <strong>Creator:</strong>
            {" "}
            {videoData.metadata.creator}
        </p>

        <p>
            <strong>Views:</strong>
            {" "}
            {videoData.metadata.views}
        </p>

        <p>
            <strong>Likes:</strong>
            {" "}
            {videoData.metadata.likes}
        </p>

        <p>
            <strong>Engagement Rate:</strong>
            {" "}
            {videoData.metadata.engagement_rate}%
        </p>

    </div>

</div>
                )
            }

        </div>
    )
}