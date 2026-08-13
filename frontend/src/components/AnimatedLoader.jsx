import { motion } from "framer-motion";

export default function AnimatedLoader() {
  return (
    <motion.div
      animate={{ rotate: 360 }}
      transition={{ repeat: Infinity, duration: 1 }}
      className="w-10 h-10 border-4 border-blue-400 border-t-transparent rounded-full"
    />
  );
}