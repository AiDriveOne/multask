web iOS android tablet and mobile


// Get all the result elements
const results = document.querySelectorAll('.results');

// Add a click event listener to each result element
results.forEach(result => {
    result.addEventListener('click', () => {
        // Toggle the active class when the element is clicked
        result.classList.toggle('active');
    });
});
