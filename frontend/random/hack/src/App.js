import React, { useState } from 'react';

function App(){

  const now = new Date().toLocaleTimeString();
  const [time, changeTime] = useState(now);

  function increase(){
    const newTime = new Date().toLocaleTimeString();
    changeTime(newTime)
  }

  return(
    <div className = "container">
    <h1>{time}}</h1>
    <button onClick = {increase}>Get Time</button>
    </div>
  );
}

export default App;
