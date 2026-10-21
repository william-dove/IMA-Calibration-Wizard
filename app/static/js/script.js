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