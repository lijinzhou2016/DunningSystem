<html>

<head>
	<meta charset="UTF-8">
	<title>列表页</title>
	<script src="http:127.0.0.1:8080/jquery-1.11.1.min.js"></script>
	<script src="http:127.0.0.1:8080/fenye.js"></script>
	<script src="http:127.0.0.1:8080/orderlist.js"></script>
	<link rel="stylesheet" href="http:127.0.0.1:8080/fenye.css">
	<link rel="stylesheet" href="http:127.0.0.1:8080/orderlist.css">
</head>

<body>
	<div class="head">
		<ul class="head-user">
			<li><img src="http:127.0.0.1:8080/icon_wp.png" style="height:16px;" alt="">用户名</li>
			<li><img src="http:127.0.0.1:8080/icon_tuichu.png" style="height:16px;" alt="">退出</li>
		</ul>
	</div>
	<div class="order-list">
		<div class="order-list-left">
			<div class="order-list-content">
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">姓名:</div><input class="order-list-content-search-right" type="text"></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">账期:</div><input class="order-list-content-search-right" type="text"></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">学校:</div>
					<select class="order-list-content-search-right" type="text">
                <option value="">全部</option>
                <option value="">清华大学</option>
                 <option value="">北京大学</option>
            </select></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">家庭住址:</div><input class="order-list-content-search-right" type="text"></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">家庭区域:</div><input class="order-list-content-search-right" type="text"></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">接单日期:</div><input class="order-list-content-search-right" type="text"></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">订单状态:</div>
					<select class="order-list-content-search-right" type="text">
                <option value="">全部</option>
                <option value="">联系本人</option>
                <option value="">联系亲属</option>
                <option value="">联系同学</option>
                <option value="">失联</option>
                <option value="">待外访</option>
                <option value="">外访中</option>
                <option value="">承诺还款</option>
                <option value="">部分还款</option>
                <option value="">已结清</option>
            </select>
				</div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">商户状态:</div><input class="order-list-content-search-right" type="text">
				</div>
				<div class="clear"></div>
				<div class="order-search-btn">
					<input type="button" class="search-btn" value="搜索">
					<input type="button" class="reset-btn" value="重置">
				</div>


			</div>
			<table class="order-list-table">
				<thead>
					<tr>
						<th class="select-result-content" colspan="8">
							已选条件：
						</th>
					</tr>
					<tr>
						<td colspan="8" style="border:none;"></td>
					</tr>
					<tr>
						<th>订单编号</th>
						<th>姓名</th>
						<th>电话</th>
						<th>总欠款</th>
						<th>订单日期</th>
						<th>收单日期</th>
						<th>学校</th>
						<th>状态</th>
					</tr>
				</thead>

				<tbody>
					<tr>
						<td class="ordernumber"> <a href="http:127.0.0.1:8080/orderDetail.html" target="_blank">
                            20161104</a></td>
						<td ><div class="name" title="刘德华刘德华">刘德华刘德华</div></td>
						<td>137712345678</td>
						<td>333333</td>
						<td>2016-10-10</td>
						<td>2016-11-01</td>
						<td><div class="schoolName" title="中国传媒大学南广学院">中国传媒大学南广学院</div></td>
						<td>已结清</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href="">
                            20161104</a></td>
						<td><div class="name" title="刘德华刘德华">刘德华刘德华</div></td>
						<td>137712345678</td>
						<td>333333</td>
						<td>2016-10-10</td>
						<td>2016-11-01</td>
						<td><div class="schoolName" title="中国传媒大学南广学院">中国传媒大学南广学院</div></td>
						<td>已结清</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href="">
                            20161104</a></td>
						<td><div class="name" title="刘德华刘德华">刘德华刘德华</div></td>
						<td>137712345678</td>
						<td>333333</td>
						<td>2016-10-10</td>
						<td>2016-11-01</td>
						<td><div class="schoolName" title="中国传媒大学南广学院">中国传媒大学南广学院</div></td>
						<td>已结清</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href="">
                            20161104</a></td>
						<td><div class="name" title="刘德华刘德华">刘德华刘德华</div></td>
						<td>137712345678</td>
						<td>333333</td>
						<td>2016-10-10</td>
						<td>2016-11-01</td>
						<td><div class="schoolName" title="中国传媒大学南广学院">中国传媒大学南广学院</div></td>
						<td>已结清</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href="">
                            20161104</a></td>
						<td><div class="name" title="刘德华刘德华">刘德华刘德华</div></td>
						<td>137712345678</td>
						<td>333333</td>
						<td>2016-10-10</td>
						<td>2016-11-01</td>
						<td><div class="schoolName" title="中国传媒大学南广学院">中国传媒大学南广学院</div></td>
						<td>已结清</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href="">
                            20161104</a></td>
						<td><div class="name" title="刘德华刘德华">刘德华刘德华</div></td>
						<td>137712345678</td>
						<td>333333</td>
						<td>2016-10-10</td>
						<td>2016-11-01</td>
						<td><div class="schoolName" title="中国传媒大学南广学院">中国传媒大学南广学院</div></td>
						<td>已结清</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href="">
                            20161104</a></td>
						<td><div class="name" title="刘德华刘德华">刘德华刘德华</div></td>
						<td>137712345678</td>
						<td>333333</td>
						<td>2016-10-10</td>
						<td>2016-11-01</td>
						<td><div class="schoolName" title="中国传媒大学南广学院">中国传媒大学南广学院</div></td>
						<td>已结清</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href="">
                            20161104</a></td>
						<td><div class="name" title="刘德华刘德华">刘德华刘德华</div></td>
						<td>137712345678</td>
						<td>333333</td>
						<td>2016-10-10</td>
						<td>2016-11-01</td>
						<td><div class="schoolName" title="中国传媒大学南广学院">中国传媒大学南广学院</div></td>
						<td>已结清</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href="">
                            20161104</a></td>
						<td><div class="name" title="刘德华刘德华">刘德华刘德华</div></td>
						<td>137712345678</td>
						<td>333333</td>
						<td>2016-10-10</td>
						<td>2016-11-01</td>
						<td><div class="schoolName" title="中国传媒大学南广学院">中国传媒大学南广学院</div></td>
						<td>已结清</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href="">
                            20161104</a></td>
						<td><div class="name" title="刘德华刘德华">刘德华刘德华</div></td>
						<td>137712345678</td>
						<td>333333</td>
						<td>2016-10-10</td>
						<td>2016-11-01</td>
						<td><div class="schoolName" title="中国传媒大学南广学院">中国传媒大学南广学院</div></td>
						<td>已结清</td>

					</tr>
				</tbody>

			</table>
			<div class="clear"></div>
			<div id="div_pager" style="text-align:center;"></div>
			<input type="hidden" class="totalPage" value="10">
			<input type="hidden" class="totalRecords" value="100">
		</div>

		<div class="order-list-right">
			<input type="text" placeholder="请输入订单来源">
			<input type="file" value="选择文件">
			<input type="button" value="上传">
			<a href="orderDetail.html" target="_blank"><input type="button" value="手动创建" style="border:1px solid #ccc;outline:none;background:url(http:127.0.0.1:8080/icon-zhanghushezhi.png) no-repeat 10px;width:80%;height:30px;background-size:20px;"></a>
			<input type="button" value="设置" style="margin-top:30px;border:1px solid #ccc;outline:none;background:url(http:127.0.0.1:8080/icon-zhanghushezhi.png) no-repeat 10px;width:80%;height:30px;background-size:20px;">
		</div>

	</div>


</body>

</html>