

$(document).ready(function(){

	$('#player').youTubeEmbed("http://www.youtube.com/watch?v=6_u4yxYJAD8")
				.youTubeEmbed('http://www.youtube.com/watch?v=uDBn6DOrNTs');

	$('form').submit(function(){
		$('#player').youTubeEmbed($('#url').val());
		$('#url').val('');
		return false;
	});

});

$(document).ready(function(){

	$('#player2').youTubeEmbed("http://www.youtube.com/watch?v=WndRNcBDaxw")
				.youTubeEmbed('http://www.youtube.com/watch?v=ZbWUKscgKYQ');

	$('form').submit(function(){
		$('#player2').youTubeEmbed($('#url').val());
		$('#url').val('');
		return false;
	});

});