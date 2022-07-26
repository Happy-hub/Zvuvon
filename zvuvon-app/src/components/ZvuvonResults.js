import React from 'react';
import ResultItem from "./ResultItem";


function ZvuvonResults(props) {
    return (
        <div className={props.className}>
            <ResultItem name={"landing_angle"}
                        label="Landing Angle"
                        value={props.landing_angle} />
            <ResultItem name={"landing_position"}
                        label="Landing Position"
                        value={props.landing_position} />
            <ResultItem name={"landing_velocity"}
                        label="Landing Velocity"
                        value={props.landing_velocity} />
        </div>
    );
}

export default ZvuvonResults;