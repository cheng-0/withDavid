import axios from 'axios';
import React, { useState } from 'react';

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [serverRes, setServerRes] = useState('not logged in');

  const login = (e: React.MouseEvent<HTMLButtonElement, MouseEvent>): void => {
    e.preventDefault();

    const credentials = { username: username, password: password };

    axios
      .post('http://localhost:3000/login', credentials)
      .then(res => setServerRes(res.data))
      .catch(e => console.error(e));
  };

  return (
    <>
      <input
        value={username}
        onChange={e => setUsername(e.target.value)}
        type='text'
      />
      <input
        value={password}
        onChange={e => setPassword(e.target.value)}
        type='password'
      />
      <button onClick={login}>login</button>
      <span>{serverRes}</span>
    </>
  );
}

export default App;
