
// Buttons for the movie page's 
// context change depending on button clicked, testing visuals
function movieOverview(){
    document.getElementById("movie_summary").innerHTML = 
    `Description of <b>Dark Knight</b> Movie: Movie Summary/Plot
    `;
}
function movieDetails(){
    document.getElementById("movie_summary").innerHTML = 
    `<div>Director(s):
    </div>
    <div> 
    Writer(s):
    </div>
    <div>
    Star(s):
    </div>
    <div>
    Genre(s):
    </div>
    `;
}
// movie available to watch 
function movieWatching(){
    document.getElementById("movie_summary").innerHTML = 
    `<div>Streaming: 
    </div>
    <div>Buy: 
    </div>
    <div>Rent: 
    </div>
    `;
}
function movieOptions(){
    document.getElementById("movie_summary").innerHTML = 
    `<div>
    Movie Comment(s): 
    </div>
    <div>
    Movie Rating(s):
    </div>
    `;
}