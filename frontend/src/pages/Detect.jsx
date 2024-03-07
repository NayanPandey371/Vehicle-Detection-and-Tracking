import { useState } from 'react'
import Dropzone from '../components/Dropzone'
import axios from 'axios'
import ErrorMessage from '../components/ErrorMessage'
import { useNavigate } from 'react-router-dom'

export default function Detect() {

  const [file, setFile] = useState([])
  // const [videos, setVideos] = useState([]);
  const [error, setError] = useState(false)
  const [uploading, setUploading] = useState(false);
  const navigate = useNavigate()

  const onFileSelected = (newFiles) => {
    setFile(newFiles)
  }

  const handleVideoSubmit = async (event) => {
    event.preventDefault();

    if (file.length === 0) {
      console.log("Error")
      setError(true)
      return
    }
    setError(false)
    const formData = new FormData();
    formData.append('video', file[0]);

    try {
      setUploading(true)
      const response = await axios.post('http://127.0.0.1:8000/upload-video', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log('Video uploaded successfully:', response.data);
      navigate('/get-result')

      
      // Handle successful upload (e.g., clear form, display success message)
    } catch (error) {
      console.error('Error uploading video:', error);
      // Handle upload errors (e.g., display error message)
    }finally{
      setUploading(false)
    }
  };
  
  // useEffect(() => {
  //   // Handle dropped files when they change
  //   if (file.length > 0) {
  //     const newVideos = file.map((file) =>
  //       URL.createObjectURL(file) // Create temporary URL for video preview
  //     );
  //     setVideos(newVideos);
  //   }
  //   // Revoke previously created URLs when unmounted
  //   return () => {
  //     videos.forEach((url) => URL.revokeObjectURL(url));
  //   };
  // }, [file]);
 
  return (
    <div className="w-full flex justify-center items-center">
      <div className="w-96 flex flex-col justify-center items-center ">
      <div>
        <h2 className="text-center font-bold text-3xl my-4">Upload Your Video</h2>
        <p className='text-center'>
          We support MP4 video format.
        </p>
      </div>
      <div className='flex flex-col justify-center items-center h-60 w-full border-2 border-dashed mt-8 mb-4 rounded'>
        <Dropzone onFileSelected={onFileSelected}/>
      </div>
      { file.length>0 && (
        <div className='w-full py-2 px-2 bg-gray-100 rounded-xl'>
          {file[0].name}
        </div>
      )}
      <div className="w-full">
        <button className="w-full py-2 px-4 mt-2 bg-primary text-white rounded cursor-pointer hover:shadow-boxshadowcolor" onClick={handleVideoSubmit}>
          {uploading? 'Uploading...': 'Upload'}</button>
      </div>
      { error && <ErrorMessage errorMessage="Please select a video file."/>}
      {/* {videos.map((videoUrl, index) => (
      <video key={index} src={videoUrl} controls />
      ))} */}
      </div>
    </div>
  )
}
