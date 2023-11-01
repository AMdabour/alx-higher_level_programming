$(function ()
{
    $('INPUT#btn_translate').click(function () {
        const language_code = $('INPUT#language_code').val();
        const api_url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=${language_code}';
        $.getJSON(api_url, function (data) {
            $('DIV#hello').text(data.hello);
        });
    });
});
