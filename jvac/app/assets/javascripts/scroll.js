(function($) {
    $(document).ready(function(){
        $(window).scroll(function(){
            if ($(this).scrollTop() > 200) {
                $('header').fadeIn(500);
           }
        });
    });
})(jQuery);
