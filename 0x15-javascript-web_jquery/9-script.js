let code = $('html').attr('lang');
$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=' + code,
  success: (results) => {
    $('DIV#hello').text(results.hello);
  }
});
