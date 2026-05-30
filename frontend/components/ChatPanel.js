"use client"

import { useState } from "react"

import { askQuestion } from "../services/api"


export default function ChatPanel({

    videoA,
    videoB

}) {

    const [question, setQuestion] = useState("")

    const [loading, setLoading] = useState(false)

    const [response, setResponse] = useState(null)
    const [displayedAnswer, setDisplayedAnswer] = useState("")

    async function streamText(text) {

        setDisplayedAnswer("")

        for (let i = 0; i < text.length; i++) {

            setDisplayedAnswer(
                (prev) => prev + text[i]
            )

            await new Promise(
                (resolve) => setTimeout(resolve, 10)
            )
        }
    }

    async function handleAsk() {

        if (!question) return

        if (!videoA || !videoB) {

            alert("Please ingest both videos first")

            return
        }

        setLoading(true)

        try {

            const data = await askQuestion(
                question,
                videoA,
                videoB
            )

            setResponse(data)

            await streamText(data.answer)

        }

        catch (error) {

            console.error(error)

            alert("Failed to get AI response")

        }

        setLoading(false)
    }


    return (

        <div className="border border-gray-700 p-6 rounded-xl">

            <h2 className="text-2xl font-semibold mb-4">
                Chat Panel
            </h2>

            <textarea
                placeholder="Ask a comparison question..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                className="w-full p-4 rounded-lg bg-gray-900 border border-gray-700 mb-4"
                rows={4}
            />

            <button
                onClick={handleAsk}
                className="bg-white text-black px-4 py-2 rounded-lg font-medium"
            >
                {
                    loading
                    ? "Thinking..."
                    : "Ask AI"
                }
            </button>

            {
    response && (

        <div className="mt-8">

            <h3 className="text-xl font-semibold mb-4">
                AI Answer
            </h3>

            <p className="whitespace-pre-wrap leading-7 mb-8">
                {displayedAnswer}
            </p>


            <div className="grid grid-cols-2 gap-6">

                <div>

                    <h3 className="text-lg font-semibold mb-4">
                        Video A Sources
                    </h3>

                    <div className="space-y-4">

                        {
                            response.video_a_sources.map(
                                (source, index) => (

                                    <div
                                        key={index}
                                        className="border border-gray-700 p-4 rounded-lg bg-gray-900"
                                    >

                                        <p className="text-sm mb-3">
                                            {source.content}
                                        </p>

                                        <p className="text-xs text-gray-400">
                                            Video ID:
                                            {" "}
                                            {source.metadata.video_id}
                                        </p>

                                    </div>
                                )
                            )
                        }

                    </div>

                </div>


                <div>

                    <h3 className="text-lg font-semibold mb-4">
                        Video B Sources
                    </h3>

                    <div className="space-y-4">

                        {
                            response.video_b_sources.map(
                                (source, index) => (

                                    <div
                                        key={index}
                                        className="border border-gray-700 p-4 rounded-lg bg-gray-900"
                                    >

                                        <p className="text-sm mb-3">
                                            {source.content}
                                        </p>

                                        <p className="text-xs text-gray-400">
                                            Video ID:
                                            {" "}
                                            {source.metadata.video_id}
                                        </p>

                                    </div>
                                )
                            )
                        }

                    </div>

                </div>

            </div>

        </div>

    )
}

        </div>
    )
}