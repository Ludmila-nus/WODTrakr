document.addEventListener("DOMContentLoaded", function () {
    const checkboxes = document.querySelectorAll(".goal-checkbox");
    const date = document.querySelector("#date");
    const updateGoalButton = document.querySelector("update-goal");

    checkboxes.forEach((checkbox) => {
        checkbox.addEventListener("change", function () {
            const goalId = this.dataset.goalId;
            const checked = this.checked;

            fetch(`/goals/${goalId}/update`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    date: date,
                    checked: checked,
                }),
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                });
        });
    }); 
   
    updateGoalButton.addEventListener("click", function () {
        const goalId = this.dataset.goalId;
        const checked = this.checked;

        fetch(`/goals/${goalId}/update`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                date: date,
                checked: checked,
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
            });
    });

});
