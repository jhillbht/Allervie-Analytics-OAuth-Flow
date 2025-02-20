async function checkAuthStatus() {
    try {
        const response = await fetch('/api/auth/status');
        const data = await response.json();
        updateAuthStatus(data);
    } catch (error) {
        console.error('Error checking auth status:', error);
    }
}

function updateAuthStatus(data) {
    const container = document.getElementById('auth-status');
    if (data.authenticated) {
        container.innerHTML = '<div class="success">Authenticated</div>';
        fetchAnalyticsData();
    } else {
        container.innerHTML = `<div class="error">Not authenticated. <a href="${data.auth_url}">Login</a></div>`;
    }
}

checkAuthStatus();