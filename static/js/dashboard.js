// Get typing level based on WPM
function getTypingLevel(wpm) {
    if (wpm <= 30) return { level: '🐢 Beginner', color: '#f38ba8' };
    else if (wpm <= 50) return { level: '⌨️ Average', color: '#fab387' };
    else if (wpm <= 75) return { level: '🌊 Fluent', color: '#cba6f7' };
    else if (wpm <= 100) return { level: '⚡ Fast', color: '#89b4fa' };
    else return { level: '🏆 Expert', color: '#a6e3a1' };
}
// Show the modal with results
function showDashboard(wpm, accuracy, errors, timeTaken) {
    document.getElementById('modal-wpm').textContent = wpm;
    document.getElementById('modal-accuracy').textContent = accuracy + '%';
    document.getElementById('modal-errors').textContent = errors;
    document.getElementById('modal-time').textContent = timeTaken + 's';
    const { level, color } = getTypingLevel(wpm);
    const levelEl = document.getElementById('modal-level');
    levelEl.textContent = level;
    levelEl.style.color = color;
    // Show the modal
    document.getElementById('modal-overlay').classList.remove('hidden');
}

// Hide the modal
function hideDashboard() {
    document.getElementById('modal-overlay').classList.add('hidden');
}

// Close button
document.getElementById('modal-close-btn').addEventListener('click', function() {
    hideDashboard();
});

// Retry button — close modal and reset everything
document.getElementById('modal-retry-btn').addEventListener('click', function() {
    hideDashboard();
    document.getElementById('reset-btn').click();
});