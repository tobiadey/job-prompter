import './landing_page.css';
import {Link} from 'react-router-dom'
import Button from '../components/button'

const LandingPage = () => {  
  return (
    <div className="App App-home-body">
        LandingPage
        <Link to= 'about'> <Button text={'Read More'}  /> </Link>
    </div>
  );
}

export default LandingPage