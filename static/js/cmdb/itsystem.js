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
                    url: '/cmdb/itsystem/delete/',
                    csrfmiddlewaretoken:"{% csrf_token %}",
                    data: {
                        "where": check_array,
                    },
                    success: function (data) {
                        swal({
                            title:'成功删除！',
                            text:'数据已经被删除',
                            type:'success',
                            confirmButtonText: 'OK！',
                            confirmButtonColor: '#374152',
                            timer:1000
                        }).then(function () {
                            window.location.reload();
                        });

                    },
                    error: function (data) {
                        swal({
                            title:'删除失败！',
                            text:data,
                            type:'error',
                            timer:1000
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
                timer:1000
            }

        )
    }
});


$('#import-form').click(function(){
    $.ajax({
        type: "POST",
        url: "/cmdb/itsystem/import/",
        csrfmiddlewaretoken:"{% csrf_token %}",
        processData:false,
        contentType:false,
        data: new FormData($(".import-form")[0]),
        success: function (data) {
            swal({
                text: '导入成功',
                confirmButtonColor: '#374152',
                timer:1000
            }).then(function () {
                window.location.reload();
            });
        },
        error: function (data) {
            swal({
                title:'导入失败！',
                type:'error',
                timer:1000
            })
            $('#myimportModal').modal('hide')
            $('#error-info').html(data['responseJSON']).show().delay(8000).fadeOut();
        }
    });
});

$('tbody tr').click(function (event) {
    if(  event.target.name !='checked') {
        var id = $(this).find('input').val()
        $.ajax({
            type: "GET",
            url: "/cmdb/itsystem/detail/"+ id +"/",
            success:function (result) {
                var detail_html =result['content_html']
                $('#myimportModal').after(detail_html)
            }
        })
    }
});

$('.slidebar-wrapper').live("click",function (event) {
    if (event.target.className == 'slidebar-wrapper'){
        $('.slidebar-wrapper').remove()
    }
});

$('.bk-tab2-head ul li').live("click",function () {
    $('.tab2-nav-item').removeClass('actived')
    $(this).addClass('actived')
    var num =$(this).index()
    console.log(num)
    $(".bk-tab2-content section").addClass('bk-tab2-pane').removeClass('active');
    $(".bk-tab2-content section").eq(num).removeClass('bk-tab2-pane').addClass('active');
});

// 属性界面点击【更多属性】弹出更多属性界面
$('.group-more-link').live("click",function () {
    if ($(this).children().is('.fa-angle-double-up')){
        $('#attr_more').show()
        $(this).children().removeClass('fa-angle-double-up').addClass('fa-angle-double-down')
    }
    else{
        $('#attr_more').hide()
        $(this).children().removeClass('fa-angle-double-down').addClass('fa-angle-double-up')
    }
})

// 属性编辑界面点击【取消】按钮触发弹出属性界面
$('.form-cancel').live("click",function () {
    $('.edit-list').removeClass('active').addClass('bk-tab2-pane')
    $('.attr-list').removeClass('bk-tab2-pane').addClass('active')
})

// 点击【属性编辑】界面触发弹出编辑界面
$('.attr-edit').live("click",function () {
    $('.edit-list').removeClass('bk-tab2-pane').addClass('active')
    $('.attr-list').removeClass('active').addClass('bk-tab2-pane')
})

//属性编辑界面点击【保存】按钮
$('.form-save').live("click",function () {
    $.ajax({
        type: "POST",
        url: "/cmdb/itsystem/edit/"+ id +"/",
        success:function (result) {
            var detail_html =result['content_html']
            $('#myimportModal').after(detail_html)
        }
    })
})