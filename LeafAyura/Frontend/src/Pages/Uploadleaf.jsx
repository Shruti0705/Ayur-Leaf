import { useState } from 'react';
import axios from 'axios';
import './Uploadleaf.css';
import { useNavigate } from 'react-router-dom';

function UploadLeaf() {
  const [file, setFile] = useState(null);
  const [description, setDescription] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) {
      setError('Please select an image to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('imagefile', file);

    try {
      const response = await axios.post('http://localhost:5000/predict', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      const { LeafName, Uses, error } = response.data;

      if (error) {
        setError(error);
        setDescription('');
      } else {
        setDescription({ LeafName, Uses });
        setError('');
        navigate('/leafdes', { state: { file, description: { LeafName, Uses } } });
      }
    } catch (error) {
      console.error('Error uploading image:', error);
      setError('Error uploading image');
      setDescription('');
    }
  };

  return (
    <div className="uploadleaf-container">
      <h1>Welcome to Leaf ID</h1>
      <p>Identify different types of leaves with our advanced detection technology. Upload an image to get started.</p>

      <form onSubmit={handleSubmit} className="upload-form">
        <input type="file" onChange={handleFileChange} className="file-input" />
        {file && (
          <div className="image-preview">
            <img src={URL.createObjectURL(file)} alt="Selected" className="preview-image" />
          </div>
        )}
        <button type="submit" className="upload-button">Upload Image</button>
      </form>

      {description && (
        <div className="description">
          <h2>Image Description</h2>
          <p>{description.LeafName}</p>
          <p>{description.Uses}</p>
        </div>
      )}

      {error && (
        <div className="error">
          <p>{error}</p>
        </div>
      )}
    </div>
  );
}

export default UploadLeaf;
