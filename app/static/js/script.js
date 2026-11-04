/**
 * This function is called when clicking a button to bring the user 
 * to the next "step" or page in the procedure.
 * If all fields are verified, it will call showStep() to bring
 * the user to the desired step.
 * @param stepNumber: the number of the step/page to display.
 * 
 * !! Currently not generalized to all fields/steps.
 */
function goToStep(stepNumber) {
    if (!document.getElementById("company").value) {
        alert("Please enter a company.");
        return;
    }
    showStep(stepNumber);
}


/**
 * The current function to bring user to the next step.
 * There is no validation, but it works for all steps.
 * @param stepNumber: the number of the step/page to display.
 */
function showStep(stepNumber) {

    document.querySelectorAll('.step').forEach(step => {
        step.classList.remove('active');
    });

    document.getElementById('step' + stepNumber)
        .classList.add('active');

    document.getElementById("progress").innerText =
        `Step ${stepNumber} of 5`;
}


// Used by addSetpoint() in calcart1_test.html //
let setpointCount = 1;
/**
 * This function is used to add new setpoints in /calcart1/test/
 */
function addSetpoint() {

    setpointCount++;

    const container = document.getElementById("setpoint_container");

    const newCard = document.createElement("div");
    newCard.className = "section-card";

    newCard.innerHTML = `
        <h3>Setpoint ${setpointCount}</h3>

        <div class="field">
            <label>Setpoint</label>
            <input type="number" step="any" name="setpoint[${setpointCount}]">
        </div>

        <div class="field">
            <label>Standard</label>
            <input type="number" step="any" name="standard[${setpointCount}]">
        </div>

        <div class="field">
            <label>Instrument</label>
            <input type="text" name="instrument[${setpointCount}]">
        </div>
    `;

    container.appendChild(newCard);
}


/**
 * Opens a file dialog popup for the user to select a save directory for the results.
 * Asynchronously calls the .save_file method from the pywebview window's javascript API.
 * This method returns the directory (a string) as a promise in javascript, which is stored
 * in `const directory`. Then the input box from the html is updated accordingly.
 */
async function chooseFolder() {

    const directory = await window.pywebview.api.choose_folder();

    if (directory) {

        document.getElementById("save_directory").value = directory;

        const status = await window.pywebview.api.get_status();

        document.getElementById("report_btn").disabled = 
            !(status.report_complete && status.calibration_complete);
    }
    
}

/**
 * Whenever one of the three steps towards completing 
 */