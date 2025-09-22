
let currentStep = 0;
const cards = document.querySelectorAll(".quiz-card");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const submitBtn = document.getElementById("submitBtn");

function showStep(n) {
    cards.forEach((card, i) => card.style.display = i === n ? "block" : "none");
    prevBtn.style.display = n === 0 ? "none" : "inline-block";
    nextBtn.style.display = n === cards.length - 1 ? "none" : "inline-block";
    submitBtn.style.display = n === cards.length - 1 ? "inline-block" : "none";
}

function nextPrev(n) {
    const selected = cards[currentStep].querySelector("input[type='radio']:checked");
    if (n == 1 && !selected) {
        alert("Please select an answer!");
        return;
    }
    currentStep += n;
    showStep(currentStep);
}

showStep(currentStep);
