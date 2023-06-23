//import all the pages that will need to be routed to
import LandingPage from './pages/landing_page';
import Home from './pages/home'
import Login from './pages/login'

// import the react-router-dom hooks to handle the routing
import { BrowserRouter as Router, Route,Routes  } from 'react-router-dom'

function App() {
  return (
      <Router>
          <Routes>
            <Route path= '/' element = {<LandingPage/>}/>
            <Route path= '/signup' element={<Login />} />
            <Route path= '/login' element={<Login />} />
            <Route path= '/home' element={<Home />} />
          </Routes>
      </Router>
  );
}

export default App;