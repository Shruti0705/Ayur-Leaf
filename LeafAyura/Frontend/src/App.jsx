import { BrowserRouter as Router,Routes,Route } from 'react-router-dom'
import AboutUs from './Pages/AboutUs'
import Contactus from './Pages/Contactus'
import Login from './Pages/Login'
import Signup from './Pages/Signup'
import Error from './Pages/Error'
import Home from './Pages/Home'
import Navbar from './Components/Navbar'
import UploadLeaf from './Pages/Uploadleaf'
import Leafdes from './Pages/Leafdes'
function App() {
 
  return (
    <>

    <Router>
    <Navbar/>
    <Routes>
      <Route path='/' index element={<Home/>}></Route>
      <Route path='/about' element={<AboutUs/>}></Route>
      <Route path='/uploadleaf' element={<UploadLeaf/>}></Route>
      <Route path='/contactus' element={<Contactus/>}></Route>
      <Route path='/login' element={<Login/>}></Route>
      <Route path='/signup' element={<Signup/>}></Route>
      <Route path='/leafdes' element={<Leafdes/>}/>
      <Route path='*' element={<Error/>}></Route>
    </Routes>

      
    </Router>
      
    </>
  )
}

export default App
