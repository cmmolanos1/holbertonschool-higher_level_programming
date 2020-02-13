$(function () {
  $('#btn_translate').click(function () {
    const langua = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/', { lang: langua }, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
