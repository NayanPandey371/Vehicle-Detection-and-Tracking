import {useDropzone} from 'react-dropzone';

export default function Basic({ onFilesSelected }) {
  const {acceptedFiles, getRootProps, open, getInputProps} = useDropzone({
    noClick: true,
    onDropAccepted: () => {handleFileChange()}
  });
  
  // const files = acceptedFiles.map(file => (
  //   <li key={file.path}>
  //     {file.path} - {file.size} bytes
  //   </li>
  // ));
  
  const handleFileChange = () =>{
    onFilesSelected(acceptedFiles)
    // console.log(files)
  }
  return (
    <section>
      <div {...getRootProps({className: 'dropzone'})}>
        <input {...getInputProps()} />
        <p className='text-2xl font-semibold'>Drag and drop your video here.</p>
        <div className='flex justify-center items-align'>
          <button className='py-2 px-2 text-white text-xl bg-blue-500 cursor-pointer rounded mt-4'>Browse Files</button>
        </div>
      </div>
    </section>
  );
}