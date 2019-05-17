$.get('https://swapi.co/api/people/5/?format=json', function (data, status) {
  $('#character').append(data.name);
});
