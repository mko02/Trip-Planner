import { Routes, Route} from "react-router-dom";

import Home from "./Pages/Home"
import TransactionSheet from "./Pages/TransactionSheet";
import Trip from "./Pages/Trip";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home/>}/> 
        <Route path="/currenttrip" element={<Trip />}/> 
        <Route path="/transactionsheet" element={<TransactionSheet />}/>
      </Routes>
    </div>
  );
}

export default App;
