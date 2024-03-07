import { useEffect, useState } from "react"
import axios from "axios"
import Skeleton from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css'
import ReactPlayer from 'react-player'

export default function Result() {

    const [isVideo, setIsVideo] = useState(false)

    useEffect(() => {
        const getVideo = async () => {
            try{
                const response = await axios.get('http://127.0.0.1:8000/get-result')
                setIsVideo(true)
                console.log(response.data)
            }catch(err){
                console.log(err)
            }
        }
        getVideo()
    }, [])

  return (
    <div className="max-w-screen-2xl mx-20 mt-10">
        <div className="flex flex-col justify-center align-center">
            { !isVideo ? (
                <div>
                    <Skeleton containerClassName="flex-1" baseColor='#E8CBF4' highlightColor="#EAE8E7" count={6} height={20}/>
                    <Skeleton containerClassName="flex-1" baseColor='#E8CBF4' highlightColor="#EAE8E7" width="50%" height={20}/>
                </div>    
            ):
            <div className="flex justify-center align-center">
                <ReactPlayer url='/videos/out.mp4'  controls />
            </div>
            }
        </div>
    </div>
  )
}
