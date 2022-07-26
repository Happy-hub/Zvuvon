import './App.css';
import {useState, useRef} from "react";
import axios from "axios";
import ZvuvonResults from "./components/ZvuvonResults";
import {ProjectileDrawer} from './drawUtils';

const api = axios.create({
    baseURL: `http://localhost:8000/api`
})

function App() {
    const [error, setError] = useState("");

    const [initialValues, setInitialValues] = useState({
        initialAngle: "",
        initialHeight: "",
        initialVelocity: "",
    })
    const canvas = useRef(null);

    const [results, setResults] = useState({
        landingAngle: "",
        landingPosition: "",
        landingVelocity: "",
    })

    const handleInitialAngleChange = (e) => {
        setInitialValues({...initialValues, initialAngle: e.target.value});
    }
    const handleInitialHeightChange = (e) => {
        setInitialValues({...initialValues, initialHeight: e.target.value});
    }
    const handleInitialVelocityChange = (e) => {
        setInitialValues({...initialValues, initialVelocity: e.target.value});
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        let params = {
            initial_angle: initialValues.initialAngle,
            initial_height: initialValues.initialHeight,
            initial_velocity: initialValues.initialVelocity,
        };

        api.get('/calculation/motion', {params: params}).then((resp) => {

            let responseData = resp.data["results"]

            setResults({landingAngle: responseData.landing_angle,
                landingPosition: responseData.landing_position,
                landingVelocity: responseData.landing_velocity})

            let pd = new ProjectileDrawer(canvas, {
                initialAngle: parseFloat(initialValues.initialAngle),
                initialHeight: parseFloat(initialValues.initialHeight),
                initialVelocity: parseFloat(initialValues.initialVelocity),
            }, responseData.landing_position);

            pd.draw();

            setError("");

        }).catch((error) =>{
            if(error.response.status === 400)
            {
                setError("Invalid parameters!");
            }
            else {
                setError("The server took too long to respond!");
            }
        })
    }

  return (
      <div className="App">
          <div className="form-container">
              <form className="calculate-form" onSubmit={handleSubmit}>
                  <div className="input-group input-group-lg mb-3">
                      <input type="number" className="form-control" placeholder="Initial Angle"
                             aria-label="Initial Velocity" aria-describedby="initial-angle" value={initialValues.initialAngle}
                             onChange={handleInitialAngleChange} min={0} max={90}/>
                      <span className="input-group-text" id="initial-angle">°</span>
                  </div>
                  {/*<label htmlFor="initialVelocity" className="form-label ms-2">Initial velocity</label>*/}
                  <div className="input-group input-group-lg mb-3">
                      <input type="number" className="form-control" placeholder="Initial Height"
                             aria-label="Initial Velocity" aria-describedby="initial-height" value={initialValues.initialHeight}
                             onChange={handleInitialHeightChange}/>
                      <span className="input-group-text" id="initial-height">m</span>
                  </div>
                  {/*<label htmlFor="initialVelocity" className="form-label ms-2">Initial velocity</label>*/}
                  <div className="input-group input-group-lg mb-3">
                      <input type="number" className="form-control" placeholder="Initial Velocity"
                             aria-label="Initial Velocity" aria-describedby="basic-addon2" value={initialValues.initialVelocity}
                             onChange={handleInitialVelocityChange}/>
                      <span className="input-group-text" id="initialVelocity">m/s</span>
                  </div>

                  <div className="d-grid gap-2 col-12">
                      <button className="btn btn-dark py-3" type="submit">
                          Calculate
                      </button>
                  </div>

                  {error !== "" && <div className="error_container">
                      <h4>{error}</h4>
                  </div> }
              </form>
          </div>

          <div className="results-container">
              <ZvuvonResults className="results"
                             landing_angle={results.landingAngle}
                             landing_position={results.landingPosition}
                             landing_velocity={results.landingVelocity}/>

              <div className="canvas-container">
                  <canvas ref={canvas}/>
              </div>
          </div>
          <div className="iaf-logo-container">
              <img className="m-2" src="/IAF.png" alt="IAF logo" width="70" height="70"/>
          </div>
      </div>
  );
}

export default App;



