function searchMovies(event) {
    key = event.keyCode

    if (key == 13) {
        searchString = event.target.value

        window.location.href="{% url 'landing_page:search_movies' %}?query=" + encodeURIComponent(searchString);
    }
}