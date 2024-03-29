function searchMovies(event) {
    // Enter key
    if (event.key === "Enter" && event.target.value.trim()) {
        searchString = event.target.value.trim()
        console.log(searchString)

        fetch("search/movies?query=" + encodeURIComponent(searchString))
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            console.log("Request successful");
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    }
}