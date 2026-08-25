import { useEffect } from "react";
import "./App.css";

function App() {
  // This hook runs once when the page loads
  useEffect(() => {
    // 1. We call our Python API
    fetch("http://127.0.0.1:8000/armies")
      .then((response) => response.json()) // 2. Convert the response to JSON
      .then((data) => {
        // 3. Log the data to the browser console!
        console.log("Message from the Citadel:", data);
      })
      .catch((error) => console.error("Ravens intercepted!", error));
  }, []);

  return (
    <div>
      <h1>⚔️ The Iron Throne Conquest</h1>
      <p>Check your browser console (F12) to see the data from Python!</p>
    </div>
  );
}

export default App;
