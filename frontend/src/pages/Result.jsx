import { useEffect, useState } from "react"
import axios from "axios"
import Loader from "../components/Loader"

export default function Result() {

    const [isVideo, setIsVideo] = useState(false)
    const [videoSrc, setVideoSrc] = useState()

    useEffect(() => {
        const getVideo = async () => {
            try{
                const response = await axios.get('http://127.0.0.1:8000/get-result')
                console.log("Message", response.data)
            }catch(err){
                console.log(err)
            }
            finally{
                const video_path = '../../../output/out.mp4'
                setVideoSrc(video_path)
                setIsVideo(true)
            }
        }
        getVideo()
    }, [])

  return (
    <div>
    { !isVideo && <Loader/>}
    hello
    </div>
  )
}
