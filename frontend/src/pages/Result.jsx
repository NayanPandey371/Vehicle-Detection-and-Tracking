import { useEffect, useState } from "react"
import axios from "axios"
import Skeleton from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css'
import ReactPlayer from 'react-player'
import PieChart from "../components/PieChart";

export default function Result() {

    const [isVideo, setIsVideo] = useState(true)
    const [northCount, setNorthCount] = useState({})
    const [southCount, setSouthCount] = useState({})

    // useEffect(() => {
    //     const getVideo = async () => {
    //         try{
    //             const response = await axios.get('http://127.0.0.1:8000/get-result')
    //             setIsVideo(true)
    //             setNorthCount(response.data["north_count"])
    //             setSouthCount(response.data["south_count"])
    //             console.log(response.data["north_count"])
    //         }catch(err){
    //             console.log(err)
    //         }
    //     }
    //     getVideo()
    // }, [])

  return (
    <div className="max-w-screen-2xl mx-20 mt-10">
            { !isVideo ? (
                <div className="flex flex-col justify-center align-center">
                    <Skeleton containerClassName="flex-1" baseColor='#E8CBF4' highlightColor="#EAE8E7" count={6} height={20}/>
                    <Skeleton containerClassName="flex-1" baseColor='#E8CBF4' highlightColor="#EAE8E7" width="50%" height={20}/>
                </div>    
            ):
            <div className="flex flex-col justify-center align-center">
                <div className="flex justify-center align-center">
                    <ReactPlayer url='/videos/out.mp4'  controls />
                </div>
                <div className="flex justify-center align-center">
                    <div className="flex flex-row justify-center align-center gap-16 mt-10 ">
                        <div className="chartGradientBg rounded-3xl p-10">
                            <PieChart />
                            <h3 className="text-2xl font-bold text-center mt-2 text-black">North</h3>
                        </div>
                        <div className="chartGradientBg rounded-3xl p-10">
                            <PieChart />
                            <h3 className="text-2xl font-bold text-center mt-2 text-black">South</h3>                                
                        </div>

                    </div>
                </div>
            </div>
            }
        </div>
  )
}
