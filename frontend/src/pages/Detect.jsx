import { useState } from 'react'
import Dropzone from '../components/Dropzone'
import NewDropzone from '../components/NewDropzone'

export default function Detect() {

  const [files, setFiles] = useState([]);

  const onFilesSelected = (newFiles) => {
    setFiles(newFiles)
  }
  console.log(files)
  return (
    <div className="w-full flex justify-center items-center">
      <div className="w-96 flex flex-col justify-center items-center ">
      <div>
        <h2 className="text-center font-bold text-3xl my-4">Upload Your Video</h2>
        <p className='text-center'>
          We support MP4 video format.
        </p>
      </div>
      <div className='flex flex-col justify-center items-center h-60 w-full border-2 border-dashed my-8 rounded'>
        <Dropzone onFilesSelected={onFilesSelected}/>
        {/* <NewDropzone/> */}
      </div>
      <div className="w-full">
        <button className="w-full py-2 px-4 mt-4 bg-primary text-white rounded cursor-pointer hover:shadow-boxshadowcolor">Upload</button>
      </div>
        <div>

        </div>
      </div>
    </div>
  )
}
