import {useDropzone} from 'react-dropzone';

export default function Basic() {
  const {acceptedFiles, getRootProps, getInputProps} = useDropzone();
  
  const files = acceptedFiles.map(file => (
    <li key={file.path}>
      {file.path} - {file.size} bytes
    </li>
  ));

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