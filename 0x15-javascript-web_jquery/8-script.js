$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
for (let m in data.results) {
    $('UL#list_movies').append('<li>' + data.results[m].title + '</li>');
  }
});
