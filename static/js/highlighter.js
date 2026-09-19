/**
 * highlighter.js
 * Handles real-time character highlighting.
 * Colors characters green (correct) or red (incorrect)
 * as the user types.
 */

// Character spans from the sample text display
let charSpans;

// Initialize spans after page loads
window.addEventListener('load', function() {
    charSpans = document.querySelectorAll('.char');
});

/**
 * Highlight each character based on typed input.
 * Compares typed text against sample text spans.
 * Applies correct, incorrect or current CSS class.
 */
function highlightChars() {
    const typedText = document.getElementById('user-input').value;

    charSpans.forEach(function(span, index) {
        const typedChar = typedText[index];

        // Remove existing highlight classes
        span.classList.remove('correct', 'incorrect', 'current');

        if (typedChar == null) {
            // Character not yet typed
            if (index === typedText.length) {
                span.classList.add('current'); // cursor position
            }
        } else if (typedChar === span.textContent) {
            span.classList.add('correct');     // correct character
        } else {
            span.classList.add('incorrect');   // wrong character
        }
    });
}

/**
 * Remove all highlight classes from character spans.
 * Called when the test is reset.
 */
function resetHighlights() {
    if (charSpans) {
        charSpans.forEach(function(span) {
            span.classList.remove('correct', 'incorrect', 'current');
        });
    }
}