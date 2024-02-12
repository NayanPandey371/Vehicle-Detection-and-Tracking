import { Route, Routes } from 'react-router-dom';
import Home from '../pages/Home'
import Landing from '../components/Landing';

const AppRoutes = () => {
  return (
      <Routes>
        <Route path="/" element={<Landing />} />
      </Routes>
  );
};

export default AppRoutes;
