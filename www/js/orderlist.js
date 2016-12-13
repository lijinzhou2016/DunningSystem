$(document).ready(function () {
    $('.loadding').hide()

    var tmp=$('.chooseinputval').val()
    if (tmp>0){
        $(".select-result-content").show();
    }

    var pageUrl = "";

    var condition=0
    var search_item = {
        'order_username': '',
        'order_zhangqi': '',
        'order_school': '',
        'order_jtzz': '',
        'order_jtqy': '',
        'order_jdrq': '',
        'order_ddzt': '',
        'order_shxx': ''
    }

    search_item.order_username = $(".orderlist-username").val();
    search_item.order_zhangqi = $(".order-zhangqi").find("option:selected").text();
    search_item.order_school = $(".order-school").val();
    search_item.order_jtzz = $(".order-jtzz").val();
    search_item.order_jtqy = $(".order-jtqy").val();
    search_item.order_jdrq = $(".order-jdrq").val();
    search_item.order_ddzt = $(".order-ddzt").find("option:selected").text();
    var mysession = '&session=' + $('.session_info').val();

    if (search_item.order_ddzt == "全部") {
        search_item.order_ddzt = "";
    }
    if (search_item.order_zhangqi == "全部") {
        search_item.order_zhangqi = "";
    }
    search_item.order_shxx = $(".order-shxx").val();
    var inputval = '';
    var search_condition = '';
    for (var key in search_item) {
        inputval += (search_item[key] + ' ');
    }

    if (inputval.length > 8) {
        condition=1
        $(".select-result-content").show();
        $(".chooseinputval").text(inputval);
        for (var key in search_item) {
            if (search_item[key] != '') {
                search_condition += ('&' + key + '=' + search_item[key])
            }
        }
    }

    

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
    var mysession = '&session=' + $('.session_info').val();
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

            return this.hrefFormer + "?pageIndex=" + n + '&condition=' + condition + mysession + search_condition;

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

///////////////////
//searchbtn
var search_item = {
    'order_username': '',
    'order_zhangqi': '',
    'order_school': '',
    'order_jtzz': '',
    'order_jtqy': '',
    'order_jdrq': '',
    'order_ddzt': '',
    'order_shxx': ''
}

function searchBtn() {
    search_item.order_username = $(".orderlist-username").val();
    search_item.order_zhangqi = $(".order-zhangqi").find("option:selected").text();
    search_item.order_school = $(".order-school").val();
    search_item.order_jtzz = $(".order-jtzz").val();
    search_item.order_jtqy = $(".order-jtqy").val();
    search_item.order_jdrq = $(".order-jdrq").val();
    search_item.order_ddzt = $(".order-ddzt").find("option:selected").text();
    var mysession = '&session=' + $('.session_info').val();
    if (search_item.order_ddzt == "全部") {
        search_item.order_ddzt = "";
    }
    if (search_item.order_zhangqi == "全部") {
        search_item.order_zhangqi = "";
    }
    search_item.order_shxx = $(".order-shxx").val();
    // var inputval = order_username + " " + order_zhangqi + " " + order_school + " " + order_jtzz + " " + order_jtqy + " " + order_jdrq + " " + order_ddzt + " " + order_shxx;
    var inputval = '';
    var search_condition = '';
    for (var key in search_item) {
        inputval += (search_item[key] + ' ');
    }

    if (inputval.length > 8) {
        for (var key in search_item) {
            if (search_item[key] != '') {
                search_condition += ('&' + key + '=' + search_item[key])
            }
        }
        //alert(search_condition)
        window.location.href = '?pageIndex=1&condition=1' + mysession + search_condition
        // $(".select-result-content").show();
        // $(".chooseinputval").text(inputval);
    }
    else {
        alert('请选择搜索条件')
    }
}

//resetBtn
function resetBtn() {
    var mysession = $('.session_info').val();
    location.href='/orderlist?pageIndex=1&condition=0&session='+mysession
}

function ajaxupLoad() {
    var mysession = $('.session_info').val();
    var file = $("#myfile").val();
    var wherefrom = $("#wherefrom").val();
    var ext = file.slice(file.lastIndexOf(".") + 1).toLowerCase();

    if (wherefrom==''){
        alert('请输入订单来源');
        return;
    }
    if (file==''){
        alert('请选择文件');
        return;
    }

    if ('xls' == ext || 'xlsx' == ext || 'xlsm' == ext) {
        $('.upload').hide()
        $('.loadding').show()
        var formData = new FormData($("#uploadForm")[0]);
        $.ajax({
            url: '/upload',
            type: 'POST',
            data: formData,
            async: true,
            cache: false,
            contentType: false,
            processData: false,
            success: function (returndata) {
                $('.loadding').hide()
                $('.upload').show()
                alert(returndata);
                location.href='/orderlist?pageIndex=1&condition=0&session='+mysession
            },
            error: function (returndata) {
                $('.loadding').hide()
                $('.upload').show()
                alert(returndata)
            }
        });
    }
    else {
        alert('请选择excel文件')
    }

}
