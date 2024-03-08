import Logo from '../assets/logo.png'
import { Link } from "react-router-dom"

export default function Navbar() {
	const navbarItems =[
		{link: "Home", path:"/"},
		{link: "Detect", path:"/detect"},
	]

  return (
		<nav className="w-full flex flex-col md:flex-row py-1 justify-between items-center px-8">
			<div className=" flex md:flex-start justify-center items-center md:ml-20 ml-0">
				<Link to="/"><img src={Logo} height={60} width={60} alt="logo"/></Link>
				<span className='ml-[14px] font-roboto font-semibold text-2xl'>Urban Pulse</span>
			</div>
			<div className=" justify-between md:justify-center items-center mt-8 md:mt-0 md:mr-20">
				<ul className=" flex flex-row justify-center gap-12 list-none">
					{navbarItems.map((nav, index) => (
						<li key={index} className='font-roboto font-semibold cursor-pointer hover:text-primary'>
						<Link to={nav.path}>{nav.link}</Link>
						</li>
					))}
				</ul>
			</div>
		</nav>
  )
}
