import React, { useState } from "react";
import axios from "axios";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from "chart.js";

import { Bar } from "react-chartjs-2";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

export default function ComparisonPage() {

  const [fileA, setFileA] = useState(null);
  const [fileB, setFileB] = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleCompare = async () => {

    if (!fileA || !fileB) {
      alert("Upload both files");
      return;
    }

    setLoading(true);

    const formData = new FormData();
    formData.append("file1", fileA);
    formData.append("file2", fileB);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/similarity/compare-files",
        formData
      );

      setResults(response.data);

    } catch (error) {

      console.error(error);
      alert("Comparison failed");

    }

    setLoading(false);
  };

  const chartData = results
    ? {
        labels: ["TF-IDF", "Structural", "Hybrid"],
        datasets: [
          {
            label: "Similarity Score",
            data: [
              results.tfidf_score,
              results.structural_score,
              results.hybrid_score
            ],
            backgroundColor: ["#4CAF50", "#2196F3", "#FF9800"]
          }
        ]
      }
    : null;

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>

      <h1>
        LLM-ASSISTED SEMANTIC BINARY CODE SIMILARITY DETECTION WITH EXPLAINABLE ANALYSIS
      </h1>

      <br/>

      <div style={{ display: "flex", gap: "80px" }}>

        <div>
          <h3>Upload File A</h3>
          <input type="file" onChange={(e) => setFileA(e.target.files[0])}/>
        </div>

        <div>
          <h3>Upload File B</h3>
          <input type="file" onChange={(e) => setFileB(e.target.files[0])}/>
        </div>

      </div>

      <br/>

      <button onClick={handleCompare} style={{ padding: "10px 20px" }}>
        Compare
      </button>

      <br/><br/>

      {loading && <p>Processing binaries...</p>}

      {results && (
        <>
          <h2>Similarity Results</h2>

          <p>TF-IDF Score: {results.tfidf_score.toFixed(3)}</p>
          <p>Structural Score: {results.structural_score.toFixed(3)}</p>
          <p>Hybrid Score: {results.hybrid_score.toFixed(3)}</p>
          <p>Exact Match: {results.exact_match ? "Yes" : "No"}</p>

          <br/>

          <h2>Similarity Graph</h2>

          <div style={{ width: "600px" }}>
            <Bar data={chartData} />
          </div>

          <br/>

          <h2>Explainability</h2>
          <p>{results.explanation}</p>
        </>
      )}

    </div>
  );
}