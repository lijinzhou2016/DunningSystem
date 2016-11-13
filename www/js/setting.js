$(document).ready(function () {
    //添加新的一栏
    $(".add").click(function () {
        var newList = "<tr><td><input type='text' placeholder='请输入账号'></td>" +
            "<td><input type='text' placeholder='请输入密码'></td>" +
            "<td><input type='text' placeholder='请输入姓名'></td>" +
            "<td><button class='delete'>删除</button></td></tr>";
        $(".table-list").append(newList);
        $(".delete").click(function () {
            $(this).parent().parent().remove();
        })
        $(".guanliyuan-btn").css("display","block");
    })
    //删除本栏
    $(".delete").click(function () {
        $(this).parent().parent().remove();
    })

    //管理员设置保存按钮
    $(".guanliyuanbtn-save").click(function () {
        $(".table-list tr").find("input").attr("readonly", true);
        $(".table-list tr").find("input").css("border", "none");
        $(".guanliyuan-btn").css("display","none");
    })
    //管理员设置取消按钮
    $(".guanliyuanbtn-cancel").click(function () {
        $(".table-list tr").find("input").val("");
    })

    //
    $(".wangpanbtn-save").click(function(){
        $(this).parent().css("display","none");
    })

    //
    $(".edit").click(function(){
        var Wzhanghao =$(".wangpanzhanghao").val();
        var Wmima =$(".wangpanmima").val();
        
        $(".wangpan-btn").css("display","block");
    })
})