import { useState } from 'react'
import Dropzone from '../components/Dropzone'
import axios from 'axios'
import ErrorMessage from '../components/ErrorMessage'
import { useNavigate } from 'react-router-dom'

export default function Detect() {

  const [file, setFile] = useState([])
  const [error, setError] = useState(false)
  const [uploadingFirstButton, setUploadingFirstButton] = useState(false);
  const [uploadingSecondButton, setUploadingSecondButton] = useState(false);

  const navigate = useNavigate()

  const onFileSelected = (newFiles) => {
    setFile(newFiles)
  }

  const handleVideoSubmit = async (event, buttonIndex) => {
    event.preventDefault()

    if (file.length === 0) {
      console.log("Error")
      setError(true)
      return
    }
    setError(false)
    const formData = new FormData();
    formData.append('video', file[0]);

    try {
      if(buttonIndex == 1){
          setUploadingFirstButton(true)
          const response = await axios.post('http://127.0.0.1:8000/upload-video', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log('Video uploaded successfully:', response.data);
        setUploadingFirstButton(false)
        navigate('/get-result')
      }
      else{
        setUploadingSecondButton(true)
        const response = await axios.post('http://127.0.0.1:8000/upload-real-video', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log('Video uploaded successfully:', response.data);
        setUploadingSecondButton(true)
      }
      
      // Handle successful upload (e.g., clear form, display success message)
    } catch (error) {
      console.error('Error uploading video:', error);
      // Handle upload errors (e.g., display error message)
    }
  }
  
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
        <div className='w-full py-2 px-2 bg-blue-100 rounded-xl'>
          {file[0].name}
        </div>
      )}
      <div className=" flex flex-col md:flex-row gap-1 w-full">
        <button className="w-full py-2 px-4 mt-2 bg-primary text-white rounded cursor-pointer hover:shadow-boxshadowcolor" onClick={(event) => handleVideoSubmit(event,1)}>
          {uploadingFirstButton? 'Uploading...': 'Upload'}
        </button>
        <button className="w-full py-2 px-4 mt-2 bg-primary text-white rounded cursor-pointer hover:shadow-boxshadowcolor" onClick={(event) => handleVideoSubmit(event,2)}>
          {uploadingSecondButton? 'Uploading...': 'Upload For Real time'}
        </button>
      </div>
      { error && <ErrorMessage errorMessage="Please select a video file."/>}
      </div>
    </div>
  )
}
