import Logo from '../assets/logo.png'
import { Link } from "react-router-dom"

export default function Navbar() {
	const navbarItems =[
		{link: "Home", path:"/"},
		{link: "Detect", path:"/detect"},
		{link: "Our Team", path:"/team"}
	]

  return (
		<nav className="w-full flex py-1 justify-between items-center px-8">
			<div className=" flex flex-start justify-center items-center ml-20">
				<img src={Logo} height={60} width={60} alt="logo"/>
				<span className='ml-[14px] font-roboto font-semibold text-2xl'>Urban Pulse</span>
			</div>
			<div className=" justify-center items-center mr-20">
				<ul className=" flex gap-12 list-none">
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
