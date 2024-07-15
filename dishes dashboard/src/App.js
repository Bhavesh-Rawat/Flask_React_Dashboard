import React, { useEffect, useState } from 'react';
import { io } from 'socket.io-client';
import './App.css';

function App() {
  const [dishes, setDishes] = useState([]);
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    fetch('/api/dishes')
      .then(response => response.json())
      .then(data => setDishes(data));
  }, []);

  useEffect(() => {
    const socket = io();

    socket.on('update', (data) => {
      setDishes(dishes => 
        dishes.map(dish => 
          dish.dishId === data.dishId ? { ...dish, isPublished: data.isPublished } : dish
        )
      );
    });

    return () => socket.disconnect();
  }, []);

  const togglePublish = (id) => {
    fetch(`/api/dishes/${id}/toggle`, { method: 'POST' })
      .then(response => response.json())
      .then(data => {
        setDishes(dishes.map(dish => 
          dish.dishId === id ? { ...dish, isPublished: data.isPublished } : dish
        ));
      });
  };

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  return (
    <div className={`App ${darkMode ? 'dark-mode' : ''}`}>
      <header>
        <h1>Dishes Dashboard</h1>
        <button className="theme-toggle-button" onClick={toggleDarkMode}>
          {darkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
        </button>
      </header>
      <ul className="dishes-list">
        {dishes.map(dish => (
          <li key={dish.dishId} className="dish-item">
            <h2>{dish.dishName}</h2>
            <img src={dish.imageUrl} alt={dish.dishName} className="dish-image" />
            <div className="dish-info">
              <p>Published: {dish.isPublished ? 'Yes' : 'No'}</p>
              <button className="publish-button" onClick={() => togglePublish(dish.dishId)}>
                {dish.isPublished ? 'Unpublish' : 'Publish'}
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
