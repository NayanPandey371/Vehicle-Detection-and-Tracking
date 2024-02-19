import {useDropzone} from 'react-dropzone';
import { useMemo } from 'react'


const focusedStyle = {
  borderColor: '#2196f3'
};

export default function Dropzone({onFilesSelected }) {

  const onDrop = (acceptedFiles) => {
    if (acceptedFiles.length > 0){
      console.log('Files selected:', acceptedFiles);
      onFilesSelected(acceptedFiles)
    } 
  }

  const {getRootProps, getInputProps, open, isFocused,
} = useDropzone({
    noClick: true,
    onDrop
  });
 
  const style = useMemo(() => ({
    ...(isFocused ? focusedStyle : {}),
  }), [
    isFocused,
  ]);
 
  return (
    <section className='h-full'>
      <div {...getRootProps({className: 'dropzone', style})} className='h-full flex flex-col my-0 justify-center items-center'>
        <input {...getInputProps()} />
        <p className='text-2xl font-semibold'>Drag and drop your video here.</p>
        <div className='flex justify-center items-align'>
          <button type="button" className='py-2 px-2 text-white text-xl bg-blue-500 cursor-pointer rounded mt-4' onClick={open}>Browse Files</button>
        </div>
      </div>
    </section>
  );
}