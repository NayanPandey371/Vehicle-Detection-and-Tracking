import Navbar from './components/Navbar'
import Landing from './components/Landing'
import './App.css'
import AppRoutes from './routes/routes'
import Footer from './components/Footer'
import Feature from './components/Feature'

function App() {
  return (
    <>
     <Navbar/>
     <AppRoutes />
     <Feature/>
     <Footer/>
    </>
  )
}

export default App
