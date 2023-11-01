$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      $('').text(data.hello);
    },
    error: function () {
      $('#hello').text('Error fetching translation');
    }
  });
});
