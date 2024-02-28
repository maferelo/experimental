import React, { useState } from 'react';

interface props {
  name: string;
}

const App: React.FC = (props: props) {
  const [name, setName] = useState()

  return(
    <div>{props.name}</div>
  )
}

export default App
