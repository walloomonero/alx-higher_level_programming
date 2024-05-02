// To query an API and fetch all movie titles
// then insert them into the UL#list_movies tag

let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  let films = data.results;
  for (let film of films) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
