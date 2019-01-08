$(document).ready(function () {
    var now = new Date();
    var today_date = new Date((now.getYear() + 1900) + '-' + (now.getMonth() + 1) + '-' + (now.getDate()));
    today_date.setMonth(0)
    today_date.setDate(31)
    // alert(today_date.getMonth())
    // alert(today_date.getDate())
    alert(today_date)
    today_date.setMonth(2)
    
    // today_date.setDate(28)
    // today_date.setMonth(1)
    alert(today_date)
})