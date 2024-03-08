import { useEffect, useState } from "react"
import axios from "axios"
import Skeleton from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css'
import ReactPlayer from 'react-player'
import PieChart from "../components/PieChart";

export default function Result() {

    const [isVideo, setIsVideo] = useState(false)
    const [videoUrl, setVideoUrl] = useState('')
    const [northCount, setNorthCount] = useState({})
    const [southCount, setSouthCount] = useState({})
    const [videoWidth, setVideoWidth] = useState(null);

    const handleOnReady = (event) => {
        // Get video metadata, including width
        const videoMetadata = event.target.getInternalPlayer().getVideoData();
        const width = videoMetadata.width;
    
        // Update state with video width
        setVideoWidth(width);
      };

    useEffect(() => {
        const getVideo = async () => {
            try{
                const response = await axios.get('http://127.0.0.1:8000/get-result')
                setIsVideo(true)
                setVideoUrl('/videos/out.mp4')
                setNorthCount(response.data["north_count"])
                setSouthCount(response.data["south_count"])
            }catch(err){
                console.log(err)
            }
        }
        getVideo()
    }, [])

  return (
    <div className="max-w-screen-2xl mx-20 mt-10">
        { !isVideo ? (
            <div className="flex flex-col justify-center align-center mt-10 mx-24">
                <div className="flex flex-col justify-center align-center ">
                    <Skeleton containerClassName="flex-1" baseColor='#E8CBF4' highlightColor="#EAE8E7" count={6} height={20}/>
                    <Skeleton containerClassName="flex-1" baseColor='#E8CBF4' highlightColor="#EAE8E7" width="50%" height={20}/>
                </div>
            </div>    
        ):(
        <div className="flex flex-col justify-center align-center ">
            <h2 className="text-4xl font-bold text-center mt-2 mb-10 text-primary">Vehicle Detection and Counting</h2>
            <div className="flex justify-center align-center">
            {!videoWidth && <ReactPlayer url={videoUrl} width={videoWidth} onReady={handleOnReady} controls />}
            </div>
            <div className="flex flex-col justify-center align-center mt-10 mb-10">
                <h2 className="text-4xl font-bold text-center mt-2 text-primary ">Vehicle Distribution Chart</h2>
                <div className="flex flex-row justify-center align-center gap-16 mt-10 ">
                    <div className="chartGradientBg rounded-3xl p-10">
                        <PieChart data={northCount}/>
                        <h3 className="text-2xl font-bold text-center mt-2 text-black">North</h3>
                    </div>
                    <div className="chartGradientBg rounded-3xl p-10">
                        <PieChart data={southCount}/>
                        <h3 className="text-2xl font-bold text-center mt-2 text-black">South</h3>                                
                    </div>
                </div>
            </div>
        </div>
        )}
    </div>
  )
}
