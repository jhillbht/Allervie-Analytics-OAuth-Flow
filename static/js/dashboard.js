// Dashboard JavaScript

// Fetch active users data
async function fetchActiveUsers() {
    try {
        const response = await fetch('/api/active-users');
        const data = await response.json();
        
        if (data.success) {
            return data.data;
        } else {
            throw new Error(data.error);
        }
    } catch (error) {
        console.error('Error fetching active users:', error);
        return null;
    }
}

// Fetch traffic sources data
async function fetchTrafficSources() {
    try {
        const response = await fetch('/api/traffic-sources');
        const data = await response.json();
        
        if (data.success) {
            return data.data;
        } else {
            throw new Error(data.error);
        }
    } catch (error) {
        console.error('Error fetching traffic sources:', error);
        return null;
    }
}

// Initialize charts
async function initializeCharts() {
    // Active Users Chart
    const activeUsersData = await fetchActiveUsers();
    if (activeUsersData) {
        const ctx = document.getElementById('active-users-chart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: activeUsersData.map(d => d.date),
                datasets: [
                    {
                        label: 'Active Users',
                        data: activeUsersData.map(d => d.active_users),
                        borderColor: '#3498db',
                        tension: 0.1
                    },
                    {
                        label: 'New Users',
                        data: activeUsersData.map(d => d.new_users),
                        borderColor: '#2ecc71',
                        tension: 0.1
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    title: {
                        display: true,
                        text: 'User Activity (Last 30 Days)'
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Traffic Sources Chart
    const trafficData = await fetchTrafficSources();
    if (trafficData) {
        const ctx = document.getElementById('traffic-sources-chart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: trafficData.map(d => d.source),
                datasets: [{
                    label: 'Sessions',
                    data: trafficData.map(d => d.sessions),
                    backgroundColor: '#3498db'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    title: {
                        display: true,
                        text: 'Traffic Sources'
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
}

// Initialize when document is ready
document.addEventListener('DOMContentLoaded', initializeCharts);
