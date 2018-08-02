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


$('.group-more-link').click(function () {
    if ($(this).children().is('.fa-angle-double-up')){
        $('#group_display').parent().css('display','block');
        $(this).children().removeClass('fa-angle-double-up').addClass('fa-angle-double-down')
    }
    else{
        $('#group_display').parent().css('display','none');
        $(this).children().removeClass('fa-angle-double-down').addClass('fa-angle-double-up')
    }

})