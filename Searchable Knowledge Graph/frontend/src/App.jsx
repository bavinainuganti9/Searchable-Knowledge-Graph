import React, { useState } from "react";
import axios from "axios";

export default function App() {
  const [file, setFile] = useState(null);
  const [url, setUrl] = useState("");
  const [results, setResults] = useState([]);

  const uploadPDF = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios.post("http://localhost:8000/upload_pdf/", formData);
    setResults(res.data.entities);
  };

  const crawlURL = async () => {
    const formData = new FormData();
    formData.append("url", url);
    const res = await axios.post("http://localhost:8000/crawl_url/", formData);
    setResults(res.data.entities);
  };

  return (
    <div className="p-8 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">GraphIQ – Knowledge Graph Builder</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} className="mb-4" />
      <button onClick={uploadPDF} className="bg-blue-600 text-white px-4 py-2 mb-6">
        Upload PDF
      </button>

      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter website URL"
        className="block w-full border p-2 mb-2"
      />
      <button onClick={crawlURL} className="bg-green-600 text-white px-4 py-2">
        Crawl Website
      </button>

      <div className="mt-6">
        <h2 className="text-xl font-semibold mb-2">Extracted Entities:</h2>
        <ul className="list-disc pl-5">
          {results.map((r, i) => (
            <li key={i}>{r[0]} ({r[1]})</li>
          ))}
        </ul>
      </div>
    </div>
  );
}
