import react from '../assets/react.svg'
import { Link } from "react-router-dom"

export default function Navbar() {
	const navbarItems =[
		{link: "Home", path:"/"},
		{link: "Detect", path:"/detect"},
		{link: "Our Team", path:"/team"}
	]

  return (
		<nav className="w-full flex py-6 justify-between items-center px-8">
			<div className=" flex flex-start ml-28">
				<img src={react} alt=""/>
			</div>
			<div className=" justify-center items-center mr-28">
				<ul className=" flex gap-12 list-none">
					{navbarItems.map((nav, index) => (
						<li key={index} className='font-roboto font-semibold cursor-pointer'>
						<Link to={nav.path}>{nav.link}</Link>
						</li>
					))}
				</ul>
			</div>
		</nav>
  )
}
