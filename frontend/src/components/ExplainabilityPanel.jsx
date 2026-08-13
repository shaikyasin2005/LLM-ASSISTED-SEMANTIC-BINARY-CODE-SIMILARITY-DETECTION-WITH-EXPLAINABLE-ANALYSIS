import { motion } from "framer-motion";
import { slideLeftVariants } from "../animations/slideVariants";

export default function ExplainabilityPanel({ explanation }) {
  return (
    <motion.div
      variants={slideLeftVariants}
      initial="hidden"
      animate="visible"
      className="bg-gray-100 p-6 rounded-xl mt-6"
    >
      <h3 className="text-xl font-bold mb-3">Explainability</h3>
      <p>{explanation}</p>
    </motion.div>
  );
}