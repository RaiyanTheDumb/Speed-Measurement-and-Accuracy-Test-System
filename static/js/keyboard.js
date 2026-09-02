let typingStarted = false;
const userInput = document.getElementById('user-input');
const sampleText = document.getElementById('sample-text').textContent;
userInput.addEventListener('keydown', function(event) {
    if (!typingStarted) {
        typingStarted = true;
        startTimer();
    }
});

userInput.addEventListener('input', function() {
    const typed = userInput.value;

    if (typed.length === sampleText.length) {
        stopTimer();
        sendResults(typed);
    }
});
function sendResults(typedText) {
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            typed_text: typedText,
            sample_text: sampleText,
            time_seconds: seconds
        })
    })
    .then(response => response.json())
    .then(data => {
        // Update stats panel with results
        document.getElementById('wpm').textContent = data.wpm;
        document.getElementById('accuracy').textContent = data.accuracy + '%';
        document.getElementById('errors').textContent = data.errors;
    });
}
document.getElementById('reset-btn').addEventListener('click', function() {
    typingStarted = false;
    resetTimer();
    userInput.value = '';
    document.getElementById('wpm').textContent = '0';
    document.getElementById('accuracy').textContent = '0%';
    document.getElementById('errors').textContent = '0';

});
userInput.addEventListener('paste', function(event) {
    event.preventDefault();
});