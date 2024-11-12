// Select the canvas element by its ID
const ctx = document.getElementById('termsChart').getContext('2d');

// Use fetch to get data from the Django view
fetch('/terms_data/')  // URL of the JSON endpoint
    .then(response => response.json())
    .then(data => {
        // Configure the chart with the obtained data
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,  // Category labels
                datasets: [{
                    label: 'Total per Category',
                    data: data.totals,  // Totals per category
                    backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'],  // Colors for each bar
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: true,
                        position: 'top'
                    }
                }
            }
        });
    })
    .catch(error => console.error('Error fetching data:', error));  // Log any errors in the console

