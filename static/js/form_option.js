document.addEventListener("DOMContentLoaded", function () {
    const formSelector = document.getElementById("formSelector"); // Dropdown to select forms
    const addFormButton = document.getElementById("addFormButton"); // Button to add new forms dynamically
    const formContainer = document.getElementById("formContainer"); // Container for FormSet
    const totalForms = document.getElementById("id_form-TOTAL_FORMS"); // Hidden input tracking total forms
    const routineRegister = document.getElementById("routineRegister"); // Routine form element
    const knownWorkoutForm = document.getElementById("knownWorkoutForm"); // Known workout form element
    const workoutForm = document.getElementById("WorkoutRegister"); // Form to add workouts

    const formIdMap = {
        workout: "workoutForm",
        routine: "routineRegister",
        known_workout: "knownWorkoutForm",
    };

    // Hide all forms
    function hideAllForms() {
        Object.values(formIdMap).forEach(formId => {
            const form = document.getElementById(formId);
            if (form) {
                form.style.display = "none";
            }
        });
    }

    // Show the selected form based on dropdown value
    function handleFormSelection() {
        hideAllForms();
        const selectedValue = formSelector.value; // Get the selected form type
        const formId = formIdMap[selectedValue]; // Map the selected value to the corresponding form ID
        const form = document.getElementById(formId);
        if (form) {
            form.style.display = "block"; // Show the selected form
        }
    }

    // Update the FormSet and action URL dynamically after creating a routine
    function updateWorkoutRegister(data) {
        formContainer.innerHTML = data.formset_html; // Update the container with the FormSet HTML
        workoutForm.style.display = "block"; // Show the workout form
        workoutForm.action = `/add-exercises/${data.routine_id}/`; // Update the form action URL with the routine ID
    }

    // Generic function to send form data via AJAX
    function sendForm(event, formElement, successCallback) {
        event.preventDefault(); // Prevent the default form submission behavior

        const url = formElement.getAttribute("data-url"); // Get the URL to send the form data to
        const formData = new FormData(formElement); // Collect all form fields and values into a FormData object

        fetch(url, {
            method: "POST",
            headers: { "X-Requested-With": "XMLHttpRequest" }, // Header to indicate an AJAX request
            body: formData,
        })
            .then(response => response.json()) // Parse the JSON response
            .then(data => {
                if (data.success) {
                    successCallback(data); // Call the provided callback if the request is successful
                } else {
                    alert("Error: " + JSON.stringify(data.errors)); // Show errors if the request fails
                }
            })
            .catch(error => console.error("Error:", error)); // Log network or other errors
    }

    // Event listeners for form submissions
    formSelector.addEventListener("change", handleFormSelection);

    addFormButton.addEventListener("click", function () {
        const formCount = parseInt(totalForms.value, 10); // Current number of forms
        const emptyFormTemplate = document.getElementById("emptyFormTemplate").innerHTML; // Template for a new form
        const newFormHTML = emptyFormTemplate.replace(/__prefix__/g, formCount); // Replace placeholders with the current count
        formContainer.insertAdjacentHTML("beforeend", newFormHTML); // Append the new form to the container
        totalForms.value = formCount + 1; // Increment the total form count
    });

    // Handle the routine form submission
    routineRegister.addEventListener("submit", function (e) {
        sendForm(e, routineRegister, updateWorkoutRegister);
    });

    // Handle the known workout form submission
    knownWorkoutForm.addEventListener("submit", function (e) {
        sendForm(e, knownWorkoutForm, function (data) {
            alert(data.message); // Show a success message for known workout
        });
    });

    // Handle the workout form submission
    workoutForm.addEventListener("submit", function (e) {
        sendForm(e, workoutForm, function (data) {
            alert(data.message); // Show a success message for workouts
        });
    });
});
