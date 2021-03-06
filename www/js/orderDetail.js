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

    var orderStatusDict = { 0: '已结清', 1: '联系本人', 2: '联系亲属', 3: '联系同学', 4: '失联', 5: '待外访', 6: '外访中', 7: '承诺还款', 8: '部分还款' };
    //下拉列表设置默认值
    //$("select[name='status_select']").val($("select[name='status_select']").parent().find("input[name='status_value']").val());
    //有多个select标签，页面加载的时候即设置默认值，需要each实现循环设置
    $("select[name='status_select']").each(function (index, data) {
        $(data).val($(data).parent().find("input[name='status_value']").val())
    })

    $("select[name='accountday']").each(function (index, data) {
        $(data).val($(data).parent().find("input[name='accountday_value']").val())
    })

    $(".loadding").hide();

    $(".orderDetail-content-orderStatus").each(function (index, data) {
        total_debt(data)
    })


    //处理新建订单的情况，新建订单的时候lender-id和order-id都为空
    if ($("input[name='lender-id']").val() == "") {
        //如果为空，则订单处于编辑状态


        display_save_cancel_button(".jichuxinxi-btn", ".orderDetail-content-jichuxinxi-right")
        //编辑的时候获取一次页面信息，防止用户取消操作
        store_lender_basic();


        display_save_cancel_button(".orderStatus-btn", ".orderStatus-content-right")
        //设置input下拉框可编辑
        $("select[name='status_select']").removeAttr("disabled");
        $("select[name='accountday']").removeAttr("disabled");
        store_order_basic(".orderStatus-info");


        display_save_cancel_button(".orderStatus-lianxiren-btn",
            ".parentsname");
        display_save_cancel_button(".orderStatus-lianxiren-btn",
            ".parentsphone");
        display_save_cancel_button(".orderStatus-lianxiren-btn",
            ".sheyouname");
        display_save_cancel_button(".orderStatus-lianxiren-btn",
            ".sheyouphone");
        display_save_cancel_button(".orderStatus-lianxiren-btn",
            ".tongxuename");
        display_save_cancel_button(".orderStatus-lianxiren-btn",
            ".tongxuephone");
        //保存最初的信息
        store_lender_relatives(".orderStatus-lianxiren");
    }



    //保存页面中的用户基本信息
    function store_lender_basic() {
        old_lender_idcard = $("input[name='idcard']").val();
        old_lender_name = $("input[name='name']").val();
        old_lender_tel = $("input[name='tel']").val();
        old_lender_univers = $("input[name='univers']").val();
        old_lender_universarea = $("input[name='universarea']").val();
        old_lender_familyaddr = $("input[name='familyaddr']").val();
        old_lender_familyarea = $("input[name='familyarea']").val();
    }

    //恢复页面中的用户基本信息
    function restore_lender_basic() {
        $("input[name='idcard']").val(old_lender_idcard);
        $("input[name='name']").val(old_lender_name);
        $("input[name='tel']").val(old_lender_tel);
        $("input[name='univers']").val(old_lender_univers);
        $("input[name='universarea']").val(old_lender_universarea);
        $("input[name='familyaddr']").val(old_lender_familyaddr);
        $("input[name='familyarea']").val(old_lender_familyarea);
    }

    //回调函数用于更新lender-id
    function update_lender_basic_id(id) {
        $("input[name='lender-id']").val(id);


    }

    //更新页面中的用户基本信息
    function update_lender_basic() {
        var idcard = $("input[name='idcard']").val();
        var name = $("input[name='name']").val();
        var tel = $("input[name='tel']").val();
        var univers = $("input[name='univers']").val();
        var universarea = $("input[name='universarea']").val();
        var familyaddr = $("input[name='familyaddr']").val();
        var familyarea = $("input[name='familyarea']").val();
        var id = $("input[name='lender-id']").val();

        var send_url = "/orderdetail"
        var send_data = {
            "action": "update", "section": "lender",
            "idcard": idcard, "name": name, "tel": tel,
            "univers": univers, "universarea": universarea,
            "familyaddr": familyaddr, "familyarea": familyarea,
            "id": id
        };
        if (id == "") {
            id = ajax_post(send_url, send_data, false);
            if (id == "0") {
                alert("新增贷款人失败");
                return false
            }
            else {
                alert("新增贷款人成功");
                update_lender_basic_id(id);
                return true
            }
        }
        else {
            id = ajax_post(send_url, send_data, false);
            if (id == "0") {
                alert("更新贷款人信息失败");
                return false
            }
            else {
                alert("更新贷款人信息成功");
                return true
            }
        }

    }

    //保存页面中的订单信息
    function store_order_basic(parentclass) {
        old_order_source = $(parentclass).find("input[name='source']").val();
        old_order_dispid = $(parentclass).find("input[name='dispid']").val();
        old_order_accountday = $(parentclass).find("select[name='accountday']").val();
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
    function restore_order_basic(parentclass) {
        $(parentclass).find("input[name='source']").val(old_order_source);
        $(parentclass).find("input[name='dispid']").val(old_order_dispid);
        $(parentclass).find("select[name='accountday']").val(old_order_accountday);
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

    //回调函数用于更新order-id
    function update_order_basic_id(parentclass, id) {
        $(parentclass).find("input[name='order-id']").val(id);
    }

    //更新页面中的用户基本信息
    function update_order_basic(parentclass) {
        var source = $(parentclass).find("input[name='source']").val();
        var dispid = $(parentclass).find("input[name='dispid']").val();
        var accountday = $(parentclass).find("select[name='accountday']").val();
        var product = $(parentclass).find("input[name='product']").val();
        var amount = $(parentclass).find("input[name='amount']").val();
        var monthpay = $(parentclass).find("input[name='monthpay']").val();
        var periods = $(parentclass).find("input[name='periods']").val();
        var paidperiods = $(parentclass).find("input[name='paidperiods']").val();
        var recvamount = $(parentclass).find("input[name='recvamount']").val();
        var orderdate = $(parentclass).find("input[name='orderdate']").val();
        var takeorderdate = $(parentclass).find("input[name='takeorderdate']").val();
        var paymentday = $(parentclass).find("input[name='paymentday']").val();
        var status = $(parentclass).find("select[name='status_select']").val();
        var id = $(parentclass).find("input[name='order-id']").val();

        var lenderid = $("input[name='lender-id']").val()

        var send_url = "/orderdetail"
        var send_data = {
            "action": "update", "section": "orderbasic",
            "source": source, "dispid": dispid, "accountday": accountday,
            "product": product, "amount": amount, "monthpay": monthpay,
            "periods": periods, "paidperiods": paidperiods,
            "recvamount": recvamount, "orderdate": orderdate,
            "takeorderdate": takeorderdate, "paymentday": paymentday,"status": status,
            "id": id, "lenderid": lenderid
        };

        if (id == "") {
            id = ajax_post(send_url, send_data, false);
            if (id == "0") {
                alert("新增订单失败");
                return false
            }
            else {
                alert("新增订单成功");
                update_order_basic_id(parentclass, id);

                //更新title的标签
                $(parentclass).find(".orderStatus-title").children("span").text(orderStatusDict[status]);
                //更新逾期金额
                total_debt(parentclass);
                return true
            }
        }
        else {
            id = ajax_post(send_url, send_data, false);
            if (id == "0") {
                alert("更新订单失败");
                return false
            }
            else {
                alert("更新订单成功");
                //更新title的标签
                $(parentclass).find(".orderStatus-title").children("span").text(orderStatusDict[status]);
                //更新逾期金额
                total_debt(parentclass);
                return true
        }


    }}

    //保存页面中的订单的联系人信息
    function store_lender_relatives(parentclass) {
        old_order_parent = $(parentclass).find("input[name='parent']").val();
        old_order_parentcall = $(parentclass).find("input[name='parentcall']").val();
        old_order_roommate = $(parentclass).find("input[name='roommate']").val();
        old_order_roommatecall = $(parentclass).find("input[name='roommatecall']").val();
        old_order_classmate = $(parentclass).find("input[name='classmate']").val();
        old_order_classmatecall = $(parentclass).find("input[name='classmatecall']").val();
    }

    //保存页面中的订单的联系人信息
    function restore_lender_relatives(parentclass) {
        $(parentclass).find("input[name='parent']").val(old_order_parent);
        $(parentclass).find("input[name='parentcall']").val(old_order_parentcall);
        $(parentclass).find("input[name='roommate']").val(old_order_roommate);
        $(parentclass).find("input[name='roommatecall']").val(old_order_roommatecall);
        $(parentclass).find("input[name='classmate']").val(old_order_classmate);
        $(parentclass).find("input[name='classmatecall']").val(old_order_classmatecall);
    }

    //更新页面中的用户联系人信息
    function update_order_relatives(parentclass) {
        var parent = $(parentclass).find("input[name='parent']").val();
        var parentcall = $(parentclass).find("input[name='parentcall']").val();
        var roommate = $(parentclass).find("input[name='roommate']").val();
        var roommatecall = $(parentclass).find("input[name='roommatecall']").val();
        var classmate = $(parentclass).find("input[name='classmate']").val();
        var classmatecall = $(parentclass).find("input[name='classmatecall']").val();
        var id = $(parentclass).find("input[name='order-id']").val();

        var send_url = "/orderdetail"
        var send_data = {
            "action": "update", "section": "relatives",
            "parent": parent, "parentcall": parentcall,
            "roommate": roommate, "roommatecall": roommatecall,
            "classmate": classmate, "classmatecall": classmatecall,
            "id": id
        };

        if (id == "") {
            alert("必须先新增一个订单");
        }
        else {
            id = ajax_post(send_url, send_data, false);
            if(id == "0")
            {
                alert("更新订单联系人信息失败");
                return false
            }
            else{
                alert("更新订单联系人信息成功");
                return true
            }
        }
    }


    //更新页面中的用户操作信息
    function update_operations() {
        var op_desc = $(".caozuo-line li:eq(0)").find(".caozuo-content").html();
        var admin_id = $("input[name='admin_id']").val();
        var lender_id = $("input[name='lender-id']").val();

        var send_url = "/orderdetail"
        var send_data = {
            "action": "update", "section": "operations",
            "opdesc": op_desc, "adminid": admin_id,
            "lenderid": lender_id, "id": ""
        };

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

        var phone = $(".tel").val();
        var flag = phoneVal(phone) && IDnumber();
        if (flag == true) {

            //保存信息到数据库
            if(update_lender_basic()){
                btn_save_cancel(".btn-cancel", ".orderDetail-content-jichuxinxi-right");
            }
        }

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
        $("select[name='accountday']").removeAttr("disabled");
        store_order_basic($(this).parent());
    })
    //订单状态取消按钮
    $(".orderStatusbtn-cancel").click(function () {
        btn_save_cancel($(this), $(this).parent().parent().find(".orderStatus-content-right"))
        //设置input下拉框不可编辑
        $("select[name='status_select']").attr("disabled", "disabled");
        $("select[name='accountday']").removeAttr("disabled");

        restore_order_basic($(this).parent().parent());
    })
    //订单状态保存按钮
    $(".orderStatusbtn-save").click(function () {
        var periods = $(".periods").val();
        var paidperiods = $(".paidperiods").val();
        var fenqijine = $(".fenqijine").val();
        var monthpay = $(".monthpay").val()
        var alreadyamount = $(".alreadyamount").val()


        if (!phoneValnum(periods)){
            alert ('请检查期数的输入');
            return;
        }
        if (!phoneValnum(paidperiods)){
            alert ('请检查已还期数的输入')
            return
        }
        if (!check_float_or_empty(fenqijine)){
            alert ('请检查分期金额的输入')
            return
        }
        if (!check_float_or_empty(monthpay)){
            alert ('请检查月供的输入')
            return
        }
        if (!check_float_or_empty(alreadyamount)){
            alert('请检查已收金额的输入')
            return
        }
        

        //保存信息到数据库
        if(update_order_basic($(this).parent().parent().parent())){
            btn_save_cancel($(this), $(this).parent().parent().find(".orderStatus-content-right"))
            //设置input下拉框不可编辑
            $("select[name='status_select']").attr("disabled", "disabled");
            $("select[name='accountday']").attr("disabled", "disabled");
        }
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
        $(".caozuo-title-edit").show()

        //恢复最初的信息
        restore_lender_relatives($(this).parent().parent());

    })
    //联系人保存按钮
    $(".lianxirenbtn-save").click(function () {
        //保存信息到数据库
        if(update_order_relatives($(this).parent().parent().parent())){
            btn_save_cancel($(this), $(this).parent().parent().find(".parentsname"))
            btn_save_cancel($(this), $(this).parent().parent().find(".parentsphone"))
            btn_save_cancel($(this), $(this).parent().parent().find(".sheyouname"))
            btn_save_cancel($(this), $(this).parent().parent().find(".sheyouphone"))
            btn_save_cancel($(this), $(this).parent().parent().find(".tongxuename"))
            btn_save_cancel($(this), $(this).parent().parent().find(".tongxuephone"))
            $(".caozuo-title-edit").show()
        }
    })

    //dingdanxinxi
    // $(".edit").click(function(){
    //     display_save_cancel_button(".jichuxinxi-btn")
    // })
    $(".caozuo-title-edit").click(function () {
        $(this).hide();
        //获取当前时间
        var d = new Date();
        var admin_name = $("#admin_name").text();
        var li = "<li><div class='width:80%;float:left;position:relative;margin-left:10%;'>" +
            "<div class='caozuo-time'><span class='caozuo-time-time'>"
            + Format(d, "yyyy-MM-dd HH:mm:ss") + "</span> <span class='caozuo-time-name'>" + admin_name + "</span></div>" +
            "<div class='caozuo-content on' readonly='true' contentEditable='true'>添加修改描述</div>" +
            "</div><div class='caouo-btn'><input type='button' value='保存' class='caozuo-savebtn' readonly/><input type='button' value='取消'/ class='caozuo-cancelbtn' readonly></div></li>";
        $(".caozuo-line").prepend(li);
        $(".caozuo-cancelbtn").click(function () {
            $(".caozuo-line li:eq(0)").remove();
            $(".caozuo-title-edit").show()
        });
        $(".caozuo-savebtn").click(function () {
            update_operations();
            $(".caozuo-title-edit").show()

            $(this).parent().css("display", "none");
            $(this).parent().parent().find(".caozuo-content").removeClass("on");
            $(this).parent().parent().find(".caozuo-content").removeAttr("contentEditable");
        })
    });


    //校验待上传文件的后缀，不合格则提示用户
    function check_upload_file(type, ext) {
        //图片类型
        if (type == 1) {
            if (ext.toUpperCase() != 'JPG'
                && ext.toUpperCase() != 'JPEG'
                && ext.toUpperCase() != 'BMP'
                && ext.toUpperCase() != 'PNG'
                && ext.toUpperCase() != 'GIF') {
                alert("图片文件格式必须是jpg,jpeg,bmp,png和gif格式的一种，请检查后再上传!")
                return false
            }
            return true
        }
        else if (type == 2) {
            return true
        }
        else if (type == 3) {
            return true
        }
        alert("页面获取元素出错，上传失败，请重新刷新页面!")
        return false
    }

    //实现md5计算功能
    $(".uploadfile").change(function () {
        var log3 = $(this).parent().find("input[name='testmd5']")[0];
        var blobSlice = File.prototype.slice || File.prototype.mozSlice || File.prototype.webkitSlice,
            file = this.files[0],
            chunkSize = 2097152, // read in chunks of 2MB
            chunks = Math.ceil(file.size / chunkSize),
            currentChunk = 0,
            spark = new SparkMD5.ArrayBuffer(),
            frOnload = function (e) {
                //log3.innerHTML+="\nread chunk number "+parseInt(currentChunk+1)+" of "+chunks;
                spark.append(e.target.result); // append array buffer
                currentChunk++;
                if (currentChunk < chunks)
                    loadNext();
                else
                    //log3.innerHTML+="\nfinished loading :)\n\ncomputed hash:\n"+spark.end()+"\n\nyou can select another file now!\n";
                    log3.value = spark.end();
                //alert(spark.end())
            },
            frOnerror = function () {
                log3.value = "\noops, something went wrong.";
            };
        function loadNext() {
            var fileReader = new FileReader();
            fileReader.onload = frOnload;
            fileReader.onerror = frOnerror;
            var start = currentChunk * chunkSize,
                end = ((start + chunkSize) >= file.size) ? file.size : start + chunkSize;
            fileReader.readAsArrayBuffer(blobSlice.call(file, start, end));
        };
        //log3.style.display="inline-block";
        //log3.innerHTML="file name: "+file.name+" ("+file.size.toString().replace(/\B(?=(?:\d{3})+(?!\d))/g, ',')+" bytes)\n";
        loadNext();
    });


    //实现图片点击放大功能
    $(".orderStatus-image-thumb").click(function () {
        var largeImage = '<img src=' + $(this).attr("src") + '></img>'
        $("#largeImage")
            .html($(largeImage)
                .animate({ height: '100%', width: '100%' }, 500));
    });

    //ajax上传后即时显示图片
    function add_file_div(uploadbtn, id, type, md5, ext) {
        var name = md5 + "." + ext;
        src = "../orderdata/" + name + "?idx=" + Math.floor(id / 100) + "&id=" + id
        //图片
        if (type == 1) {
            var div = "<div class='orderStatus-upload-image-box'>"
                + "<image class='orderStatus-image-thumb' src='" + src + "' />"
                + "<a href='" + src + "' download = ''>下载</a>"
                + "</div>"
            $(uploadbtn).parents(".orderStatus-upload-image").find(".orderStatus-upload-image-list").prepend(div);
        }
        //合同
        else if (type == 2) {
            if (ext == 'doc' || ext == 'docx') {
                src_img = "../word_icon.jpg"
            }
            else if (ext == 'pdf') {
                src_img = "../pdf_icon.png"
            }
            else {
                src_img = "../unknow.jpg"
            }
            var div = "<div class='orderStatus-upload-contract-box'>"
                + "<image class='orderStatus-contract-thumb' src='" + src_img + "' />"
                + "<a href='" + src + "' download = ''>下载</a>"
                + "</div>"
            $(uploadbtn).parents(".orderStatus-upload-contract").find(".orderStatus-upload-contract-list").prepend(div);

        }
        //通话详单
        else if (type == 3) {
            if (ext == 'xls' || ext == 'xlsx') {
                src_img = "../excel_icon.jpg"
            }
            else {
                src_img = "../unknow.jpg"
            }

            var div = "<div class='orderStatus-upload-phonelist-box'>"
                + "<image class='orderStatus-phonelist-thumb' src='" + src_img + "' />"
                + "<a href='" + src + "' download = ''>下载</a>"
                + "</div>"
            $(uploadbtn).parents(".orderStatus-upload-phonelist").find(".orderStatus-upload-phonelist-list").prepend(div);

        }

    }

    $(".upload").click(function () {
        //this指针在AJAX中表示AJAX作用域，必须要在外面定义，用全局变量表示
        var uploadobj = $(this).parent().find('.upload');
        var loadingobj = $(this).parents("td").find('.loadding');
        var dataobj = $(this).parent().find("input[name='data']");
        var id = $(this).parents(".orderDetail-content-orderStatus").find("input[name='order-id']").val();
        var file = $(dataobj).val();
        var ext = file.slice(file.lastIndexOf(".") + 1).toLowerCase();
        var md5 = $(this).parent().find("input[name='testmd5']").val();
        var type = $(this).parent().find("input[name='type']").val();

        var formData = new FormData($(this).parent()[0]);
        //增加订单ID
        formData.append("orderid", id);
        //增加MD5
        formData.append("md5", md5);
        //增加文件类型
        formData.append("type", type);

        if (check_upload_file(type, ext) == false) {
            return
        }

        uploadobj.hide();
        loadingobj.show();
        $.ajax({
            url: '/uploadlenderfile',
            type: 'POST',
            data: formData,
            async: true,
            cache: false,
            contentType: false,
            processData: false,
            //this指针在AJAX中表示AJAX作用域，必须要在外面定义，用全局变量表示
            success: function (returndata) {
                loadingobj.hide()
                uploadobj.show()
                //dataobj.val("未选择任何文件")
                var dataObj = eval("(" + returndata + ")");
                alert(dataObj.desc);
                if (dataObj.result == 'success') {
                    add_file_div(uploadobj, id, type, md5, ext)
                }
            },
            error: function (returndata) {
                loadingobj.hide()
                uploadobj.show()
                var dataObj = eval("(" + returndata + ")");
                alert(dataObj.desc)
                //dataobj.val("未选择任何文件")
                alert(returndata)
            }
        });

    });

    function ajax_post(send_url, send_data, is_async) {
        var id = "0";   //需要新增的情况下，如果失败则为0
        $.ajax({
            type: 'post',
            url: send_url,
            data: send_data,
            async: is_async,
            timeout: 60000,
            success: function (result) {
                //alert(result);
                var dataObj = eval("(" + result + ")");
                //alert("result id = " + dataObj.id)            
                if (dataObj.result == 'error') {
                    alert('操作失败')
                }
                else if (dataObj.result == 'success') {
                    id = dataObj.id;
                }
            },
            error: function (result) {
                alert('与后台通信失败')
            }
        });

        return id;
    }

    function isLeapYear(year) {
        var cond1 = year % 4 == 0;  //条件1：年份必须要能被4整除
        var cond2 = year % 100 != 0;  //条件2：年份不能是整百数
        var cond3 = year % 400 ==0;  //条件3：年份是400的倍数
        //当条件1和条件2同时成立时，就肯定是闰年，所以条件1和条件2之间为“与”的关系。
        //如果条件1和条件2不能同时成立，但如果条件3能成立，则仍然是闰年。所以条件3与前2项为“或”的关系。
        //所以得出判断闰年的表达式：
        var cond = cond1 && cond2 || cond3;
        if(cond) {
            //alert(year + "是闰年");
            return true;
        } else {
            //alert(year + "不是闰年");
            return false;
        }
    }

    //计算金额
    function total_debt(basicObject) {
        var month_pay = $(basicObject).find("input[name='monthpay']").val();
        var periods = $(basicObject).find("input[name='periods']").val();
        var paid_periods = $(basicObject).find("input[name='paidperiods']").val();
        var amount = $(basicObject).find("input[name='paidperiods']").val();
        var payment_day = $(basicObject).find("input[name='paymentday']").val();
        //alert("periods "+periods+"\n"+"paid_periods "+paid_periods+"\n"+"payment_day "+payment_day+"\n"+"month_pay "+month_pay);
     
        if (periods == paid_periods){//期数已还完
            //设置相关标签
            $(basicObject).find("input[name='latefees']").val("0.0");
            $(basicObject).find("input[name='sumdebt']").val("0.0");   //保留2位小数
            return;
        }
        // payment_day_list = payment_day.split('-') //分割成字符串数组

        if(payment_day != "" && month_pay != "" && periods !="" && paid_periods !=""){

            var over_day_arr = new Array();// 每月逾期的天数
            var i=0;

            //获取首次账期日
            var paymentDate = new Date(payment_day);
            
            //计算开始逾期账单日
            // now.getMonth()获取的是索引！！！
            var now = new Date();
            var is_LeapYear = isLeapYear(now.getYear() + 1900)
            var today_date = new Date((now.getYear() + 1900) + '-' + (now.getMonth() + 1) + '-' + (now.getDate()));
            var exceedDate;
            
            // 计算出每月逾期的天数
            while(true){
                exceedDate = new Date(payment_day); //首次还款日期

                // exceedDate.getMonth() + parseInt(paid_periods)：开始逾期的月份
                // exceedDate.getMonth() + parseInt(paid_periods)+parseInt(i):从开始逾期的月份开始往后推，找出所有的逾期月份
                exceedDate.setMonth(exceedDate.getMonth() + parseInt(paid_periods)+parseInt(i));

                if(exceedDate.getMonth()==2 && paymentDate.getDate()>28 && exceedDate.getDate()!=paymentDate.getDate()){
                    //如果首次还款日期大于28，二月份还款日设置为最后一天
                    if (is_LeapYear){//闰年
                        exceedDate.setDate(29);
                        exceedDate.setMonth(exceedDate.getMonth()-1);
                    }
                    else{//平年
                        exceedDate.setDate(28);
                        exceedDate.setMonth(exceedDate.getMonth()-1);
                    }
                }
                
                if(exceedDate.getMonth()!=1 && exceedDate.getDate() != 31 && paymentDate.getDate() == 31){
                    //如果首次还款日期为31，小月份还款日设置为30
                    exceedDate.setDate(30);
                    exceedDate.setMonth(exceedDate.getMonth()-1);
                }
                
                //计算逾期天数
                var over_day = parseInt((today_date - exceedDate) / 3600 / 24 / 1000)+1;//计算毫秒差值换算成日差值
                // alert(exceedDate+"\n"+over_day)
                // alert(over_day)
                if (parseInt(paid_periods)+parseInt(i)==parseInt(periods)){
                    // 逾期月份的个数 + 已还期数 = 总期数
                    // 说明所有账期都逾期，所有逾期月份均以计算
                    break;
                }  
                if(over_day>0){
                    over_day_arr[i] = over_day; //加入逾期数组
                    i++;
                }
                else{// 该月账期为逾期
                    break;
                }
            }
            
            //滞纳金
            var late_fee;
            var total_late_fee=parseFloat(0.0);
            var j;
            if (i > 0) {
                for(j=0; j<i; j++){
                    if (over_day_arr[j] > 90) {
                        late_fee = (parseFloat(month_pay) * 0.26 / 30.0) * 90 + (parseFloat(month_pay) * 0.50 / 30.0) * (over_day_arr[j] - 90)
                    }
                    else {
                        late_fee = (parseFloat(month_pay) * 0.26 / 30.0) * over_day_arr[j]
                    }
                    total_late_fee = total_late_fee + late_fee;
                } 
            }
            else {
                total_late_fee = 0.0
            }

            //总欠款                   
            debt = parseFloat(month_pay) * (parseInt(periods) - parseFloat(paid_periods)) + total_late_fee
            
            //设置相关标签
            $(basicObject).find("input[name='latefees']").val(total_late_fee.toFixed(2))
            $(basicObject).find("input[name='sumdebt']").val(debt.toFixed(2))   //保留2位小数
        }
        //如果其中任意值为空，则计算值的框显示为空字符串
        else{
             //设置相关标签
            $(basicObject).find("input[name='latefees']").val("NULL")
            $(basicObject).find("input[name='sumdebt']").val("NULL")   //保留2位小数
        }
    }

    function Format(now, mask) {
        var d = now;
        var zeroize = function (value, length) {
            if (!length) length = 2;
            value = String(value);
            for (var i = 0, zeros = ''; i < (length - value.length); i++) {
                zeros += '0';
            }
            return zeros + value;
        };

        return mask.replace(/"[^"]*"|'[^']*'|\b(?:d{1,4}|m{1,4}|yy(?:yy)?|([hHMstT])\1?|[lLZ])\b/g, function ($0) {
            switch ($0) {
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


//验证手机号
function phoneVal(phone) {
    if (phone == "") {
        //alert("手机号不能为空！");
        return true;
    } else {
        if (phone && /^1[34578]\d{9}$/.test(phone)) {
            return true;
        } else {
            alert("请检查手机号的输入格式");
            return false;
        }
    }

}

//验证身份证
function IDnumber() {
    var pattern = /(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/;
    var IDnumber = $(".idcard").val();
    if (IDnumber == "") {
        alert("身份证号不能为空！");
        return false;
    } else {
        if (IDnumber && pattern.test(IDnumber)) {
            return true;

        } else {
            alert("请检查身份证的输入");
            return false;
        }
    }
}

//验证数字
function phoneValnum(number) {
    if (number == "") {
        number = 0;
        return true;
    } else {
        if (number && /^\d+$/.test(number)) {
            return true;
        } else {
            return false;
        }
    }

}

//验证小数
function check_float(number) {
    if (number && /^\d+[\.]?\d*$/.test(number)) {
        return true;
    } else {
        return false;
    }

}

//验证小数同时允许为空
function check_float_or_empty(number) {
    if (number=="" || /^\d+[\.]?\d*$/.test(number)) {
        return true;
    } else {
        return false;
    }

}


