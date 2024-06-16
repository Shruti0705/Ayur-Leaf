import { useLocation } from 'react-router-dom';

function Leafdes() {
  const location = useLocation();
  const { file, description } = location.state;

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8">
          <div className="card">
            <div className="card-body">
              <h4 className="card-title">Image detected successfully</h4>
              <p className="card-text">The image you uploaded was:</p>
              <div>
                <img src={URL.createObjectURL(file)} alt="Uploaded" className="img-fluid mb-3" />
              </div>
              <p className="card-text">Name of the leaf: {file.name}</p>
              <p className="card-text">Details: {JSON.stringify(description.LeafName)}</p>
              <p className="card-text">Details:{JSON.stringify(description.Uses)}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Leafdes;
