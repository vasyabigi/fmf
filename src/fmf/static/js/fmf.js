$(document).ready(function(){

/*  SLIDER  */

    var auto = true;
    var autostopped = false;
    var sudoSlider = $("#slider").sudoSlider({
     fade:true,
     numeric:true,
     auto:true,
     continuous: true,
     fadespeed: '1000',
     speed:'3000',
     resumePause:'5000'/*,
     beforeAniFunc: function(){
     var sliderPos = $("#slider").offset().top;
     var scrolledDown = $(window).scrollTop();
      if (sliderPos < scrolledDown)
       {
          $('html,body').animate({scrollTop: sliderPos}, 800);
       }
     }*/
  });
    $(".prevBtn, .nextBtn, #slider").hover(
    function () {
      // Mousein
      $(".prevBtn, .nextBtn").stop().fadeTo(200, 1);
    },
    function () {
      //Mouse out
      $(".prevBtn, .nextBtn").stop().fadeTo(200, 0);
    }
    );
    $(".prevBtn, .nextBtn").stop().fadeTo(0, 0);
    $('#slider_box') .mouseenter(function() {
      auto = sudoSlider.getValue('autoAnimation');
      sudoSlider.stopAuto();
   }).mouseleave(function() {
         sudoSlider.startAuto();
   });

/*  TABS  */
  

	$(function() {
		$("#accordion" ).accordion({
			collapsible: true
		});
	});

});