export default function Home() {

  return (

    <main className="min-h-screen p-6 bg-black text-white">

      <h1 className="text-4xl font-bold mb-8">
        Creator RAG Comparison
      </h1>

      <div className="grid grid-cols-2 gap-6 mb-8">

        <div className="border border-gray-700 p-4 rounded-xl">
          Video A
        </div>

        <div className="border border-gray-700 p-4 rounded-xl">
          Video B
        </div>

      </div>

      <div className="border border-gray-700 p-6 rounded-xl">

        Chat Panel

      </div>

    </main>
  )
}