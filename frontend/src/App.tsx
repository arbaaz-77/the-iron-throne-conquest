import { useEffect, useState } from "react";
import "./App.css";

function App() {
  // 1. Create a state variable to hold our armies dictionary.
  // The <Record<string, number>> part is TypeScript strictly enforcing that
  // our dictionary will have string keys (houses) and number values (troops).
  const [armies, setArmies] = useState<Record<string, number>>({});

  useEffect(() => {
    fetch("http://127.0.0.1:8000/armies")
      .then((response) => response.json())
      .then((data) => {
        // 2. Save the fetched data into React State!
        setArmies(data.data);
      })
      .catch((error) => console.error("Ravens intercepted!", error));
  }, []);

  return (
    <div className="game-board">
      <h1>⚔️ The Iron Throne Conquest</h1>

      <h2>Active Banners</h2>
      {/* 3. Loop through the dictionary and render a card for each house */}
      <div className="banner-grid">
        {Object.entries(armies).map(([house, troops]) => (
          <div
            key={house}
            className="house-card"
          >
            <h3>House {house}</h3>
            <p>Troops: {troops}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
