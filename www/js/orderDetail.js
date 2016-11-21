$(document).ready(function () {
    $(".orderDetail-content-jichuxinxi").hover(function () {
        if ($(".jichuxinxi-btn").css("display") == "none") {
            $(this).find(".edit").css("display", "block");
        }
    }, function () {
        $(this).find(".edit").css("display", "none");
    })



    function display_save_cancel_button(mclass, obj) {
        $(mclass).css("display", "block");
        $(obj).removeAttr("readonly");
        $(obj).css("border", "1px solid #f1f1f1");
    }

    function btn_save_cancel(btnclass, inputclass) {
        $(btnclass).parent().css("display", "none");
        $(inputclass).attr("readonly", "readonly");
        $(inputclass).css("border", "none");

    }

    //基本信息
    $(".edit").click(function () {
        display_save_cancel_button(".jichuxinxi-btn", ".orderDetail-content-jichuxinxi-right")

    })
    //基础信息取消按钮
    $(".btn-cancel").click(function () {
        btn_save_cancel(".btn-cancel", ".orderDetail-content-jichuxinxi-right");
    })
    //基础信息保存按钮
    $(".btn-save").click(function () {
        btn_save_cancel(".btn-cancel", ".orderDetail-content-jichuxinxi-right");
    })

    $(".orderStatus-info").hover(function () {
        if ($(".orderStatus-btn").css("display") == "none") {
            $(this).find(".status-edit").css("display", "block");
        }
    }, function () {
        $(this).find(".status-edit").css("display", "none");
    })
    //订单状态
    $(".status-edit").click(function () {
        display_save_cancel_button(".orderStatus-btn", ".orderStatus-content-right")

    })
    //订单状态取消按钮
    $(".orderStatusbtn-cancel").click(function () {
        btn_save_cancel(".orderStatusbtn-cancel", ".orderStatus-content-right");
    })
    //订单状态保存按钮
    $(".orderStatusbtn-save").click(function () {
        btn_save_cancel(".orderStatusbtn-save", ".orderStatus-content-right");
    })

    //联系人

    $(".orderStatus-lianxiren").hover(function () {
        if ($(".orderStatus-lianxiren-btn").css("display") == "none") {
            $(this).find(".orderStatus-lianxiren-edit").css("display", "block");
        }
    }, function () {
        $(this).find(".orderStatus-lianxiren-edit").css("display", "none");
    })
    //联系人
    $(".orderStatus-lianxiren-edit").click(function () {
        display_save_cancel_button(".orderStatus-lianxiren-btn", ".parentsname");
        display_save_cancel_button(".orderStatus-lianxiren-btn", ".parentsphone");
        display_save_cancel_button(".orderStatus-lianxiren-btn", ".sheyouname");
        display_save_cancel_button(".orderStatus-lianxiren-btn", ".sheyouphone");
        display_save_cancel_button(".orderStatus-lianxiren-btn", ".tongxuename");
        display_save_cancel_button(".orderStatus-lianxiren-btn", ".tongxuephone");

    })
    //联系人取消按钮
    $(".lianxirenbtn-cancel").click(function () {
        btn_save_cancel(".lianxirenbtn-cancel", ".parentsname");
        btn_save_cancel(".lianxirenbtn-cancel", ".parentsphone");
        btn_save_cancel(".lianxirenbtn-cancel", ".sheyouname");
        btn_save_cancel(".lianxirenbtn-cancel", ".sheyouphone");
        btn_save_cancel(".lianxirenbtn-cancel", ".tongxuename");
        btn_save_cancel(".lianxirenbtn-cancel", ".tongxuephone");
    })
    //联系人保存按钮
    $(".lianxirenbtn-save").click(function () {
        btn_save_cancel(".lianxirenbtn-save", ".parentsname");
        btn_save_cancel(".lianxirenbtn-cancel", ".parentsphone");
        btn_save_cancel(".lianxirenbtn-cancel", ".sheyouname");
        btn_save_cancel(".lianxirenbtn-cancel", ".sheyouphone");
        btn_save_cancel(".lianxirenbtn-cancel", ".tongxuename");
        btn_save_cancel(".lianxirenbtn-cancel", ".tongxuephone");
        $(".caozuo-title-edit").css("display","block");
    })

    //dingdanxinxi
    // $(".edit").click(function(){
    //     display_save_cancel_button(".jichuxinxi-btn")
    // })
    $(".caozuo-title-edit").click(function () {
        $(".caozuo-title-edit").css("display","none");
        var li = "<li><div class='width:80%;float:left;position:relative;margin-left:10%;'>" +
            "<div class='caozuo-time'><span class='caozuo-time-time'>2016-11-06</span> <span class='caozuo-time-name'>张三</span></div>" +
            "<div class='caozuo-content on' readonly='true' contentEditable='true'>添加修改描述</div>" +
            "</div><div class='caouo-btn'><input type='button' value='保存' class='caozuo-savebtn' readonly/><input type='button' value='取消'/ class='caozuo-cancelbtn' readonly></div></li>";
        $(".caozuo-line").prepend(li);
        $(".caozuo-cancelbtn").click(function () {
            $(".caozuo-line li:eq(0)").remove();
             $(".caozuo-title-edit").css("display","block");
        });
        $(".caozuo-savebtn").click(function(){
            $(this).parent().css("display","none");
            $(this).parent().parent().find(".caozuo-content").removeClass("on");
            $(this).parent().parent().find(".caozuo-content").removeAttr("contentEditable");
             $(".caozuo-title-edit").css("display","block");
        })
    });


})