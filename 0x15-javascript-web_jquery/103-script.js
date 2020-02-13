$(function () {
  $('#btn_translate').click(function () {
    const langua = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/', { lang: langua }, function (data) {
      $('#hello').text(data.hello);
    });
  });
  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      $('#btn_translate').click();
      return false;
    }
  });
});
