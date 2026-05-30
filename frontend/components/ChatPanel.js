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

                        <p className="whitespace-pre-wrap leading-7">
                            {response.answer}
                        </p>

                    </div>

                )
            }

        </div>
    )
}