import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [armies, setArmies] = useState<Record<string, number>>({});

  // 1. New state to track user inputs and battle results
  const [attacker, setAttacker] = useState("");
  const [defender, setDefender] = useState("");
  const [battleMessage, setBattleMessage] = useState(
    "Awaiting your orders, Commander.",
  );

  useEffect(() => {
    fetch("http://127.0.0.1:8000/armies")
      .then((response) => response.json())
      .then((data) => setArmies(data.data))
      .catch((error) => console.error("Ravens intercepted!", error));
  }, []);

  // 2. The function to trigger the attack
  const handleMarch = async () => {
    if (!attacker || !defender) {
      setBattleMessage(
        "You must specify both an attacking and defending house.",
      );
      return;
    }

    try {
      // Send the POST request to our FastAPI backend
      const response = await fetch("http://127.0.0.1:8000/march", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        // Convert our React state into a JSON string matching our Pydantic model
        body: JSON.stringify({
          attacker:
            attacker.charAt(0).toUpperCase() + attacker.slice(1).toLowerCase(),
          defender:
            defender.charAt(0).toUpperCase() + defender.slice(1).toLowerCase(),
        }),
      });

      const data = await response.json();

      if (data.status === "error") {
        setBattleMessage(`❌ Invalid Order: ${data.message}`);
      } else {
        // Success! Update the message and the army counts on screen
        setBattleMessage(`⚔️ ${data.message}`);
        setArmies(data.armies);
      }
    } catch (error) {
      setBattleMessage("❌ The ravens were intercepted! (Server Error)");
    }
  };

  return (
    <div className="game-board">
      <h1>⚔️ The Iron Throne Conquest</h1>

      {/* 3. The Command Tent (Input Form) */}
      <div className="command-tent">
        <p className="battle-message">{battleMessage}</p>
        <div className="inputs">
          <input
            type="text"
            placeholder="Attacker (e.g. Stark)"
            value={attacker}
            onChange={(e) => setAttacker(e.target.value)}
          />
          <span className="vs-text">VS</span>
          <input
            type="text"
            placeholder="Defender (e.g. Tully)"
            value={defender}
            onChange={(e) => setDefender(e.target.value)}
          />
          <button onClick={handleMarch}>March!</button>
        </div>
      </div>

      <h2>Active Banners</h2>
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
