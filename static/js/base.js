

$(document).ready(function () {
    //左边菜单栏页面跳转JS
    $('.menu-list ul li a').each(function () {
        $this = $(this);
        if (window.location.href.indexOf($this[0].href) == 0) {
            $('.active').removeClass('active');
            $('.nav-active').removeClass('nav-active');
            $(this).parent().addClass('active');
            $(this).parents().addClass('nav-active');
        }
    });
});

$(function () {
    $("#check_all").click(function () {
        $("input[name='checked']").prop("checked", $(this).prop("checked"));
    });
});

$('tbody tr').click(function (event) {
    if(  event.target.name !='checked') {
        $('.slidebar-wrapper').removeClass('hidden')
    }
});

$('.slidebar-wrapper').click(function (event) {
    if (event.target.className == 'slidebar-wrapper'){
        $('.slidebar-wrapper').addClass('hidden')
    }
});

$('.bk-tab2-head ul li').click(function () {
    $('.tab2-nav-item').removeClass('actived')
    $(this).addClass('actived')
    var num =$(this).index()
    $(".bk-tab2-content section").addClass('bk-tab2-pane').removeClass('active');
    $(".bk-tab2-content section").eq(num).removeClass('bk-tab2-pane').addClass('active');
});


//点击非主体部分触发关闭明细界面
$('.slidebar-wrapper').live("click", function (event) {
    if (event.target.className == 'slidebar-wrapper') {
        $('.slidebar-wrapper').remove()
    }
});

//点击明细tab触发切换界面
$('.bk-tab2-head ul li').live("click", function () {
    $('.tab2-nav-item').removeClass('actived')
    $(this).addClass('actived')
    var num = $(this).index()
    $(".bk-tab2-content section").addClass('bk-tab2-pane').removeClass('active');
    $(".bk-tab2-content section").eq(num).removeClass('bk-tab2-pane').addClass('active');
});

// 属性界面点击【更多属性】弹出更多属性界面
$('.group-more-link').live("click", function () {
    if ($(this).children().is('.fa-angle-double-up')) {
        $('#attr_more').show()
        $(this).children().removeClass('fa-angle-double-up').addClass('fa-angle-double-down')
    }
    else {
        $('#attr_more').hide()
        $(this).children().removeClass('fa-angle-double-down').addClass('fa-angle-double-up')
    }
})

// 属性编辑界面点击【取消】按钮触发弹出属性界面
$('.form-cancel').live("click", function () {
    $('.edit-list').removeClass('active').addClass('bk-tab2-pane')
    $('.attr-list').removeClass('bk-tab2-pane').addClass('active')
})


// 点击【属性编辑】界面触发弹出编辑界面
$('.attr-edit').live("click", function () {
    $('.edit-list').removeClass('bk-tab2-pane').addClass('active')
    $('.attr-list').removeClass('active').addClass('bk-tab2-pane')
})