import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [name, setName] = useState("")

  useEffect(() => {
    fetch("/api").then(res => res.json()).then(data => {
      setName(data)
    })
  }, [])
  return (
    <div className="App">
      <p>{name.user}</p>
    </div>
  );
}

export default App;
