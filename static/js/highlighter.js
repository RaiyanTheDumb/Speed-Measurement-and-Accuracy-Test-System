let charSpans;
window.addEventListener('load', function() {
    charSpans = document.querySelectorAll('.char');
});

function highlightChars() {
    const typedText = document.getElementById('user-input').value;
    charSpans.forEach(function(span, index) {
        const typedChar = typedText[index];
        span.classList.remove('correct', 'incorrect', 'current');
        if (typedChar == null) {
            if (index === typedText.length) {
                span.classList.add('current');
            }
        } else if (typedChar === span.textContent) {
            span.classList.add('correct');
        } else {
            span.classList.add('incorrect');
        }
    });
}

function resetHighlights() {
    if (charSpans) {
        charSpans.forEach(function(span) {
            span.classList.remove('correct', 'incorrect', 'current');
        });
    }
}