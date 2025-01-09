document.addEventListener("DOMContentLoaded", function () {
    const forms = document.querySelectorAll(".ajaxForm");

    forms.forEach((form) => {
        form.addEventListener("submit", function (event) {
            event.preventDefault(); 

            const url = form.getAttribute("data-url"); 
            const formData = new FormData(form); 

            fetch(url, {
                method: "POST",
                headers: {
                    "X-Requested-With": "XMLHttpRequest", 
                },
                body: formData,
            })
                .then((response) => response.json()) 
                .then((data) => {
                    if (data.success) {
                        alert(data.message); 
                        window.location.replace("/workouts/goals"); 
                    } else {
                        alert("Error: " + JSON.stringify(data.errors)); 
                    }
                })
                .catch((error) => console.error("Error:", error)); 
        });
    });
});
