let typingStarted = false;
const userInput = document.getElementById('user-input');

// Wait for page to fully load before running
window.addEventListener('load', function() {

    const charSpans = document.querySelectorAll('.char');
    const sampleText = Array.from(charSpans).map(span => span.textContent).join('');

    // Start timer on first keypress
    userInput.addEventListener('keydown', function(event) {
        if (!typingStarted) {
            typingStarted = true;
            startTimer();
        }
    });

    // Check input on every keystroke
    userInput.addEventListener('input', function() {
        const typed = userInput.value;
        highlightChars();

        if (typed.length >= sampleText.length) {
            stopTimer();
            sendResults(typed, sampleText);
        }
    });

    // Reset button
    document.getElementById('reset-btn').addEventListener('click', function() {
        typingStarted = false;
        resetTimer();
        resetHighlights();
        userInput.value = '';
        document.getElementById('wpm').textContent = '0';
        document.getElementById('accuracy').textContent = '0%';
        document.getElementById('errors').textContent = '0';
    });

    // Prevent copy-paste
    userInput.addEventListener('paste', function(event) {
        event.preventDefault();
    });

});

// Send results to Flask
function sendResults(typedText, sampleText) {
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
        document.getElementById('wpm').textContent = data.wpm;
        document.getElementById('accuracy').textContent = data.accuracy + '%';
        document.getElementById('errors').textContent = data.errors;
    });
}