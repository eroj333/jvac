$(document).ready(function(){
  $('.menu').click(function(e){
      e.stopPropagation();
        $('nav').toggleClass('active');
  });
});
