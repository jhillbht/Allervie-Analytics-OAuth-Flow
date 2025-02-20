async function fetchAnalyticsData() {
    try {
        const response = await fetch('/api/analytics');
        const data = await response.json();
        displayAnalytics(data);
    } catch (error) {
        console.error('Error fetching analytics:', error);
        displayError(error);
    }
}

function displayAnalytics(data) {
    const container = document.getElementById('analytics-content');
    // Add your visualization logic here
}

function displayError(error) {
    const container = document.getElementById('analytics-content');
    container.innerHTML = `<div class="error">Error: ${error.message}</div>`;
}