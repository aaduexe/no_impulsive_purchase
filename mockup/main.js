const openBtn = document.getElementById("open-adder");
const closeBtn = document.getElementById("close-adder");
const popup = document.getElementById("adder");

// Function to open popup at a random position
openBtn.addEventListener("click", () => {
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;

    // Get random top and left position for the popup
    const randomTop = Math.floor(Math.random() * (windowHeight - 300)); // 300px is the height of the popup
    const randomLeft = Math.floor(Math.random() * (windowWidth - 300)); // 300px is the width of the popup

    // Apply random positions to the popup
    popup.style.top = `${randomTop}px`;
    popup.style.left = `${randomLeft}px`;

    // Show the popup
    popup.style.display = "block";
});

// Close the popup
closeBtn.addEventListener("click", () => {
    popup.style.display = "none";
});
