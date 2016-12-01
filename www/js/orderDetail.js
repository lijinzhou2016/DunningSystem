$(document).ready(function () {

    //保存原有的lender信息
    var old_lender_idcard;
    var old_lender_name;
    var old_lender_tel;
    var old_lender_univers;
    var old_lender_universarea;
    var old_lender_familyaddr;
    var old_lender_familyarea;

    //订单个数
    //var order_num = $(".orderDetail-content-orderStatus").length;
    //保存原有的订单信息
    /*
    var old_order_source      = new Array(order_num);
    var old_order_dispid      = new Array(order_num);
    var old_order_accountday  = new Array(order_num);
    var old_order_product     = new Array(order_num);
    var old_order_amount      = new Array(order_num);
    var old_order_monthpay    = new Array(order_num);
    var old_order_periods     = new Array(order_num);
    var old_order_paidperiods = new Array(order_num);
    var old_order_recvamount  = new Array(order_num);
    var old_order_orderdate   = new Array(order_num);
    var old_order_takeorderdate   = new Array(order_num);
    var old_order_calldetails = new Array(order_num);
    var old_order_contract    = new Array(order_num);
    var old_order_parent      = new Array(order_num);
    var old_order_parentcall  = new Array(order_num);
    var old_order_roommate    = new Array(order_num);
    var old_order_roommatecall = new Array(order_num);
    var old_order_classmate   = new Array(order_num);
    var old_order_classmatecall = new Array(order_num);
    var old_order_status      = new Array(order_num);
    */
    //获取多个订单的值
     //$("input[name='source']").each(function(index, data){
      //   old_order_source[index] = $(data).val()
     //}) 

    var old_order_source;
    var old_order_dispid;
    var old_order_accountday;
    var old_order_product;
    var old_order_amount;
    var old_order_monthpay;
    var old_order_periods;
    var old_order_paidperiods;
    var old_order_recvamount;
    var old_order_orderdate;
    var old_order_takeorderdate;
    var old_order_calldetails;
    var old_order_contract;
    var old_order_parent;
    var old_order_parentcall;
    var old_order_roommate;
    var old_order_roommatecall;
    var old_order_classmate;
    var old_order_classmatecall;
    var old_order_status;

    //保存页面中的用户基本信息
    function store_lender_basic(){
        old_lender_idcard = $("input[name='idcard']").val();
        old_lender_name = $("input[name='name']").val();
        old_lender_tel = $("input[name='tel']").val();
        old_lender_univers = $("input[name='univers']").val();
        old_lender_universarea = $("input[name='universarea']").val();
        old_lender_familyaddr = $("input[name='familyaddr']").val();
        old_lender_familyarea = $("input[name='familyarea']").val();
    }

    //恢复页面中的用户基本信息
    function restore_lender_basic(){
        $("input[name='idcard']").val(old_lender_idcard);
        $("input[name='name']").val(old_lender_name);
        $("input[name='tel']").val(old_lender_tel);
        $("input[name='univers']").val(old_lender_univers);
        $("input[name='universarea']").val(old_lender_universarea);
        $("input[name='familyaddr']").val(old_lender_familyaddr);
        $("input[name='familyarea']").val(old_lender_familyarea);
    }

    //保存页面中的订单信息
    function store_order_basic(parentclass){
        old_order_source = $(parentclass).find("input[name='source']").val();
        old_order_dispid = $(parentclass).find("input[name='dispid']").val();
        old_order_accountday = $(parentclass).find("input[name='accountday']").val();
        old_order_product = $(parentclass).find("input[name='product']").val();
        old_order_amount = $(parentclass).find("input[name='amount']").val();
        old_order_monthpay = $(parentclass).find("input[name='monthpay']").val();
        old_order_periods = $(parentclass).find("input[name='periods']").val();
        old_order_paidperiods = $(parentclass).find("input[name='paidperiods']").val();
        old_order_recvamount = $(parentclass).find("input[name='recvamount']").val();
        old_order_orderdate = $(parentclass).find("input[name='orderdate']").val();
        old_order_takeorderdate = $(parentclass).find("input[name='takeorderdate']").val();
        old_order_calldetails = $(parentclass).find("input[name='call_details']").val();
        old_order_contract = $(parentclass).find("input[name='contract']").val();
        old_order_status = $(parentclass).find("input[name='status']").val();
    }

    //恢复页面中的订单信息
    function restore_order_basic(parentclass){
        $(parentclass).find("input[name='source']").val(old_order_source);
        $(parentclass).find("input[name='dispid']").val(old_order_dispid);
        $(parentclass).find("input[name='accountday']").val(old_order_accountday);
        $(parentclass).find("input[name='product']").val(old_order_product);
        $(parentclass).find("input[name='amount']").val(old_order_amount);
        $(parentclass).find("input[name='monthpay']").val(old_order_monthpay);
        $(parentclass).find("input[name='periods']").val(old_order_periods);
        $(parentclass).find("input[name='paidperiods']").val(old_order_paidperiods);
        $(parentclass).find("input[name='recvamount']").val(old_order_recvamount);
        $(parentclass).find("input[name='orderdate']").val(old_order_orderdate);
        $(parentclass).find("input[name='takeorderdate']").val(old_order_takeorderdate);
        $(parentclass).find("input[name='call_details']").val(old_order_calldetails);
        $(parentclass).find("input[name='contract']").val(old_order_contract);
        $(parentclass).find("input[name='status']").val(old_order_status);
    }

    //保存页面中的订单的联系人信息
    function store_lender_relatives(parentclass){
        old_order_parent = $(parentclass).find("input[name='parent']").val();
        old_order_parentcall = $(parentclass).find("input[name='parentcall']").val();
        old_order_roommate = $(parentclass).find("input[name='roommate']").val();
        old_order_roommatecall = $(parentclass).find("input[name='roommatecall']").val();
        old_order_classmate = $(parentclass).find("input[name='classmate']").val();
        old_order_classmatecall = $(parentclass).find("input[name='classmatecall']").val();
    }

    //保存页面中的订单的联系人信息
    function restore_lender_relatives(parentclass){
        $(parentclass).find("input[name='parent']").val(old_order_parent);
        $(parentclass).find("input[name='parentcall']").val(old_order_parentcall);
        $(parentclass).find("input[name='roommate']").val(old_order_roommate);
        $(parentclass).find("input[name='roommatecall']").val(old_order_roommatecall);
        $(parentclass).find("input[name='classmate']").val(old_order_classmate);
        $(parentclass).find("input[name='classmatecall']").val(old_order_classmatecall);
    }

    $(".orderDetail-content-jichuxinxi").hover(function () {
        if ($(".jichuxinxi-btn").css("display") == "none") {
            $(this).find(".edit").css("display", "block");
        }
    }, function () {
        $(this).find(".edit").css("display", "none");
    })

    //按下编辑的效果
    function display_save_cancel_button(mclass, obj) {
        $(mclass).css("display", "block");
        $(obj).removeAttr("readonly");
        $(obj).css("border", "1px solid #f1f1f1");
    }

    //按下保存或者取消按键的效果
    function btn_save_cancel(btnclass, inputclass) {
        $(btnclass).parent().css("display", "none");
        $(inputclass).attr("readonly", "readonly");
        $(inputclass).css("border", "none");
    }

    
    function click_save_cancel_btn(btnclass, inputclass) {
        $(btnclass).parent().css("display", "none");
        $(inputclass).attr("readonly", "readonly");
        $(inputclass).css("border", "none");
    }

    //按下编辑的效果
    function show_save_cancel_btn(btnparentobj, inputclass){
        $(btnparentobj).css("display", "block");
        $(textobj).removeAttr("readonly");
        $(textobj).css("border", "1px solid #f1f1f1");
    }

    //基本信息
    $(".edit").click(function () {
        display_save_cancel_button(".jichuxinxi-btn", ".orderDetail-content-jichuxinxi-right")
        //$(this).parent().parent().find(".orderDetail-content-jichuxinxi-right").css("border", "1px solid #f1f1f1");
        //编辑的时候获取一次页面信息，防止用户取消操作
        store_lender_basic();

    })
    //基础信息取消按钮
    $(".btn-cancel").click(function () {
        btn_save_cancel(".btn-cancel", ".orderDetail-content-jichuxinxi-right");
        //恢复最初的信息
        restore_lender_basic();
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
        display_save_cancel_button($(this).parent().find(".orderStatus-btn"), 
                    $(this).parent().find(".orderStatus-content-right"))
        store_order_basic($(this).parent());
    })
    //订单状态取消按钮
    $(".orderStatusbtn-cancel").click(function () {
        //btn_save_cancel(".orderStatusbtn-cancel", ".orderStatus-content-right");
        btn_save_cancel($(this), $(this).parent().parent().find(".orderStatus-content-right"))
        restore_order_basic($(this).parent().parent());
    })
    //订单状态保存按钮
    $(".orderStatusbtn-save").click(function () {
        //btn_save_cancel(".orderStatusbtn-save", ".orderStatus-content-right");
        btn_save_cancel($(this), $(this).parent().parent().find(".orderStatus-content-right"))
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
        display_save_cancel_button($(this).parent().find(".orderStatus-lianxiren-btn"), 
                            $(this).parent().find(".parentsname"));
        display_save_cancel_button($(this).parent().find(".orderStatus-lianxiren-btn"), 
                            $(this).parent().find(".parentsphone"));
        display_save_cancel_button($(this).parent().find(".orderStatus-lianxiren-btn"), 
                            $(this).parent().find(".sheyouname"));
        display_save_cancel_button($(this).parent().find(".orderStatus-lianxiren-btn"), 
                            $(this).parent().find(".sheyouphone"));
        display_save_cancel_button($(this).parent().find(".orderStatus-lianxiren-btn"), 
                            $(this).parent().find(".tongxuename"));
        display_save_cancel_button($(this).parent().find(".orderStatus-lianxiren-btn"), 
                            $(this).parent().find(".tongxuephone"));
        
        store_lender_relatives($(this).parent());
    
    })
    //联系人取消按钮
    $(".lianxirenbtn-cancel").click(function () {
        btn_save_cancel($(this), $(this).parent().parent().find(".parentsname"))
        btn_save_cancel($(this), $(this).parent().parent().find(".parentsphone"))
        btn_save_cancel($(this), $(this).parent().parent().find(".sheyouname"))
        btn_save_cancel($(this), $(this).parent().parent().find(".sheyouphone"))
        btn_save_cancel($(this), $(this).parent().parent().find(".tongxuename"))
        btn_save_cancel($(this), $(this).parent().parent().find(".tongxuephone"))
        
        restore_lender_relatives($(this).parent().parent());

    })
    //联系人保存按钮
    $(".lianxirenbtn-save").click(function () {
        btn_save_cancel($(this), $(this).parent().parent().find(".parentsname"))
        btn_save_cancel($(this), $(this).parent().parent().find(".parentsphone"))
        btn_save_cancel($(this), $(this).parent().parent().find(".sheyouname"))
        btn_save_cancel($(this), $(this).parent().parent().find(".sheyouphone"))
        btn_save_cancel($(this), $(this).parent().parent().find(".tongxuename"))
        btn_save_cancel($(this), $(this).parent().parent().find(".tongxuephone"))
    })

    //dingdanxinxi
    // $(".edit").click(function(){
    //     display_save_cancel_button(".jichuxinxi-btn")
    // })
    $(".caozuo-title-edit").click(function () {
        var li = "<li><div class='width:80%;float:left;position:relative;margin-left:10%;'>" +
            "<div class='caozuo-time'><span class='caozuo-time-time'>2016-11-06</span> <span class='caozuo-time-name'>张三</span></div>" +
            "<div class='caozuo-content on' readonly='true' contentEditable='true'>添加修改描述</div>" +
            "</div><div class='caouo-btn'><input type='button' value='保存' class='caozuo-savebtn' readonly/><input type='button' value='取消'/ class='caozuo-cancelbtn' readonly></div></li>";
        $(".caozuo-line").prepend(li);
        $(".caozuo-cancelbtn").click(function () {
            $(".caozuo-line li:eq(0)").remove();
        });
        $(".caozuo-savebtn").click(function(){
            $(this).parent().css("display","none");
            $(this).parent().parent().find(".caozuo-content").removeClass("on");
            $(this).parent().parent().find(".caozuo-content").removeAttr("contentEditable");
        })
    });



    function ajax_post(send_url, send_data, is_async) {
        $.ajax({
            type: 'post',
            url: send_url,
            data: send_data,
            async: is_async,
            timeout: 30000,
            success: function (result) {
                if (result['state'] == "success") {
                    return true;
                }
                else {
                    alert("【操作失败】 " + result)
                    return false;
                }
            }
        });
    }


})