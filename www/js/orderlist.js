$(document).ready(function () {
    var pageUrl = "";

    /* window.onload=function(){
        pageUrl=window.location.href;
    } */

    function getParameter(name) {

        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");

        var r = window.location.search.substr(1).match(reg);

        if (r != null)
            return unescape(r[2]);
        return null;
    }


    var totalPage = $(".totalPage").val();

    var totalRecords = $(".totalRecords").val();

    var pageNo = getParameter('pageIndex');

    if (!pageNo) {

        pageNo = 1;

    }
    //生成分页控件

    kkpager.init({
        pageIndex: pageNo,
        //总页码

        total: totalPage,
        //总数据条数

        totalRecords: totalRecords,
        //链接前部

        hrefFormer: pageUrl,
        //链接尾部

        hrefLatter: '',

        getLink: function (n) {

            return this.hrefFormer + this.hrefLatter + "?pageIndex=" + n;

        }

    });

    kkpager.generPageHtml();


    $(".order-list-table tbody tr").hover(function () { //tr:gt(0)表示不选第一行，因为第一行往往是标题
        $(this).addClass("tron");

    }, function () {
        $(this).removeClass("tron");
    });
    // $(".order-list-table tbody tr").find("td").eq(0).hover(function () {
    //     $(this).css("color", "red");
    // }, function () {
    //     $(this).css("color", "#666");
    // })


})
//searchbtn
function searchBtn() {
    var order_username = $(".orderlist-username").val();
    var order_zhangqi = $(".order-zhangqi").val();
    var order_school = $(".order-school").val();
    var order_jtzz = $(".order-jtzz").val();
    var order_jtqy = $(".order-jtqy").val();
    var order_jdrq = $(".order-jdrq").val();
    var order_ddzt = $(".order-ddzt").find("option:selected").text();
    if (order_ddzt == "全部") {
        order_ddzt = "";
    }
    var order_shxx = $(".order-shxx").val();
    var inputval = order_username + " " + order_zhangqi + " " + order_school + " " + order_jtzz + " " + order_jtqy + " " + order_jdrq + " " + order_ddzt + " " + order_shxx;

    if (inputval.length > 7) {
        $(".select-result-content").show();
    }
    $(".chooseinputval").text(inputval);

}

//resetBtn
function resetBtn() {
    $(".order-list-content-search").find("input").val("");
    $("#order-ddzt option:first").prop("selected", 'selected');
    $(".chooseinputval").text("");
    $(".select-result-content").hide();
}

function ajaxupLoad() {

    var file = $("#myfile").val();
    var ext = file.slice(file.lastIndexOf(".") + 1).toLowerCase();
    alert(ext);
    if ('xls' == ext || 'xlsx' == ext) {
        var formData = new FormData($("#uploadForm")[0]);
        $.ajax({
            url: '/upload',
            type: 'POST',
            data: formData,
            async: false,
            cache: false,
            contentType: false,
            processData: false,
            success: function (returndata) {
                alert(returndata);
            },
            error: function (returndata) {
                alert('error')
                alert(returndata)
            }
        });
    }
    else {
        alert('请上传excel文件')
    }

}
