// Select the canvas where the chart will be rendered
const ctx = document.getElementById('progressChart').getContext('2d');

// Fetch data from the ProgressView in Django
fetch('/workouts/progress_data/')  // Update URL to match your Django view endpoint
    .then(response => response.json())
    .then(data => {
        // Prepare data structures for Chart.js
        const labels = [];  // Dates for X-axis
        const datasets = [];  // Array to store dataset for each exercise

        // Iterate through each exercise's history
        data.exercises.forEach((exerciseData, index) => {
            const exercise = exerciseData.exercise;
            const history = exerciseData.history;

            // Extract dates and weights for each exercise
            const exerciseLabels = history.map(entry => entry.date);
            const weights = history.map(entry => entry.weight);

            // Add dates to the main labels array only if it's the first exercise (to avoid duplicates)
            if (index === 0) {
                labels.push(...exerciseLabels);
            }

            // Create a dataset for each exercise
            datasets.push({
                label: exercise,
                data: weights,
                fill: false,
                borderColor: `hsl(${index * 50}, 70%, 50%)`,  // Unique color per exercise
                tension: 0.2  // Smoothness for line
            });
        });

        // Create the line chart
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: datasets
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: true,
                        position: 'top'
                    }
                },
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'Date'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Weight (lbs)'
                        }
                    }
                }
            }
        });
    })
    .catch(error => console.error('Error fetching data:', error));
