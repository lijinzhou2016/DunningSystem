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


    //下拉列表设置默认值
    //$("select[name='status_select']").val($("select[name='status_select']").parent().find("input[name='status_value']").val());
    //有多个select标签，页面加载的时候即设置默认值，需要each实现循环设置
    $("select[name='status_select']").each(function(index, data){
        $(data).val($(data).parent().find("input[name='status_value']").val())
    })

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

    //更新页面中的用户基本信息
    function update_lender_basic(){
        var idcard = $("input[name='idcard']").val();
        var name = $("input[name='name']").val();
        var tel = $("input[name='tel']").val();
        var univers = $("input[name='univers']").val();
        var universarea = $("input[name='universarea']").val();
        var familyaddr = $("input[name='familyaddr']").val();
        var familyarea = $("input[name='familyarea']").val();
        var id = $("input[name='lender-id']").val();

        var send_url = "/orderdetail"
        var send_data = {"action":"update", "section": "lender", 
                        "idcard": idcard, "name": name, "tel": tel,
                        "univers": univers, "universarea":universarea, 
                        "familyaddr": familyaddr, "familyarea": familyarea,
                        "id": id};
        
        ajax_post(send_url, send_data, false);

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
        old_order_status = $(parentclass).find("select[name='status_select']").val();
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
        $(parentclass).find("select[name='status_select']").val(old_order_status);
    }


    //更新页面中的用户基本信息
    function update_order_basic(parentclass){
        var source = $(parentclass).find("input[name='source']").val();
        var dispid = $(parentclass).find("input[name='dispid']").val();
        var accountday = $(parentclass).find("input[name='accountday']").val();
        var product = $(parentclass).find("input[name='product']").val();
        var amount = $(parentclass).find("input[name='amount']").val();
        var monthpay = $(parentclass).find("input[name='monthpay']").val();
        var periods = $(parentclass).find("input[name='periods']").val();
        var paidperiods = $(parentclass).find("input[name='paidperiods']").val();
        var recvamount = $(parentclass).find("input[name='recvamount']").val();
        var orderdate = $(parentclass).find("input[name='orderdate']").val();
        var takeorderdate = $(parentclass).find("input[name='takeorderdate']").val();
        var status = $(parentclass).find("select[name='status_select']").val();
        var id = $(parentclass).find("input[name='order-id']").val();

        var send_url = "/orderdetail"
        var send_data = {"action":"update", "section": "orderbasic", 
                        "source": source, "dispid": dispid, "accountday": accountday,
                        "product": product, "amount":amount, "monthpay":monthpay, 
                        "periods": periods, "paidperiods": paidperiods,
                        "recvamount": recvamount, "orderdate": orderdate,
                        "takeorderdate": takeorderdate, "status": status,
                        "id": id};
        
        ajax_post(send_url, send_data, false);

        //更新title的标签
        

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

    //更新页面中的用户联系人信息
     function update_order_relatives(parentclass){
        var parent = $(parentclass).find("input[name='parent']").val();
        var parentcall = $(parentclass).find("input[name='parentcall']").val();
        var roommate = $(parentclass).find("input[name='roommate']").val();
        var roommatecall = $(parentclass).find("input[name='roommatecall']").val();
        var classmate = $(parentclass).find("input[name='classmate']").val();
        var classmatecall = $(parentclass).find("input[name='classmatecall']").val();
        var id = $(parentclass).find("input[name='order-id']").val();

        var send_url = "/orderdetail"
        var send_data = {"action":"update", "section": "relatives", 
                        "parent": parent, "parentcall": parentcall, 
                        "roommate": roommate, "roommatecall": roommatecall, 
                        "classmate":classmate, "classmatecall":classmatecall, 
                        "id": id};
        
        ajax_post(send_url, send_data, false);

    }


    //更新页面中的用户操作信息
     function update_operations(){
        var op_desc = $(".caozuo-line li:eq(0)").find(".caozuo-content").html();
        var admin_id = $("input[name='admin_id']").val();
        var lender_id = $("input[name='lender-id']").val();

        var send_url = "/orderdetail"
        var send_data = {"action":"update", "section": "operations", 
                        "opdesc": op_desc, "adminid": admin_id, 
                        "lenderid": lender_id, "id": ""};
        
        ajax_post(send_url, send_data, false);

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

    //基本信息
    $(".edit").click(function () {
        display_save_cancel_button(".jichuxinxi-btn", ".orderDetail-content-jichuxinxi-right")
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

        //保存信息到数据库
        update_lender_basic();
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
        //设置input下拉框可编辑
        $("select[name='status_select']").removeAttr("disabled");
        store_order_basic($(this).parent());
    })
    //订单状态取消按钮
    $(".orderStatusbtn-cancel").click(function () {
        btn_save_cancel($(this), $(this).parent().parent().find(".orderStatus-content-right"))
        //设置input下拉框不可编辑
        $("select[name='status_select']").attr("disabled","disabled");

        restore_order_basic($(this).parent().parent());
    })
    //订单状态保存按钮
    $(".orderStatusbtn-save").click(function () {
        btn_save_cancel($(this), $(this).parent().parent().find(".orderStatus-content-right"))
        //设置input下拉框不可编辑
        $("select[name='status_select']").attr("disabled","disabled");
         //保存信息到数据库
        update_order_basic($(this).parent().parent().parent());
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
        //保存最初的信息
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
        //恢复最初的信息
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

         //保存信息到数据库
        update_order_relatives($(this).parent().parent().parent());
    })

    //dingdanxinxi
    // $(".edit").click(function(){
    //     display_save_cancel_button(".jichuxinxi-btn")
    // })
    $(".caozuo-title-edit").click(function () {

        //获取当前时间
        var d = new Date();
        var admin_name = $("#admin_name").text();
        var li = "<li><div class='width:80%;float:left;position:relative;margin-left:10%;'>" +
            "<div class='caozuo-time'><span class='caozuo-time-time'>" 
            + Format(d,"yyyy-MM-dd HH:mm:ss") +"</span> <span class='caozuo-time-name'>" + admin_name + "</span></div>" +
            "<div class='caozuo-content on' readonly='true' contentEditable='true'>添加修改描述</div>" +
            "</div><div class='caouo-btn'><input type='button' value='保存' class='caozuo-savebtn' readonly/><input type='button' value='取消'/ class='caozuo-cancelbtn' readonly></div></li>";
        $(".caozuo-line").prepend(li);
        $(".caozuo-cancelbtn").click(function () {
            $(".caozuo-line li:eq(0)").remove();
        });
        $(".caozuo-savebtn").click(function(){
            update_operations();

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
            timeout: 60000,
            success: function (result) {
                if(result=='error'){
                    alert('操作失败')
                }
            },
            error: function(result){
                alert(result)
            }
        });
    }


    function Format(now,mask)
    {
        var d = now;
        var zeroize = function (value, length)
        {
            if (!length) length = 2;
            value = String(value);
            for (var i = 0, zeros = ''; i < (length - value.length); i++)
            {
                zeros += '0';
            }
            return zeros + value;
        };
     
        return mask.replace(/"[^"]*"|'[^']*'|\b(?:d{1,4}|m{1,4}|yy(?:yy)?|([hHMstT])\1?|[lLZ])\b/g, function ($0)
        {
            switch ($0)
            {
                case 'd': return d.getDate();
                case 'dd': return zeroize(d.getDate());
                case 'ddd': return ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat'][d.getDay()];
                case 'dddd': return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][d.getDay()];
                case 'M': return d.getMonth() + 1;
                case 'MM': return zeroize(d.getMonth() + 1);
                case 'MMM': return ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][d.getMonth()];
                case 'MMMM': return ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][d.getMonth()];
                case 'yy': return String(d.getFullYear()).substr(2);
                case 'yyyy': return d.getFullYear();
                case 'h': return d.getHours() % 12 || 12;
                case 'hh': return zeroize(d.getHours() % 12 || 12);
                case 'H': return d.getHours();
                case 'HH': return zeroize(d.getHours());
                case 'm': return d.getMinutes();
                case 'mm': return zeroize(d.getMinutes());
                case 's': return d.getSeconds();
                case 'ss': return zeroize(d.getSeconds());
                case 'l': return zeroize(d.getMilliseconds(), 3);
                case 'L': var m = d.getMilliseconds();
                    if (m > 99) m = Math.round(m / 10);
                    return zeroize(m);
                case 'tt': return d.getHours() < 12 ? 'am' : 'pm';
                case 'TT': return d.getHours() < 12 ? 'AM' : 'PM';
                case 'Z': return d.toUTCString().match(/[A-Z]+$/);
                // Return quoted strings with the surrounding quotes removed
                default: return $0.substr(1, $0.length - 2);
            }
        });
    };

})



