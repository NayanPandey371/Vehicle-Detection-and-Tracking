import Hero from '../assets/hero.jpg'
import Detection from '../assets/detection.png'
import Classification from '../assets/classification.png'
import Piechart from '../assets/pie_chart.png'

export default function Feature() {
  return (
    <div className="max-w-screen-2xl mx-20 mt-10">
        <div className='mb-10'>
            <h2 className="text-center text-bold text-4xl text-primary">Features</h2>
        </div>
        {/* Detection  */}
        <div className="flex flex-row justify-between items-center gap-1 ml-4">
            <div className='w-1/2 px-4'>
                <img src={Detection} alt="Hero image" />
            </div>

            <div className='w-2/5'>
                <h2 className='text-semibold text-3xl text-primary mb-4'>Detection and Counting</h2>
                <p>Detection and counting of vehicle based on video using YOLO.</p>
            </div>
        </div>
        {/* Classification  */}
        <div className="flex flex-row justify-between items-center gap-1 ml-4">
            <div className='w-2/5'>
                <h2 className='text-semibold text-3xl text-primary mb-4'>Classification of Vehicles</h2>
                <p>Detection and counting of vehicle based on video using YOLO.</p>
            </div>

            <div className='w-1/2 px-4'>
                <img src={Classification} alt="Classification image" />
            </div>
        </div>

        <div className="flex flex-row justify-between items-center gap-1 ml-4">
            <div className='w-1/2 px-4'>
                <img src={Piechart} alt="Hero image" />
            </div>

            <div className='w-2/5'>
                <h2 className='text-semibold text-3xl text-primary mb-4'>Detection and Counting</h2>
                <p>Detection and counting of vehicle based on video using YOLO.</p>
            </div>
        </div>
    </div>
  )
}
