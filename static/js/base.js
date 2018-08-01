$(document).ready(function () {
    $('.menu-list ul li a').each(function () {
        $this = $(this);
        if (window.location.href.indexOf($this[0].href) == 0) {
            $('.active').removeClass('active');
            $('.nav-active').removeClass('nav-active');
            $(this).parent().addClass('active');
            $(this).parents().addClass('nav-active');

        }
    });
    $('.page').each(function () {
        $this = $(this);
        if (window.location.href.indexOf($this[0].href) == 0) {
            $(this).parent().addClass('active');

        }
    });
    $('#error-info').hide();

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

