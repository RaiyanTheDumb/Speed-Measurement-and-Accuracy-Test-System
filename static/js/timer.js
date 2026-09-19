/**
 * timer.js
 * Handles the background timer for the typing test.
 * Tracks elapsed seconds and updates the timer display.
 */

// Timer state variables
let seconds = 0;
let timerInterval = null;
let timerRunning = false;

/**
 * Start the timer.
 * Only starts if not already running.
 * Updates the timer display every second.
 */
function startTimer() {
    if (!timerRunning) {
        timerRunning = true;
        timerInterval = setInterval(function() {
            seconds++;
            document.getElementById('timer').textContent = seconds + 's';
        }, 1000);
    }
}

/**
 * Stop the timer.
 * Clears the interval and marks timer as not running.
 */
function stopTimer() {
    clearInterval(timerInterval);
    timerRunning = false;
}

/**
 * Reset the timer back to zero.
 * Stops the timer and resets the display.
 */
function resetTimer() {
    stopTimer();
    seconds = 0;
    document.getElementById('timer').textContent = '0s';
}