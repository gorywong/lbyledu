$(function(){
    var imgBox = $('.main-slide-imgBox');
    var excerpt = $('.main-slide-excerpt');
    imgBox.flexslider({
        selector: ".main-slide-list > .main-slide-item",
        animation: "slide",
        slideshowSpeed: 6000,
        controlNav: false,
        prevText: '<div class="main-slide-btn main-slide-left"><span class="glyphicon glyphicon-chevron-left"></span></div>',
        nextText: '<div class="main-slide-btn main-slide-right"><span class="glyphicon glyphicon-chevron-right"></span></div>',
        before: function(slider, target){
            excerpt.flexslider(target);
        }
    });
    excerpt.flexslider({
        selector: ".main-slide-excerpt-list > .main-slide-excerpt-item",
        animation: "slide",
        slideshowSpeed: 6000,
        controlNav: false,
        directionNav: false,
        slideshow: false
    });
    excerpt.hover(function(){
        imgBox.flexslider("pause");
    },function(){
        imgBox.flexslider("play");
    });
    $('.panel-show-box').flexslider({
        selector: ".panel-show-list > .panel-show-item",
        animation: "slide",
        controlNav: false,
        slideshowSpeed: 3000
    });
    $('.panel-show-body').hover(function(){
        $(this).find('.panel-show-box').flexslider("pause");
    },function(){
        $(this).find('.panel-show-box').flexslider("play");
    });
    //IE10+ blur
    var ie_v = document.documentMode;
    var $blur_img = $(".main-slide-excerpt-item>img");
    if (ie_v == "10" || ie_v == "11" || navigator.userAgent.indexOf("Edge") != -1) {
        $blur_img.each(function(index, img) {
            var src = img.src;
            img.insertAdjacentHTML("afterend", '<svg><image xlink:href="'+ src +'" src="'+ src +'" width="620" height="360" y="0" x="0" filter="url(#blur)" /></svg>');
        });
    }else{
        $blur_img.removeClass("hidden");
    }
});