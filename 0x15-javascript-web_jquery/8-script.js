$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (result) {
      const movies = result.results;
      const movieList = $('ul#list_movies');

      for (let i = 0; i < movies.length; i++) {
        const title = movies[i].title;
        const listItem = $('<li>').text(title);
        movieList.append(listItem);
      }
    },
    error: function (error) {
      console.log('An error occurred: ' + error);
    }
  });
});
