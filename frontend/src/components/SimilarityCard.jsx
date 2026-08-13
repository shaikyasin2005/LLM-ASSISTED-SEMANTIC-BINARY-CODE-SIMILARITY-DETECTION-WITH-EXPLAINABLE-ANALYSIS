import { motion } from "framer-motion";
import { fadeVariants } from "../animations/fadeVariants";

export default function SimilarityCard({ result }) {
  return (
    <motion.div
      variants={fadeVariants}
      initial="hidden"
      animate="visible"
      className="bg-gray-800 p-6 rounded-xl shadow-lg"
    >
      <h3 className="text-xl font-bold mb-2">Similarity Results</h3>
      <p>TF-IDF Score: {result.tfidf_score.toFixed(3)}</p>
      <p>Structural Score: {result.structural_score.toFixed(3)}</p>
      <p>Hybrid Score: {result.hybrid_score.toFixed(3)}</p>
      <p>Exact Match: {result.exact_match ? "Yes" : "No"}</p>
    </motion.div>
  );
}