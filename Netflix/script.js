// Smooth scrolling for movie row
document.querySelectorAll('.movie-row').forEach(row => {
    row.addEventListener('wheel', (event) => {
        if (event.deltaY > 0) {
            row.scrollLeft += 300;
        } else {
            row.scrollLeft -= 300;
        }
    });
});
