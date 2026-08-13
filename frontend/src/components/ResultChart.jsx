import { motion } from "framer-motion";
import { slideRightVariants } from "../animations/slideVariants";
import { BarChart, Bar, XAxis, YAxis, Tooltip } from "recharts";

export default function ResultChart({ result }) {

  const data = [
    { name: "TF-IDF", value: result.tfidf_score },
    { name: "Structural", value: result.structural_score },
    { name: "Hybrid", value: result.hybrid_score }
  ];

  return (
    <motion.div
      variants={slideRightVariants}
      initial="hidden"
      animate="visible"
      className="bg-gray-800 p-6 rounded-xl"
    >
      <BarChart width={400} height={300} data={data}>
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="value" fill="#3b82f6" />
      </BarChart>
    </motion.div>
  );
}