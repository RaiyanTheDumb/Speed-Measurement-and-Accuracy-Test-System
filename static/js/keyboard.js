let typingStarted = false;
const userInput = document.getElementById('user-input');

userInput.addEventListener('keydown', function(event) {
    if (!typingStarted) {
        typingStarted = true;
        startTimer();
    }
});
document.getElementById('reset-btn').addEventListener('click', function() {
    typingStarted = false;
    resetTimer();
    userInput.value = '';  // clears the input box
});
userInput.addEventListener('paste', function(event) {
    event.preventDefault();
});