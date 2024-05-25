import React, { useState, useEffect } from 'react';
import MotivationList from './components/MotivationList';

function App() {
  const [motivations, setMotivations] = useState([]);

  useEffect(() => {
    fetchMotivations();
  }, []);

  const fetchMotivations = async () => {
    try {
      const response = await fetch('/api/motivations');
      const data = await response.json();
      setMotivations(data);
    } catch (error) {
      console.error('Error fetching motivations:', error);
    }
  };

  return (
    <div className="App">
      <h1>Motivation App</h1>
      <MotivationList motivations={motivations} />
    </div>
  );
}

export default App;