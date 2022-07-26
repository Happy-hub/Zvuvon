import React from 'react';

function ResultItem(props) {
    return (
        <div className={"result_item_container"}>
            <div className={"result_item_label"}>
                <h4>{props.label}</h4>
            </div>
            <div className={"result_item_value"}>
                <h4>{props.value}</h4>
            </div>
        </div>

    );
}

export default ResultItem;