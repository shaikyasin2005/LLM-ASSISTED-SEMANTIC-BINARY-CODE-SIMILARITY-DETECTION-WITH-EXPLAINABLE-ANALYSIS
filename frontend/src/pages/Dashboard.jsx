import Navbar from "../components/Navbar";
import ComparisonPage from "./ComparisonPage";

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <Navbar />
      <ComparisonPage />
    </div>
  );
}