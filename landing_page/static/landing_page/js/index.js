function searchMovies(event) {
    searchString = event.target.value.trim()
    // Enter key
    if (event.key === "Enter" && searchString) {
        // Route to search movies
        window.location.href = window.location.origin + "/search/movies?query=" + encodeURIComponent(searchString)
    } else if (event.key !== "Backspace" && searchString) {
        fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ search: searchString })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.error("Fetch error:", error);
        });
    }
}