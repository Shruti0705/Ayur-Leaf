import { useState } from "react";
import './Login.css';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(username, password);
        
    };

    return (
        <div>
           
            <div className="login-container">
                <h2 className="login-title">Existing User! Login</h2>
                <form className="login-form" onSubmit={handleSubmit}>
                    <label htmlFor="username">Enter your Email</label>
                    <input 
                        type="text"  
                        id="username"
                        value={username} 
                        onChange={(e) => setUsername(e.target.value)}
                    />
                    <label htmlFor="password">Enter your password</label>
                    <input 
                        type="password" 
                        id="password"
                        value={password} 
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    <button type="submit">Login</button>
                </form>
            </div>
        </div>
    );
}

export default Login;
