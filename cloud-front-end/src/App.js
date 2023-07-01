import React, { useEffect, useState } from 'react';
import axios from 'axios';

import './App.css';

function App() {
const [data, setData] = useState([]);

useEffect(() => {
      async function fetchData() {
        try {
          // Taking serialised data running from local server
          const response = await axios.get('http://127.0.0.1:8000');
          console.log(response.data);
        } catch (error) {
          console.error(error);
        }
      }
  }, []);

  return (
    <div className="App">
        <h1> Cloud Services Comparison </h1>
      <div>
        {data.map(item => (
          <div>
            <table key={item.id}>
                <thead>
                    <tr>
                      <th>ID</th>
                      <th>Name</th>
                      <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                  {data.map(item => (
                    <tr key={item.id}>
                      <td>{item.name}</td>
                      <td>{item.number_of_service}</td>
                      <td>{item.number_of_region}</td>
                      <td>{item.number_of_availability_zone}</td>
                    </tr>
                  ))}
              </tbody>            
            </table>

          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
