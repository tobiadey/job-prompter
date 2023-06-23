import './landing_page.css';
import {Link} from 'react-router-dom'
import Button from '../components/button'


const LandingPage = () => {  
  return (
    <div className="lp lp-body">
        <div className="left-half">
            <div className='left-container'> 

                <div className='content'>
                    <h1 className='header'>Elevate your career with AI-driven Job Applications</h1>
                    <div className="vector-line"></div>
                </div>
                
                <div className='content explanation'>
                    <p>We leverage artificial intelligence to streamline and optimise the creation of job applications. Benefit from the power of AI - Craft a standout job application while saving time and effort.</p>
                </div>
                
                <div className='content'>
                    <div className='cta'>
                        <Link to="/signup">
                            <Button 
                                className="btn" 
                                text={"Get Started"}
                            >
                            </Button> 
                        </Link>
                        <p> <a className='link' href='/login'>Log into your account</a></p>
                    </div> 
                </div>

                <div className='content'>
                    <p>Developed by <strong>AdeyStudios</strong> </p>
                </div>

            </div>
        </div>

        <div className="right-half">
            <div className='right-container'>
            </div>
        </div>

    </div>

  );
}

export default LandingPage