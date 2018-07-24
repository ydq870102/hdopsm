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
});

$(function () {
    $("#check_all").click(function () {
        $("input[name='checked']").prop("checked", $(this).prop("checked"));
    });
});

