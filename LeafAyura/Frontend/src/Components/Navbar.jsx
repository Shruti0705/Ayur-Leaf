import { Link} from 'react-router-dom'
import './Navbar.css'
const Navbar = () => {
  return (
    <div className='navbar'>
        <div className='nav-left'>LeafAyura</div>
        <ul className='nav-mid'>
            <li><Link to='/'>Home</Link></li>
            <li><Link to='/uploadleaf'>Upload Leaf</Link></li>
            <li><Link to='/about'>About Us</Link></li>
            
            <li><Link to='/contactus'>Contact us</Link></li>
        </ul>
        
    </div>
  )
}

export default Navbar