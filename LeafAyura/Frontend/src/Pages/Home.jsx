import './Home.css'
import {Link} from "react-router-dom"

const Home = () => {
  return (
    <>

    
    <div className="mid-main">
            <p>Experience Holistic Wellness Through this <br/> Ayurvedic Assistant... </p>
        </div>
        <div className="low-main">
            <div className="low-main-left">
                <p>Explore the Ancient wisdom of ayurveda and discover natural remedies for a balanced, healthy life.
                    our size guides you through the identification
                    and benefits of ayurvedic medicinal herbs to enhance 
                    your well-being Naturally and Holistically</p>
                    <br/>
                <div className="check">
                    <ul className="ul1">
                        <li>identify Ayurvedic Leafs</li>
                        <li>Learn Ayurvedic Wisdom</li>
                        <li>Herbal Remedies</li>
                    </ul>
                    <ul className="ul2">
                        <li>Explore Ancient Remedies</li>
                        <li>Get Accurate Knowledge</li>
                        <li>Join our community</li>
                    </ul>
                </div>
            </div>
            
            </div>
            <div className='btn'><button className='button'><Link to='/uploadleaf'>Get Started</Link></button></div>
            
</>
  );
};

export default Home;
