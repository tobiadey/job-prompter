import './login.css';
import logo from '../logo.svg';
import {Link, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import jwt_decode from 'jwt-decode';

// TODO:
// - use parmas to check if login or sign up & populate with required text
// - fix ui to look more like figma design 

function Login() { 
    const navigate = useNavigate();
    const [ user, setUser] = useState({});

    function handleCallbackResponse(response) {
        console.log("JWT TOKEN:", response.credential);
        var userObject = jwt_decode(response.credential);
        console.log(userObject);

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userObject)
        };
        fetch("/authenticate_user", requestOptions).then(res => res.json()).then(data => {
            setUser(data);
          })
        navigate("/home");
    }


    useEffect(() => {
        //https://developers.google.com/identity/gsi/web/reference/js-reference#ux_mode
        window.google.accounts.id.initialize({
        client_id:"1086140467707-v0s3fc491criqu6s9bglbspt9is2d68f.apps.googleusercontent.com",
        callback: handleCallbackResponse,
        // ux_mode: "redirect",
        // login_uri: "http://localhost:5000/api",
        });

        window.google.accounts.id.prompt();

        window.google.accounts.id.renderButton(
            document.getElementById("signInDiv"),
            {
                theme:"outline",
                size:"large",
                width:"495",
                shape:"circle",
                text:"continue_with",
                logo_alignment: "left",
            });

    },[]);
  return (
    <div className="login login-body">
        <div className="left-half">
            <div className='left-container'>
                <div className='absolute-content'>
                    <img src={logo} className="logo-small" alt="logo" />
                </div>
                <div className='content'>
                    <h1>Get exclusive access to Lorem Ipsum</h1>
                    <p>Lorem ipsum dolor sit amet consectetur. Pellentesque urna facilisi sit facilisi. Sed etiam in ornare praesent. Sapien pellentesque vulputate integer egestas egestas. Sed felis elit ultrices nunc non. Amet aliquam pretium vitae eu. Lobortis volutpat mauris egestas gravida amet rhoncus felis.</p>
                </div>
            </div>
        </div>
        <div className="right-half">
            <div className='right-container'>

                <div className='content'>
                    <h1>Create an account</h1>
                </div>


                <div className='content'>
                    <p>Sign up quickly and securely on our platform using your Google account</p>
                </div>

                <div className='content'>
                    <div id='signInDiv' ></div>
                </div>

                <div className='special-content'>
                    <p>Already have an account?</p> 
                    <Link to="/login">
                        <p className='blue-text'>Log into your account.</p>
                    </Link>
                </div>

                <div className='absolute-content'>
                </div>

            </div>
        </div>
    </div>
  );
}

export default Login