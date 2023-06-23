import './home.css';
import {Link} from 'react-router-dom'
import Button from '../components/button'

const Home = () => {  
  return (
    <div className="App App-home-body">
        Home
        <Link to= '/chat'> <Button text={'Read More'}  /> </Link>
    </div>
  );
}

export default Home