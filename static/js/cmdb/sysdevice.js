var url_params = {}
//点击【删除按钮】触发JS
$('#del').click(function () {
    var check_array = [];
    $(".gradeX input:checked").each(function () {
        check_array.push($(this).attr("value"))
    });
    if (check_array.length) {
        swal({
            title: '确定删除吗？',
            text: '你将无法恢复它！',
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#374152',
            cancelButtonColor: '#d33',
            confirmButtonText: '确定删除！',
        }).then(function (isConfirm) {
            if (isConfirm.value === true) {
                $.ajax({
                    type: 'POST',
                    url: '/cmdb/sysdevice/delete/',
                    csrfmiddlewaretoken: "{% csrf_token %}",
                    data: {
                        "where": check_array,
                    },
                    success: function (data) {
                        swal({
                            title: '成功删除！',
                            text: '数据已经被删除',
                            type: 'success',
                            confirmButtonText: 'OK！',
                            confirmButtonColor: '#374152',
                            timer: 1000
                        }).then(function () {
                            window.location.reload();
                        });

                    },
                    error: function (data) {
                        swal({
                            title: '删除失败！',
                            text: data,
                            type: 'error',
                            timer: 1000
                        });
                        $('#error-info').html(data['responseJSON'][0]).show().delay(8000).fadeOut();
                    },
                });
            }
            else {
                swal.close;
            }
        })
    }
    else {
        swal({
                text: '请选择要删除的数据',
                confirmButtonColor: '#374152',
                timer: 1000
            }
        )
    }
});

//点击【导入】按钮触发JS
$('#import-form').click(function () {
    $.ajax({
        type: "POST",
        url: "/cmdb/sysdevice/import/",
        processData: false,
        contentType: false,
        data: new FormData($(".import-form")[0]),
        success: function (data) {
            swal({
                text: '导入成功',
                confirmButtonColor: '#374152',
                timer: 1000
            }).then(function () {
                window.location.reload();
            });
        },
        error: function (data) {
            swal({
                title: '导入失败！',
                type: 'error',
                timer: 1000
            })
            $('#myimportModal').modal('hide')
            $('#error-info').html(data['responseJSON']).show().delay(8000).fadeOut();
        }
    });
});

//点击【数据行】触发弹出明细界面
$('tbody tr').live("click", function (event) {
    if (event.target.name != 'checked') {
        var id = $(this).find('input').val()
        $.ajax({
            type: "GET",
            url: "/cmdb/sysdevice/detail/" + id + "/",
            success: function (result) {
                var detail_html = result['content_html']
                $('#myimportModal').after(detail_html)
                var left_width = $('.left-side').css('width')
                $('.slidebar-wrapper').css("left", left_width).removeClass('hidden')
            }
        })
    }
});

//属性编辑界面点击【保存】按钮
$('.form-save').live("click", function () {
    var id = $(this).val()
    var form_dict = get_form_data()
    var error_info = $('.error-ip-input').val()
    if (error_info) {
        $('#edit-error').html('请填写正确的数据！').show().delay(8000).fadeOut();
    }
    else {
        $.ajax({
            type: "POST",
            url: "/cmdb/sysdevice/update/" + id + "/",
            data: {'result': JSON.stringify(form_dict)},
            success: function () {
                $('.slidebar-wrapper').remove()
                $.ajax({
                    type: "GET",
                    url: "/cmdb/sysdevice/detail/" + id + "/",
                    success: function (result) {
                        var detail_html = result['content_html']
                        $('#myimportModal').after(detail_html)
                        var left_width = $('.left-side').css('width')
                        $('.slidebar-wrapper').css("left", left_width).removeClass('hidden')
                    }
                })
            },
            error: function (result) {
                $('#edit-error').html(result['responseJSON']).show().delay(8000).fadeOut();
            }
        })
    }
})


//搜索选择框触发js
$('.select_form').change(function () {
    var column_value = $(this).val()
    var column_name = $(this).attr('title')
    var filter_params = {}
    filter_params[column_name] = column_value
    if (column_value == 'all') {
        url_params['where'] = {}
    }
    else {
        url_params['where'] = JSON.stringify(filter_params)
    }
    $.ajax({
        type: "POST",
        url: "/cmdb/sysdevice/search/",
        data: url_params,
        success: function (result) {
            load_table_data(result['result'], result['content_html'])
        }
    })
})

//动态搜索框输入查询
$('.set-select2').bind('input propertychange', function () {
    var column_value = $(this).val()
    var column_name = $(this).attr('title')
    var filter_params = {}
    filter_params[column_name + '__icontains'] = column_value
    url_params['where'] = JSON.stringify(filter_params)
    $.ajax({
        type: "POST",
        url: "/cmdb/sysdevice/search/",
        data: url_params,
        success: function (result) {
            load_table_data(result['result'], result['content_html'])
        }
    })
});

//动态更新table函数
function load_table_data(data, page) {
    //替换table部分
    var html = "";
    for (var i = 0; i < data.length; i++) {
        html += "<tbody> "
        html += "<tr class=\"gradeX\">"
        html += "<td class=\"text-center\">"
        html += '<input type="checkbox" name="checked" value="' + data[i].id + '">'
        html += "</td>"
        html += "<td>" + data[i].related_itsystem_id_id + "</td>"
        html += "<td>" + data[i].related_zone_id_id + "</td>"
        html += "<td>" + data[i].label_cn + "</td>"
        html += "<td>" + data[i].ipaddr + "</td>"
        html += "<td>" + data[i].assets_type + "</td>"
        html += "<td>" + data[i].system + "</td>"
        html += "</tr> "
        html += "</tbody> "
    }
    $("table tbody").remove()
    $("table thead").after(html)
    $('#paginate_page').remove()
    $("table").after(page)
}

//分页点击切换
$(".page").live("click", function () {
    var current_page = $(this).attr('title')
    var previous_page = $(".page-active").attr('title')
    if (current_page == 'next') {
        current_page = Number(previous_page) + 1
    }
    else if (current_page == 'previous') {
        current_page = Number(previous_page) - 1
    }
    url_params['current_page'] = current_page
    $.ajax({
        type: "POST",
        url: "/cmdb/sysdevice/search/",
        data: url_params,
        success: function (result) {
            load_table_data(result['result'], result['content_html'])
            delete url_params['current_page']
        }
    })
})