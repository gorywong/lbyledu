//index.html
$(function(){
    //导航
    var $mainNav = $(".main-nav");
    $mainNav.on("click", ">li", function(){
        location.href = $(this).find(">a").attr("href");
        return false;
    });
    $mainNav.on("mouseenter", ">li", function(){
        if($(this).is('[data-toggle="tab"]')){
            $(".main-nav>li").removeClass("active show");
            $(".main-nav-more>li").removeClass("active show");
            $(this).tab('show');
            $(".main-nav-more").addClass("active");
        }else{
            $(".main-nav-more").removeClass("active");
        }
        $(".main-nav>li>a").removeClass("active");
        $(this).find(">a").addClass("active");
    });
    $(".main-header-navbar").mouseleave(function(){
        $(".main-nav>li").removeClass("active show");
        $(".main-nav>li>a").removeClass("active");
        $(".main-nav>li>a[name='active']").addClass("active");
        $(".main-nav-more").removeClass("active");
        $(".main-nav-more>li").removeClass("active show");
    });
    
    //字体大小
    $(".setting-font-size>.btn").click(function(){
        $(".setting-font-size>.btn").removeClass("active");
        $(this).addClass("active");
        var $content = $(".main-content-body");
        $content.removeClass("font-size-lg font-size-md");
        if(!!$(this).attr("name")){
            $content.addClass("font-size-" + $(this).attr("name"));
        }
    });
});

//content.html
$(function(){
    //左侧导航
    $('[data-toggle="offcanvas"]').click(function(){
        $('.row-offcanvas').toggleClass('active');
    });
    //左侧二级导航
    $(".main-content-sidebar .toggle").on("click", function(){
        $(this).find(".float-right").toggleClass("hidden");
        $(this).next(".child").toggleClass("hidden");
        $(this).next(".grand-child").toggleClass("hidden");
    });
    if ($(".main-content-sidebar .child .toggle").hasClass("active")) {
        $(".main-content-sidebar .child .toggle.active").next(".grand-child").removeClass("hidden");
        $(".main-content-sidebar .child .toggle.active").find(".fa-angle-down").removeClass("hidden");
        $(".main-content-sidebar .child .toggle.active").find(".fa-angle-right").addClass("hidden");
    };
    //老师自定义模块展开更多
    var people_nav_tabs = $(".content-people-body .nav-tabs");
    var one_line_btn = people_nav_tabs.find(".one-line-btn");
    if(people_nav_tabs.children().length > 8){
        one_line_btn.show().click(function(){
            people_nav_tabs.toggleClass("one-line");
            one_line_btn.find(".one-line-btn-down").toggle();
            one_line_btn.find(".one-line-btn-up").toggle();
        });
    }
});

//common
$(function(){
				
	//为当前窗口添加滚动条滚动事件（适用于所有可滚动的元素和 window 对象（浏览器窗口））
	$(window).scroll(function(){
		 //创建一个变量存储当前窗口下移的高度
		var scroTop = $(window).scrollTop();
		//判断当前窗口滚动高度
		//如果大于100，则显示顶部元素，否则隐藏顶部元素
		if(scroTop>=0){
			$('.returntop').fadeIn(500);
		}else{
			$('.returntop').fadeOut(500);
		}
    });
		    	
	//为返回顶部元素添加点击事件
	$('.returntop').click(function(){
		//将当前窗口的内容区滚动高度改为0，即顶部
		$("html,body").animate({scrollTop:0},"fast");
    });
    
    var $contactus = $('.contactus')
    $contactus.on("mouseenter", ">a", function(){
        $('.contactus-card').css({
            'opacity': '1',
            '-webkit-transform': 'scale(1)',
            '-ms-transform': 'scale(1)',
            'transform': 'scale(1)'
          })
    });
    $contactus.on("mouseleave", function(){
        $('.contactus-card').css({
            'opacity': '0',
            '-webkit-transform': 'scale(0.01)',
            '-ms-transform': 'scale(0.01)',
            'transform': 'scale(0.01)'
          })
    });

    var $caption = $(".content-page p");
    $caption.each(function(){
        if ($(this).css("text-align") == "center") {
            $(this).addClass("caption");
        }
      });
});

// article_index.html
$(function(){
    $page_numbers = $(".page-item");

    function GetQueryString(name) {
     var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
     var r = window.location.search.substr(1).match(reg);
     if(r!=null)return  unescape(r[2]); return null;
    }

    if (window.location.pathname.search("category")) {
        var $page = parseInt(GetQueryString("page"));

        if ($page) {
            $.each($page_numbers, function(i, val) {
                if (parseInt(val.textContent) == $page) {
                    val.className += " active";
                    console.log(val.className);
                }
            });
        } else {
            $page_numbers[2].className += " active";
        }
    }
});