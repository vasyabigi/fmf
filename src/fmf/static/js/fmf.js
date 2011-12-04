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
          
        }
    }
})($);


$(document).ready(function(){
    Fmf.init();
    Fmf.NewsSlider();
    Fmf.IndexTabs();
});