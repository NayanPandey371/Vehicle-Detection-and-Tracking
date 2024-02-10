import logo from '../assets/logo.png'

export default function Footer() {
    return (
    <div className="max-w-screen-2xl mx-auto mt-10 ">
        <footer className=" p-4 rounded-lg shadow md:px-6 md:py-8 gradientBg">
            <div className=" mx-20 sm:flex sm:items-center sm:justify-between">
                <a href="#" target="_blank" className="flex items-center mb-4 sm:mb-0">
                    <img src={logo} className="mr-4 h-8 ml-2" alt="Logo" />
                    <span className="self-center text-xl font-semibold whitespace-nowrap text-white">Urban Pulse</span>
                </a>
                <ul className="flex flex-wrap items-center mb-6 sm:mb-0">
                    <li>
                        <a href="/home" className="mr-4 text-sm text-gray-500 hover:underline md:mr-6 text-white">About</a>
                    </li>
                    <li>
                        <a href="#" className="mr-4 text-sm text-gray-500 hover:underline md:mr-6 text-white">Privacy
                            Policy</a>
                    </li>
                    <li>
                        <a href="#"
                            className="mr-4 text-sm text-gray-500 hover:underline md:mr-6 text-white">Licensing</a>
                    </li>
                    <li>
                        <a href="team" className="text-sm text-gray-500 hover:underline text-white">Contact</a>
                    </li>
                </ul>
            </div>
            <hr className="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
            <span className="block text-sm text-gray-500 sm:text-center text-white">© 2024 <a href="/" target="_blank" className="hover:underline">Urban Pulse™</a>. All Rights Reserved.
        </span>
        </footer>
    </div>
  )
}
