import logo from '../assets/logo.png'

export default function Landing() {
  return (
    <div className="max-w-screen-2xl mx-20 mt-16">
      <div className='gradientBg rounded-xl rounded-br-[80px]'>
        <div className="flex flex-row justify-between items-center gap-1">

          <div className='p-4 ml-4 '>
            <h2 className='text-4xl text-white mb-4'>Vehicle Detection</h2>
            <h2 className='text-4xl text-white mb-4'>and</h2>
            <h2 className='text-4xl text-white mb-4'>Counting</h2>
            <div className='w-2/3 mt-[6px] mb-[30px]'>
              <p className='text-white text-[12px] w-2/3'>
                Ever wished you could monitor your property or fleet of vehicles with eagle-eyed accuracy? Look no further! 
                This web application leverages the power of YOLO (You Only Look Once) to detect and track vehicles,
                providing you with invaluable insights and security.
              </p>
            </div>
            
            <div>
              <button className="py-2 px-4 bg-primary text-white rounded cursor-pointer ">Get Started</button>
            </div>
          </div>

          <div>
            <img src={logo} className='h-40 w-40'/>
          </div>
        </div>
      </div>
    </div>
  )
}
