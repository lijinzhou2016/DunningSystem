$(document).ready(function () {
    var oldwangpanzhanghao;
    var oldwangpanmima;
    var selectchecked;

    oldwangpanzhanghao=$(".wangpanzhanghao").val();
    oldwangpanmima=$(".wangpanmima").val();
    selectchecked=$("#timeselect").val();;
    
    $(".edit").click(function(){
        $(".wangpan-btn").css("display","block");
        $(this).css("display","none");
        $(".wangpan-content").find("input").removeAttr("readonly");
        $("#timeselect").removeAttr("disabled");
        
    })
    
    
    $(".wangpanbtn-save").click(function() {
        $(".wangpan-content").find("input").attr("readonly",true);
        $("#timeselect").attr("disabled",true);
        $(".wangpan-btn").css("display","none");
        $(".edit").css("display","block");
        oldwangpanzhanghao=$(".wangpanzhanghao").val();
        oldwangpanmima=$(".wangpanmima").val();
        //selectchecked=$("#timeselect").find("option:selected").text();
        selectchecked=$("#timeselect").val();
        //alert(selectchecked);
        
    })
    
    $(".wangpanbtn-cancel").click(function(){
        $(".wangpan-content").find("input").attr("readonly",true);
        $(".wangpan-btn").css("display","none");
        $(".edit").css("display","block");
        $(".wangpanzhanghao").val(oldwangpanzhanghao);
        $(".wangpanmima").val(oldwangpanmima);
       // $("#timeselect").find("option[text='selectchecked']").attr("selected",true);
        $("#timeselect").val(selectchecked);
        $("#timeselect").attr("disabled",true);
        //alert($("#timeselect").find("option:selected").text())
        
    })
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
        $(".guanliyuan-btn").css("display", "block");
    })
    //删除本栏
    $(".delete").click(function () {
        $(this).parent().parent().remove();
    })

    //管理员设置保存按钮
    $(".guanliyuanbtn-save").click(function () {
        $(".table-list tr").find("input").attr("readonly", true);
        $(".table-list tr").find("input").css("border", "none");
        $(".guanliyuan-btn").css("display", "none");
    })
    //管理员设置取消按钮
    $(".guanliyuanbtn-cancel").click(function () {
        $(".table-list tr").find("input").val("");
    })

    //
    $(".wangpanbtn-save").click(function () {
        $(this).parent().css("display", "none");
    })

})