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

        NewsSlider : function(){
            var sudoSlider = $("#slider").sudoSlider({
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
                },
                afterAniFunc: function(t){
                    $(this).children('.caption').slideDown(200);
                }
            });

            $(".prevBtn, .nextBtn, #slider").hover(
                function () {
                    // Mouse in
                    $(".prevBtn, .nextBtn").stop().fadeTo(200, 1);
                },
                function () {
                    //Mouse out
                    $(".prevBtn, .nextBtn").stop().fadeTo(200, 0);
                }
            );

            $(".prevBtn, .nextBtn").stop().fadeTo(0, 0);
            $('#slider_box').mouseenter(function() {
                auto = sudoSlider.getValue('autoAnimation');
                sudoSlider.stopAuto();
            });
            $('#slider_box').mouseleave(function() {
                sudoSlider.startAuto();
            });
        }, //End of NewsSlider

        IndexTabs : function(){
            $("#tab_content li").hide();
            $("#"+$("#tab_nav li a.active").attr("title")).show();

            $("#tab_nav li a").click(function() {
                if ($(this).hasClass('active')) {
                    return false;
                }
                $("#tab_nav li a.active").removeClass("active");
                $(this).addClass("active");
                $("#tab_content > li").hide();
                $("#"+$(this).attr("title")).fadeIn();
                return false;
            });
        },

        TabsWidth : function(){

        },

        NewsDetailsSldier: function(){
            $("#news_detail_images").sudoSlider({
                autowidth:false,
                slideCount:5,
                continuous: true,
                speed: '300'
            });

            $(".fancybox").fancybox({
                nextEffect: 'fade',
                prevEffect: 'fade',
                nextSpeed: 'slow',
                prevSpeed: 'slow'
            });
        }
    }
})($);


$(document).ready(function(){
    Fmf.init();
    Fmf.NewsSlider();
    Fmf.IndexTabs();
//    Fmf.TabsWidth();
    Fmf.NewsDetailsSldier();

});
	$(window).scroll(function() {
		if($(this).scrollTop() > 300) {
			$('.toTop').fadeIn();
		} else {
			$('.toTop').fadeOut();
		}
	});

	$('.toTop').click(function() {
		$('body,html').animate({scrollTop:0},1000);
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
