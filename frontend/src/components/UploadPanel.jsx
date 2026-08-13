import { motion } from "framer-motion";
import { slideUpVariants } from "../animations/slideVariants";
import { useState } from "react";

export default function UploadPanel({ onCompare }) {

  const [code1, setCode1] = useState("");
  const [code2, setCode2] = useState("");

  return (
    <motion.div
      variants={slideUpVariants}
      initial="hidden"
      animate="visible"
      className="bg-gray-800 p-6 rounded-xl shadow-lg"
    >
      <h2 className="text-lg font-semibold mb-4">Compare Code</h2>

      <textarea
        placeholder="Paste Code 1"
        className="w-full p-3 mb-4 bg-gray-700 rounded"
        rows="6"
        onChange={(e) => setCode1(e.target.value)}
      />

      <textarea
        placeholder="Paste Code 2"
        className="w-full p-3 mb-4 bg-gray-700 rounded"
        rows="6"
        onChange={(e) => setCode2(e.target.value)}
      />

      <button
        className="bg-blue-500 px-4 py-2 rounded hover:bg-blue-600 transition"
        onClick={() => onCompare(code1, code2)}
      >
        Compare
      </button>
    </motion.div>
  );
}