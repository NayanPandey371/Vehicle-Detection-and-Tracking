import Navbar from './components/Navbar'
import Landing from './components/Landing'
import './App.css'
import AppRoutes from './routes/routes'
import Footer from './components/Footer'

function App() {
  return (
    <>
     <Navbar/>
     <AppRoutes />
     <Footer/>
    </>
  )
}

export default App
