import { Route, Routes } from 'react-router-dom';
import Home from '../pages/Home'
import Detect from '../pages/Detect';

const AppRoutes = () => {
  return (
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/detect" element={<Detect/>} />
      </Routes>
  );
};

export default AppRoutes;
