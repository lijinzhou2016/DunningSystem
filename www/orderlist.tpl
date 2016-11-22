<html>

<head>
	<meta charset="UTF-8">
	<title>列表页</title>
	<script src="jquery-1.11.1.min.js"></script>
	<script src="fenye.js"></script>
	<script src="orderlist.js"></script>
	<link rel="stylesheet" href="fenye.css">
	<link rel="stylesheet" href="orderlist.css">
</head>

<body>
	<div class="head">
		<ul class="head-user">
			<li><img src="icon_wp.png" style="height:16px;" alt="">{{username}}</li>
			<li><img src="icon_tuichu.png" style="height:16px;" alt="">退出</li>
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
				<div class="order-list-content-search-left">学校:</div><input class="order-list-content-search-right" type="text">
					</div>
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
						<td class="ordernumber"> <a href={{detailurl_0}} target="_blank">
							{{ordernumber_0}}</a></td>
						<td ><div class="name" title={{name_0}}>{{name_0}}</div></td>
						<td>{{phone_0}}</td>
						<td>{{qiankuan_0}}</td>
						<td>{{orderdata_0}}</td>
						<td>{{acquiringdata_0}}</td>
						<td><div class="schoolName" title={{school_0}}>{{school_0}}</div></td>
						<td>{{state_0}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_1}} target="_blank">
							{{ordernumber_1}}</a></td>
						<td><div class="name" title={{name_1}}>{{name_1}}</div></td>
						<td>{{phone_1}}</td>
						<td>{{qiankuan_1}}</td>
						<td>{{orderdata_1}}</td>
						<td>{{acquiringdata_1}}</td>
						<td><div class="schoolName" title={{school_1}}>{{school_1}}</div></td>
						<td>{{state_1}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_2}} target="_blank">
							{{ordernumber_2}}</a></td>
						<td><div class="name" title={{name_2}}>{{name_2}}</div></td>
						<td>{{phone_2}}</td>
						<td>{{qiankuan_2}}</td>
						<td>{{orderdata_2}}</td>
						<td>{{acquiringdata_2}}</td>
						<td><div class="schoolName" title={{school_2}}>{{school_2}}</div></td>
						<td>{{state_2}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_3}} target="_blank">
							{{ordernumber_3}}</a></td>
						<td><div class="name" title={{name_3}}>{{name_3}}</div></td>
						<td>{{phone_3}}</td>
						<td>{{qiankuan_3}}</td>
						<td>{{orderdata_3}}</td>
						<td>{{acquiringdata_3}}</td>
						<td><div class="schoolName" title={{school_3}}>{{school_3}}</div></td>
						<td>{{state_3}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_4}} target="_blank">
							{{ordernumber_4}}</a></td>
						<td><div class="name" title={{name_4}}>{{name_4}}</div></td>
						<td>{{phone_4}}</td>
						<td>{{qiankuan_4}}</td>
						<td>{{orderdata_4}}</td>
						<td>{{acquiringdata_4}}</td>
						<td><div class="schoolName" title={{school_4}}>{{school_4}}</div></td>
						<td>{{state_4}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_5}} target="_blank">
							{{ordernumber_5}}</a></td>
						<td><div class="name" title={{name_5}}>{{name_5}}</div></td>
						<td>{{phone_5}}</td>
						<td>{{qiankuan_5}}</td>
						<td>{{orderdata_5}}</td>
						<td>{{acquiringdata_5}}</td>
						<td><div class="schoolName" title={{school_5}}>{{school_5}}</div></td>
						<td>{{state_5}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_6}} target="_blank">
							{{ordernumber_6}}</a></td>
						<td><div class="name" title={{name_6}}>{{name_6}}</div></td>
						<td>{{phone_6}}</td>
						<td>{{qiankuan_6}}</td>
						<td>{{orderdata_6}}</td>
						<td>{{acquiringdata_6}}</td>
						<td><div class="schoolName" title={{school_6}}>{{school_6}}</div></td>
						<td>{{state_6}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_7}} target="_blank">
							{{ordernumber_7}}</a></td>
						<td><div class="name" title={{name_7}}>{{name_7}}</div></td>
						<td>{{phone_7}}</td>
						<td>{{qiankuan_7}}</td>
						<td>{{orderdata_7}}</td>
						<td>{{acquiringdata_7}}</td>
						<td><div class="schoolName" title={{school_7}}>{{school_7}}</div></td>
						<td>{{state_7}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_8}} target="_blank">
							{{ordernumber_8}}</a></td>
						<td><div class="name" title={{name_8}}>{{name_8}}</div></td>
						<td>{{phone_8}}</td>
						<td>{{qiankuan_8}}</td>
						<td>{{orderdata_8}}</td>
						<td>{{acquiringdata_8}}</td>
						<td><div class="schoolName" title={{school_8}}>{{school_8}}</div></td>
						<td>{{state_8}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_9}} target="_blank">
							{{ordernumber_9}}</a></td>
						<td><div class="name" title={{name_9}}>{{name_9}}</div></td>
						<td>{{phone_9}}</td>
						<td>{{qiankuan_9}}</td>
						<td>{{orderdata_9}}</td>
						<td>{{acquiringdata_9}}</td>
						<td><div class="schoolName" title={{school_9}}>{{school_9}}</div></td>
						<td>{{state_9}}</td>

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
			<a href='http://127.0.0.1:8080/setting?action=jump' target="_blank">
			<input type="button" value="设置" style="margin-top:30px;border:1px solid #ccc;outline:none;background:url(http:127.0.0.1:8080/icon-zhanghushezhi.png) no-repeat 10px;width:80%;height:30px;background-size:20px;">
			</a>
		</div>

	</div>
	<script>
		function setting(){
			alert('setting post json')
			var url = "http://127.0.0.1:8080/setting";
			var json={'action':'jump'};
			var post={data:JSON.stringify(json)};
			$.post(url,post);
		}
	</script>

</body>

</html>