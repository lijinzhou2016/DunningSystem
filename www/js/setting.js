$(document).ready(function () {
    //保存数据库所有用户id，初始化网页时会被赋值
    var user_ids = new Array();
    user_ids[0] = 1;
    //新增用户id，刷新网页或提交新增用户后为空
    var new_user_ids = new Array();
    //要删除的用户id
    var delete_user_id;

    //保存的网盘账号信息，用户取消设置后，用户恢复数据
    var oldwangpanzhanghao;
    var oldwangpanmima;
    var selectchecked;
    var oldtimetext;

    oldwangpanzhanghao = $(".wangpanzhanghao").val();
    oldwangpanmima = $(".wangpanmima").val();
    selectchecked = $("#timeselect").val(); //备份时间索引，取消设置后，用此数据恢复
    oldtimetext = $("#timeselect").find("option:selected").text(); //备份时间，提交保存时用此数据

    //点击后，网盘设置处于可编辑状态
    $(".edit").click(function () {
        $(".wangpan-btn").css("display", "block");
        $(this).css("display", "none");
        $(".wangpan-content").find("input").removeAttr("readonly");
        $(".wangpan-content").find("input").css("border","1px solid #f1f1f1")
        $("#timeselect").removeAttr("disabled");

    })

    function delete_user(obj) {
        alert('begin delete')
        $(this).parent().parent().remove();
    }

    //取消本次网盘编辑
    $(".wangpanbtn-cancel").click(function () {
        if (is_sure("确定放弃修改？")) {
            //alert('fangqixiugai')
            $(".wangpan-content").find("input").attr("readonly", true);
            $(".wangpan-content").find("input").css("border","none");
            $(".wangpan-btn").css("display", "none");
            $(".edit").css("display", "block");
            $(".wangpanzhanghao").val(oldwangpanzhanghao);
            $(".wangpanmima").val(oldwangpanmima);
            // $("#timeselect").find("option[text='selectchecked']").attr("selected",true);
            $("#timeselect").val(selectchecked);
            $("#timeselect").attr("disabled", true);
            //alert($("#timeselect").find("option:selected").text())
        }

    })

    //管理员设置 添加按钮
    $(".add").click(function () {
        var i = 2;
        var j = 0;
        var flag = 0

        //给新用户分配一个id（数据库中没有被占用且较小的数字）
        for (i = 2; i < 100; i++) {
            for (j = 0; j < user_ids.length; j++) {
                if (i == user_ids[j]) {
                    break;
                }
                else if (j == (user_ids.length - 1)) {
                    user_ids[user_ids.length] = i; //添加到所有用户id数组
                    new_user_ids[new_user_ids.length] = i; //添加到新增用户id数组，用于提交
                    flag = 1;
                    break;
                }
            }
            if (flag) {
                break;
            }
        }

        //添加一条编辑栏
        var cls_account = 'account_' + i;
        var cls_passwd = 'passwd_' + i;
        var cls_name = 'name_' + i;
        var newList = "<tr><td><input class=" + cls_account + " type='text' placeholder='请输入账号'></td>" +
            "<td><input class=" + cls_passwd + " type='text' placeholder='请输入密码'></td>" +
            "<td><input class=" + cls_name + " type='text' placeholder='请输入姓名'></td>" +
            "<td><button id=" + i + " class='delete'>删除</button></td></tr>";
        $(".table-list").append(newList);
        $(".guanliyuan-btn").css("display", "block");
        myid = "#" + i;

        //绑定一个点击事件， 删除按钮
        $(myid).click(function () {
            if (is_sure("确定要删除此管理员吗？")) {
                delete_user_id = $(this).attr('id');
                //alert(delete_user_id);
                $(this).parent().parent().remove();
                user_ids[user_ids.indexOf(delete_user_id)] = 0;
                new_user_ids[new_user_ids.indexOf(delete_user_id)] = 0;
                ajax_get("http://127.0.0.1:8080/setting/deluset", { 'action': 'deluser', 'id': delete_user_id }, true)
            }
        })
    })

    //管理员设置 保存按钮
    $(".guanliyuanbtn-save").click(function () {
        if (check_user_set()) {
            $(".table-list tr").find("input").attr("readonly", true);
            $(".table-list tr").find("input").css("border", "none");
            $(".guanliyuan-btn").css("display", "none");
            push_user()
        }
        else {
            alert('选项不能为空')
        }

    })
    // //管理员设置取消按钮
    // $(".guanliyuanbtn-cancel").click(function () {
    //     $(".table-list tr").find("input").val("");
    // })

    //网盘保存按钮
    $(".wangpanbtn-save").click(function () {
        if ($(".wangpanzhanghao").val() != '' && $(".wangpanmima").val() != '') {
            //状态改为不可编辑
            $(".wangpan-content").find("input").attr("readonly", true);
            $("#timeselect").attr("disabled", true);
            $(".wangpan-btn").css("display", "none");
            $(".edit").css("display", "block");
            oldwangpanzhanghao = $(".wangpanzhanghao").val();
            oldwangpanmima = $(".wangpanmima").val();
            oldtimetext = $("#timeselect").find("option:selected").text();
            selectchecked = $("#timeselect").val();

            var send_url = "http://127.0.0.1:8080/setting/yunpan"
            var send_data = { "username": oldwangpanzhanghao, "passwd": oldwangpanmima, "backuptime": oldtimetext };
            ajax_get(send_url, send_data, true); //提交后台
        }
        else {
            alert("账号密码不能为空")
        }
    })

    function ajax_get(send_url, send_data, is_async) {
        $.ajax({
            type: 'get',
            url: send_url,
            data: send_data,
            async: is_async,
            timeout: 30000,
            success: function (result) {
                if (result['state'] == "success") {
                    alert('hahahhahahahahah')
                    return true;
                }
                else {
                    alert("【操作失败】 " + result)
                    return false;
                }
            }
        });
    }

    function add_user(id, account, passwd, name) {
        var cls_account = 'account_' + id;
        var cls_passwd = 'passwd_' + id;
        var cls_name = 'name_' + id;
        var newList = "<tr><td><input class=" + cls_account + " type='text' placeholder=" + account + " readonly></td>" +
            "<td><input class=" + cls_passwd + " type='text' placeholder=" + passwd + " readonly></td>" +
            "<td><input class=" + cls_name + " type='text' placeholder=" + name + " readonly></td>" +
            "<td><button id=" + id + " class='delete'>删除</button></td></tr>";
        $(".table-list").append(newList);

        //添加点击事件
        myid = "#" + id
        $(myid).click(function () {
            if (is_sure("确定要删除此管理员吗？")) {
                delete_user_id = $(this).attr('id');
                //alert(delete_user_id);
                $(this).parent().parent().remove();
                user_ids[user_ids.indexOf(delete_user_id)] = 0;
                new_user_ids[new_user_ids.indexOf(delete_user_id)] = 0;
                ajax_get("http://127.0.0.1:8080/setting/deluser", { 'action': 'deluser', 'id': delete_user_id }, true)
            }
        })
    }


    //加载网页时，初始化管理员列表
    function init_user_list() {
        var user_list = $('.userinfo').html(); //读取隐藏在setting.tpl中的数据
        if (user_list == "") {
            return 'kong';
        }
        var user_array = new Array();
        user_array = user_list.split(",");
        var i = 0;
        //解析每条用户信息，添加到网页
        for (i = 0; i < user_array.length; i++) {
            var user_item = new Array();
            var user = user_array[i];

            user_item = user.split("#");
            var id = user_item[0];
            var account = user_item[1];
            var passwd = user_item[2];
            var name = user_item[3];

            user_ids[i] = id;
            add_user(id, account, passwd, name);
        }
    }

    // 检测用户列表设置是否为空，为空返回false，反正返回true
    function check_user_set() {
        var i = 0;
        var user_id = 0;
        var cls_userid;
        var cls_account;
        var cls_passwd;
        var cls_name;
        var send_data = { "action": "adduser", "id": "", "user": "", "passwd": "", "name": "" };
        for (i = 0; i < new_user_ids.length; i++) {
            user_id = new_user_ids[i];
            cls_userid = '.' + user_id;
            cls_account = '.account_' + user_id;
            cls_passwd = '.passwd_' + user_id;
            cls_name = '.name_' + user_id;

            send_data.id = user_id;
            send_data.user = $(cls_account).val();
            send_data.passwd = $(cls_passwd).val();
            send_data.name = $(cls_name).val();

            if (send_data.user == "" || send_data.passwd == "" || send_data.name == "") {
                return false
            }

        }

        return true
    }

    //新增用户提交到后台
    function push_user() {
        var i = 0;
        var user_id = 0;
        var cls_userid;
        var cls_account;
        var cls_passwd;
        var cls_name;
        var send_data = { "action": "adduser", "id": "", "user": "", "passwd": "", "name": "" }
        var send_url = "http://127.0.0.1:8080/setting/adduser"
        for (i = 0; i < new_user_ids.length; i++) {
            if (new_user_ids[i] != 0) {
                user_id = new_user_ids[i];
                cls_userid = '.' + user_id;
                cls_account = '.account_' + user_id;
                cls_passwd = '.passwd_' + user_id;
                cls_name = '.name_' + user_id;

                send_data.id = user_id;
                send_data.user = $(cls_account).val();
                send_data.passwd = $(cls_passwd).val();
                send_data.name = $(cls_name).val();

                ajax_get(send_url, send_data, true);

            }

        }
        //初始化新增户id数组
        new_user_ids = new Array();
    }

    function dele_user() {

    }

    //确认对话框
    function is_sure(message) {
        return confirm(message)
    }
    init_user_list();

})