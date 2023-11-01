$(function () {
	$("INPUT#btn_translate").click(fetchTranslation);
	$("INPUT#language_code").keydown(function (event) {
		if (event.which === 13) {
			fetchTranslation();
		}
	});

	function fetchTranslation() {
		const language_code = $("INPUT#language_code").val();
		$.get(
			`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`,
			function (data) {
				$("DIV#hello").text(data.hello);
			}
		);
	}
});
