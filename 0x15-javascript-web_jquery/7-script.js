// To fetch and replace the name of the API data then
// replace the name of the character in the DIV#character tag text

let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, function (data, stat) {
  $('div#character').text(data.name);
});
