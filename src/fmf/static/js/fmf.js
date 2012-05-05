var Fmf = (function(){
    return {
        init : function(){
            $('a.selected').click(function(){
                return false;
            });

            $('a[href=#]').click(function(){
                return false;
            })
        },

        IndexSlider : function(){
            if ($("#slider").length) {
                var oldt = 0;
                var sudoSlider = $("#slider").sudoSlider({
                    customLink: '.custom',
                    fade:true,
                    numeric:true,
                    auto:true,
                    continuous: true,
                    fadespeed: '1000',
                    speed:'4000',
                    resumePause:'5000',
                    updateBefore: true,
                    beforeAniFunc: function(t){
                        $(this).children('.caption').hide();

                        var scroll = -t+3;
                        if (scroll > -1) scroll = 0;
                        if (scroll < -6) scroll = -6;
                        var scroll = scroll * $('.custom').eq(0).outerWidth(true);

                        var diff = Math.sqrt(Math.abs(oldt-t));
                        var speed = parseInt(diff*800);

                        $('.customBox').animate(
                                { marginLeft: scroll },
                                {
                                    queue:true,
                                    duration:speed
                                }
                        );
                        oldt = t;
                    },
                    afterAniFunc: function(t){
                        $(this).children('.caption').slideDown(200);
                    }
                });

                $("#slider_box").hover(
                    function () {
                        // Mouse in
                        $("#slider_box .prevBtn, #slider_box .nextBtn").stop().fadeTo(200, 1);
                    },
                    function () {
                        //Mouse out
                        $("#slider_box .prevBtn, #slider_box .nextBtn").stop().fadeTo(200, 0);
                    }
                );

                $("#slider_box .prevBtn, #slider_box .nextBtn").stop().fadeTo(0, 0);
                $('#slider_box').mouseenter(function() {
                    auto = sudoSlider.getValue('autoAnimation');
                    sudoSlider.stopAuto();
                });
                $('#slider_box').mouseleave(function() {
                    sudoSlider.startAuto();
                });
            }
        }, //End of NewsSlider

        EntrantsSlider : function(){
            if ($("#entrants_images").length) {
                var oldt = 0;
                var sudoSlider = $("#entrants_images").sudoSlider({
                    customLink: '.custom',
                    fade:true,
                    continuous: true,
                    fadespeed: '1000',
                    speed:'4000',
                    resumePause:'5000',
                    updateBefore: true,
                    beforeAniFunc: function(t){
                        var scroll = -t+2;
                        if (scroll == 1) scroll = 0;
                        if (scroll < -2) scroll = -2;
                        var scroll = scroll * $('.custom').eq(0).outerWidth(true);

                        var diff = Math.sqrt(Math.abs(oldt-t));
                        var speed = parseInt(diff*800);

                        $('.customBox').animate(
                                { marginLeft: scroll },
                                {
                                    queue:true,
                                    duration:speed
                                }
                        );
                        oldt = t;
                    }
                });
            }
        },

        NewsDetailsSldier: function(){
            if ($("#news_detail_images").length) {
                $("#news_detail_images").sudoSlider({
                    autowidth:false,
                    slideCount:5,
                    speed: '300'
                });

                if ($(".fancybox").length > 0)
                    $(".fancybox").fancybox({
                        nextEffect: 'fade',
                        prevEffect: 'fade',
                        nextSpeed: 'slow',
                        prevSpeed: 'slow'
                    });
            }
        },

        StreamerSlider: function(){
            if ($(".streamer_slider").length) {
                $(".streamer_slider").sudoSlider({
                    vertical:true,
                    slideCount:3,
                    autowidth:false,
                    autoheight:false,
                    speed: 400
                });
            }
        },

        ContactForm: function(){
            var form = $('#contact');
            if (form.length) {
                form.validationEngine({'scroll':false});
                form.find('input[type=submit]').click(function(event){
                    event.preventDefault();
                    if (form.validationEngine('validate'))
                        $.ajax(form.attr('action'), {
                            type: 'post',
                            data: form.serialize(),
                            dataType: 'json',
                            success: function(data){
                                form.replaceWith(data.content);
                            }
                        });
                });

                form.ajaxStart(function() {
                    form.html('<div id="loading"><img src="/static/images/loading-big.gif" alt="loading"></div>');
                })
            }
        },

        Scroll: function(){
            $(window).scroll(function() {
                var scrollTop = $(this).scrollTop();
                var scrollBottom = $(document).height() - $(window).height() - scrollTop;
                var header_height = $('header').outerHeight() + $('nav').outerHeight();

                /*ToTop_button*/
                if(scrollTop > 300) {
                    $('.toTop').fadeIn();
                } else {
                    $('.toTop').fadeOut();
                }
                /*ToTop_button fixing*/
                if(scrollBottom < 100) {
                    $('.toTop').addClass('toTop_fixed');
                } else {
                    $('.toTop').removeClass('toTop_fixed');
                }
                /*Sidebar fixing*/
                if (scrollTop > 180) {
                    $('.left_sidebar').addClass('fixed_sidebar');
                } else {
                    $('.left_sidebar').removeClass('fixed_sidebar');
                }
            });

            $('.toTop').click(function() {
                $('body,html').animate({scrollTop:0},'slow');
            });
        },

        TextNav: function(){
            $(window).scroll(function(arr) {
                var scrollTop = $(this).scrollTop();
                var val = $('a[name]').length;

                for (i=1; i<=val; i++) {

                    if (scrollTop > $('a[name='+i+']').offset().top-1 && scrollTop < $('a[name='+(i+1)+']').offset().top-1 && scrollTop < $('a[name='+val+']').offset().top+300) {
                        $(".side_nav > ul ul > li > a").removeClass('selected');
                        $("a#"+i).addClass('selected');
                    }
                    else if (scrollTop < $('a[name=1]').offset().top-1 || scrollTop > $('a[name='+(val)+']').offset().top+300) {
                        $(".side_nav > ul ul > li > a").removeClass('selected');
                    }
                }
            });

            $(".side_nav > ul ul > li > a").click(function() {
                $('html,body').stop().animate({scrollTop: $('a[name='+$(this).attr("id")+']').offset().top},'slow');
            });
        },

        LazyLoad: function(){
            $("img").lazyload({
                effect : "fadeIn"
            });
        },
        IndexFeedbackSlider: function() {
            $('#feedback-image-main').html($(".feedback li:first").find('.feedback-image').html());
            $('#feedback-description-main').html($(".feedback li:first").find('.feedback-description').html());

            $(".feedback li").click(function(){
              if (!$(this).hasClass('active')) {
                  $(".feedback li").removeClass('active');
                  $(this).addClass('active');
                  var feedbackImage = $(this).find('.feedback-image').html();
                  var feedbackDescription = $(this).find('.feedback-description').html();
                  $('#feedback-image-main').html(feedbackImage).hide().fadeIn();
                  $('#feedback-description-main').html(feedbackDescription).hide().fadeIn();
              }
            });

            function startFeedbackInterval() {
                timerFeedback = setInterval(function(){
                    var activeSlide = $(".feedback li.active");
                    if (activeSlide.next().length) {
                      activeSlide.next().trigger('click');
                    } else {
                      $(".feedback li:first").trigger('click');
                    }
                }, 5000);
            }
            startFeedbackInterval();

            $(".feedback li, .feedback-main").hover(function(){
                clearInterval(timerFeedback);
            }, function(){
                startFeedbackInterval();
            });
        }
    };
})($);


$(document).ready(function(){
    Fmf.init();
    Fmf.IndexSlider();
    Fmf.EntrantsSlider();
    Fmf.NewsDetailsSldier();
    Fmf.ContactForm();
    Fmf.Scroll();
    Fmf.TextNav();
    Fmf.StreamerSlider();
    Fmf.LazyLoad();
    Fmf.IndexFeedbackSlider();
});



(function($) {

	$.fn.konami = function(options) {

		var opts = $.extend({}, $.fn.konami.defaults, options);
		return this.each(function() {

			var masterKey = [38,38,40,40,37,39,37,39,66,65];
			var controllerCode = [];
			$(window).keyup(function(evt) {

				var code = evt.keyCode ? evt.keyCode : evt.which;
				controllerCode.push(code);
				if(controllerCode.length === 10) {

					var bIsValid = true;
					for(var i = 0, l = masterKey.length; i < l; i++) {
						if(masterKey[i] !== controllerCode[i]) {
							bIsValid = false;
						} // end if
					} // end for

					if(bIsValid) {
						opts.cheat();
					} // end if

					controllerCode = [];

				} // end if

			}); // keyup

		}); // each

	}; // opts

	$.fn.konami.defaults = {
		cheat: null
	};

})(jQuery);

$(function() {
	$(window).konami({
		cheat: function() {
			$('.page_info > div > span').html('&#1057;&#1072;&#1084;&#1080;&#1081;&#32;&#1054;&#1061;&#1059;&#1028;&#1053;&#1053;&#1048;&#1049;&#32;&#1089;&#1072;&#1081;&#1090;&#33;&#33;&#33;&#32;');
		}
	});
});
