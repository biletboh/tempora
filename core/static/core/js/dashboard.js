$(function () {

	// change trash icon for ajax selects
	function prettifyKillicon() {
		var kill = $('.ui-icon.ui-icon-trash');
		kill.empty();
		kill.append('<i class="fa fa-lg fa-trash" aria-hidden="true"></i>');
		console.log(kill);
	};

	prettifyKillicon();
});
