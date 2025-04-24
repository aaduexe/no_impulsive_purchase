const addItemBtn = document.getElementById("open-adder");
const closeAdder = document.getElementById("close-adder");
const popupAdder = document.getElementById("adder");

const reviewerBtn = document.getElementById("open-reviewer");
const closeReviewer = document.getElementById("close-reviewer");
const popupReviewer = document.getElementById("reviewer");

const message = document.getElementById("message");

// Function to open popupAdder at a random position
addItemBtn.addEventListener("click", () => {
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;

    // Get random top and left position for the popupAdder
    const randomTop = Math.floor(Math.random() * (windowHeight - 300)); // 300px is the height of the popupAdder
    const randomLeft = Math.floor(Math.random() * (windowWidth - 300)); // 300px is the width of the popupAdder

    // Apply random positions to the popupAdder
    popupAdder.style.top = `${randomTop}px`;
    popupAdder.style.left = `${randomLeft}px`;

    // Show the popupAdder
    popupAdder.style.display = "block";
});

// Function to open popupReviewer at a random position
reviewerBtn.addEventListener("click", () => {
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;

    // Get random top and left position for the popupAdder
    const randomTop = Math.floor(Math.random() * (windowHeight - 300)); // 300px is the height of the popupAdder
    const randomLeft = Math.floor(Math.random() * (windowWidth - 300)); // 300px is the width of the popupAdder

    // Apply random positions to the popupAdder
    popupReviewer.style.top = `${randomTop}px`;
    popupReviewer.style.left = `${randomLeft}px`;

    // Show the popupAdder
    popupReviewer.style.display = "block";
});



// Close the popupAdder
closeAdder.addEventListener("click", () => {
    message.textContent = "";
    popupAdder.style.display = "none";
});

// Close the popupReviewer
closeReviewer.addEventListener("click", () => {
    popupReviewer.style.display = "none";
});


// Temp function to handle the message for add item
function handleClick() {
    const input = document.getElementById("itemInput");
    

    const itemName = input.value.trim();

    if (itemName) {
        input.value = ""; // clear input
        message.style.display = "block";
        message.textContent = `The button was clicked, and as it is a mock website nothing happened. However in full website the item "${itemName}" should get saved with today's date and will be ready for review.`;
    }
}