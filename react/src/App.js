import { useEffect, useState } from "react";
import Axios from "axios";
import Cards from "./Cards";

function App() {
  const [data, setData] = useState([]);
  useEffect(() => {
    Axios.get("http://localhost:8000").then((res) => setData(res.data));
  }, []);
  return (
    <div className="App">
      {data.map((value) => (
        <Cards
          name={value.name}
          age={value.age}
          city={value.city}
          country={value.country}
          id={value.id}
        />
      ))}
    </div>
  );
}

export default App;
