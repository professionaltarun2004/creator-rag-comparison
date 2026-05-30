const BASE_URL = "http://127.0.0.1:8000"


export async function ingestVideo(url) {

    const response = await fetch(
        `${BASE_URL}/ingest`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        }
    )

    return response.json()
}


export async function askQuestion(
    question,
    videoA,
    videoB
) {

    const response = await fetch(
        `${BASE_URL}/chat`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question,
                video_a: videoA,
                video_b: videoB
            })
        }
    )

    return response.json()
}