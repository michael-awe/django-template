function searchMovies(event) {
    // Enter key
    if (event.key === "Enter" && event.target.value.trim()) {
        searchString = event.target.value.trim()
        
        // Route to search movies
        window.location.href = window.location.origin + "/search/movies?query=" + encodeURIComponent(searchString)
    }
}