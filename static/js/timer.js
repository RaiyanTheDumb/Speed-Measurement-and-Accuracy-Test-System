let seconds = 0;
let timerInterval = null;
let timerRunning = false;

function startTimer() {
    if (!timerRunning) {
        timerRunning = true;
        timerInterval = setInterval(function() {
            seconds++;
            document.getElementById('timer').textContent = seconds + 's';
        }, 1000);
    }
}

function stopTimer() {
    clearInterval(timerInterval);
    timerRunning = false;
}


function resetTimer() {
    stopTimer();
    seconds = 0;
    document.getElementById('timer').textContent = '0s';
}