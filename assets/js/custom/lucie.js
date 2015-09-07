$(".cover-photo-button").click(
    function() {
        var parent = $(this).parent();

        if (parent.hasClass('extended')) {
            parent.animate({
                height: 250
            }, 1000, function() {
                parent.removeClass('extended');
            })
        } else {
            parent.animate({
                height: 500
            }, 1000, function() {
                parent.addClass('extended');
            })
        }
    }
);