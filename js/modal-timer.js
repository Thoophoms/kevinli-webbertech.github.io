document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("modal"); // Finds the modal in the HTML
    const closeModalBtn = document.getElementById("close-modal"); // Finds the "Close" button

    // Show the modal after 15 seconds
    setTimeout(() => {
        modal.classList.remove("hidden"); // Removes the 'hidden' class to show the modal
    }, 15000); // 15000 milliseconds = 15 seconds

    // Close the modal when the button is clicked
    closeModalBtn.addEventListener("click", () => {
        modal.classList.add("hidden"); // Adds the 'hidden' class to hide the modal again
    });
});
