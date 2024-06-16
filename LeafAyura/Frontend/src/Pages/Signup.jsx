import { useState } from "react";
import './Signup.css';
import axios from 'axios';
const Signup = () => {
  const [formData, setFormData] = useState({
    email: '',
    username: '',
    password: '',
    confirmPassword: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (formData.password !== formData.confirmPassword) {
      alert("Passwords do not match")
      return;
    }

    try {
      const response = await axios.post('/signup', formData);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };


  return (
    <>
    <div className="signup">
      <form onSubmit={handleSubmit}>
        <label>Email</label>
        <br />
        <input type="email" name="email" value={formData.email} onChange={handleChange} required />
        <br />
        <label>Username</label>
        <br />
        <input type="text" name="username" value={formData.username} onChange={handleChange} required />
        <br />
        <label>Password</label>
        <br />
        <input type="password" name="password" value={formData.password} onChange={handleChange} required />
        <br />
        <label>Confirm password</label>
        <br />
        <input type="password" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} required />
        <br />
        <button type="submit">Signup</button>
      </form>
    </div>
    </>
  );
}

export default Signup;
