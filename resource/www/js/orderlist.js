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