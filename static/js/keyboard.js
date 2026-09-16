let typingStarted = false;
let resultsSent = false;
let sampleText = '';

const userInput = document.getElementById('user-input');

// Wait for page to fully load before running
window.addEventListener('load', function() {

    // Get sample text cleanly — trim each span
    const charSpans = document.querySelectorAll('.char');
    sampleText = Array.from(charSpans)
                      .map(span => span.textContent)
                      .join('')
                      .trim();

    console.log('Sample text:', sampleText);
    console.log('Sample length:', sampleText.length);

    userInput.addEventListener('keydown', function(event) {
        if (!typingStarted && !resultsSent) {
            typingStarted = true;
            startTimer();
        }
    });

    // Check input on every keystroke
   userInput.addEventListener('input', function() {
        if (resultsSent) return;

        const typed = userInput.value;
        highlightChars();
        updateLiveStats(typed);

        console.log('Typed length:', typed.length, 'Sample length:', sampleText.length);

        if (typed.length >= sampleText.length) {
            resultsSent = true;
            userInput.setAttribute('disabled', 'true');
            stopTimer();
            setTimeout(function() {
                sendResults(typed, sampleText);
            }, 300);
        }
    });

    // Reset button
    document.getElementById('reset-btn').addEventListener('click', function() {
        typingStarted = false;
        resultsSent = false;
        resetTimer();
        resetHighlights();
        userInput.removeAttribute('disabled');
        userInput.value = '';
        document.getElementById('wpm').textContent = '0';
        document.getElementById('accuracy').textContent = '0%';
        document.getElementById('errors').textContent = '0';
        userInput.focus();
    });

    // Prevent copy-paste
    userInput.addEventListener('paste', function(event) {
        event.preventDefault();
    });

});

// Update the on-page stats live, on every keystroke
function updateLiveStats(typed) {
    const elapsedMinutes = seconds / 60;
    const wpm = elapsedMinutes > 0 ? Math.round((typed.length / 5) / elapsedMinutes) : 0;

    const total = Math.min(sampleText.length, typed.length);
    let correct = 0;
    for (let i = 0; i < total; i++) {
        if (sampleText[i] === typed[i]) correct++;
    }
    const errors = (total - correct) + Math.abs(typed.length - sampleText.length);
    const accuracy = typed.length > 0
        ? Math.min(Math.round((correct / sampleText.length) * 100), 100)
        : 0;

    document.getElementById('wpm').textContent = wpm;
    document.getElementById('accuracy').textContent = accuracy + '%';
    document.getElementById('errors').textContent = errors;
}

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
        showDashboard(data.wpm, data.accuracy, data.errors, seconds);
    });
}