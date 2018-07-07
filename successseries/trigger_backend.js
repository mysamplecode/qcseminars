jQuery(document).ready(function() {

    $("body").delegate('.first_image', 'click', function() {
        var player = $(this).parent().find('#audio_player');
        $(".second_image").each(function() {
            if ($(this).is(":visible"))
            {
                $(this).hide();
                $(this).prev().show();
            }
            var player2 = $(this).parent().find('#audio_player');
            player2.trigger('pause');
        });
        $(this).hide();
        $(this).next().show();
        player.trigger('play');
    });
    $("body").delegate(".second_image", 'click', function() {
        var player = $(this).parent().find('#audio_player');
        $(this).hide();
        $(this).prev().show();
        player.trigger('pause');
    });
});

