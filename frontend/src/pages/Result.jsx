import { useEffect, useState } from "react"
import axios from "axios"
import Skeleton from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css'
import ReactPlayer from 'react-player'
import { Player } from 'video-react';

export default function Result() {


    const [isVideo, setIsVideo] = useState(true)

    // useEffect(() => {
    //     const getVideo = async () => {
    //         try{
    //             const response = await axios.get('http://127.0.0.1:8000/get-result')
    //             setIsVideo(true)
    //             console.log(response.data)
    //         }catch(err){
    //             console.log(err)
    //         }
    //     }
    //     getVideo()
    //     // Clean up temporary URL on component unmount
    //     //  return () => URL.revokeObjectURL(videoUrl);
    // }, [])

  return (
    <div className="max-w-screen-2xl mx-20 mt-10">
        <div className="flex flex-col justify-center align-center">
            { !isVideo ? (
                <Skeleton containerClassName="flex-1" baseColor='#7734e7' highlightColor="#EAE8E7" count={7} />
            ):
            (<ReactPlayer
                url="/videos/out.mp4"
                controls
            />)}
        </div>
    </div>
  )
}
