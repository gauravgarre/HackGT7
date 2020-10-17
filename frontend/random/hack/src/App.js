import React, { useState } from 'react';

function App(){
  const [contact, setContact] = useState({
    eventName = "",
    eventType = "",
    eventDate = "",
    eventTime = ""

  });

  function handleChange(event){
    const [name, value] = event.target();
      setContact((prevValue) => {
        if (name === "eventName"){
          return{
            eventName: value,
            eventType: prevValue.eventType,
            eventDate: prevValue.eventDate,
            eventTime: prevValue.eventTime

          }
        }
        else if (name === "eventType"){
          return{
            eventName: prevValue.eventName,
            eventType: value,
            eventDate: prevValue.eventDate,
            eventTime: prevValue.eventTime
          }
        }
        else if (name === "eventDate"){
          return{
            eventName: prevValue.eventName,
            eventType: prevValue.eventType,
            eventDate: value,
            eventTime: prevValue.eventTime
          }
        }
        else if (name === "eventTime"){
          return{
            eventName: prevValue.eventName,
            eventType: prevValue.eventType,
            eventDate: prevValue.eventDate,
            eventTime: value
          }
        }
      })
  }

  return(
    <div className = "container">
    <h1>What event would you like to add?</h1>
    <form>
      <input name = "eventName" value = {contact.eventName} onChange = {handleChange} placeholder = "Name of event" />
      <input name = "eventType" value = {contact.eventType} onChange = {handleChange} placeholder = "Type" />
      if
      <input name = "eventDate" value = {contact.eventDate} onChange = {handleChange} placeholder = "Due date" />
      <input name = "eventTime" value = {contact.eventTime} onChange = {handleChange} placeholder = "Estimated time" />
    <button>Submit</button>
    </form>
    </div>
  );
}

export default App;
