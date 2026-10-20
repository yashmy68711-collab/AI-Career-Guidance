const assessmentButton = document.getElementById("assessmentButton");
const assessmentMessage = document.getElementById("assessmentMessage");

assessmentButton.addEventListener("click", function () {
    assessmentMessage.textContent =
        "Career assessment is coming soon! We'll build it in Day 3.";
});