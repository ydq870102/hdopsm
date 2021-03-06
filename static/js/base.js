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


//table 勾选所有框
$(function () {
    $("#check_all").click(function () {
        $("input[name='checked']").prop("checked", $(this).prop("checked"));
    });
});

//点击非主体部分触发关闭明细界面
$('.slidebar-wrapper').live("click", function (event) {
    if (event.target.className == 'slidebar-wrapper') {
        $('.slidebar-wrapper').remove()
    }
});

//查询条件点击更多，弹出多余查询条件
$('.filter-more').click(function () {
    console.log($(this).find('i'))
    if ($(this).find('i').is('.fa-angle-double-right')){
        $(this).find('i').removeClass('fa-angle-double-right').addClass('fa-angle-double-down')
        $(this).siblings('#clear-more').show()
    }
    else {
        $(this).find('i').removeClass('fa-angle-double-down').addClass('fa-angle-double-right')
        $(this).siblings('#clear-more').hide()
    }

})


// 属性界面点击【更多属性】弹出更多属性界面
$('.group-more-link').live("click", function () {
    if ($(this).children().is('.fa-angle-double-up')) {
        $('.attr_more').each(function () {
            $(this).show()
        })
        $(this).children().removeClass('fa-angle-double-up').addClass('fa-angle-double-down')
    }
    else {
        $('.attr_more').each(function () {
            $(this).hide()
        })
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

// 日期选择样式
$('.datetimepicker').live('focus', function () {
    $(this).datetimepicker({
        format: 'yyyy-mm-dd hh:ii:ss',  //格式  如果只有yyyy-mm-dd那就是0000-00-00
        autoclose: true,//选择后是否自动关闭
        minView: 0,//最精准的时间选择为日期  0-分 1-时 2-日 3-月
        language: 'zh-CN', //中文
        todayBtn: true,  //在底部是否显示今天
        initialDate: new Date()
    });
})

//获取form数据，返回字段函数
function get_form_data() {
    var result = {}
    $('.attribute-item-field').each(function () {
        var form_attr = $(this).attr('title')
        var form_value = $(this).children().val()
        result[form_attr] = form_value
    })
    return result
}

// IP地址合法监测
$(".ip-input").live('blur', function () {
    var ip = $(this).val()
    var exp = /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/;
    var reg = ip.match(exp);
    if (reg == null) {
        $(this).addClass('error-ip-input')
    }
    else {
        $(this).removeClass('error-ip-input')
    }
})

//关联明细中点击展开按钮
$(".list-icon").live("click", function () {
    $(this).removeClass('fa-caret-right')
    $(this).addClass('fa-caret-down')
    $(this).removeClass('list-icon')
    $(this).addClass('open-icon')
    $(this).parent().siblings("ul").show()
})

//关联明细中点击收缩按钮
$(".open-icon").live("click", function () {
    $(this).removeClass('fa-caret-down')
    $(this).addClass('fa-caret-right')
    $(this).removeClass('open-icon')
    $(this).addClass('list-icon')
    $(this).parent().siblings("ul").hide()
})

//鼠标移入变色
// $(".relevance-box ul li").live("mouseover", function () {
//     console.log($(this))
//     $(this).css("background-color","#e8ffff")
//
// })
// 鼠标移出变色
// $(".relevance-box ul li").live("mouseout", function () {
//     console.log($(this))
//     $(this).css("background-color","#ffffff")
//
// })
