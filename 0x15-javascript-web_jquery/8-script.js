$.get('https://swapi.co/api/films/?format=json', function (data, status) {
  for (let movie of data.results) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  }
});
