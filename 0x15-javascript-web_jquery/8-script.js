$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      const movieTitle = data.results;
      const listElem = $('#list_movies');
      $.each(movieTitle, function (index, movie) {
        listElem.append('<Li>' + movie.title + '<Li>');
      });
    },
    error: function () {
      $('#list_movies').text('Error fetching movie titles');
    }
  });
});
