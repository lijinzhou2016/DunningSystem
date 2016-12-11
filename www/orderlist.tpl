<html>

<head>
	<meta charset="UTF-8">
	<title>列表页</title>
	<script src="./jquery-1.11.1.min.js"></script>
	<script src="./fenye.js"></script>
	<script src="./orderlist.js"></script>
	<script src="./WdatePicker.js"></script>
	<script src="./spark-md5.min.js"></script>

	<link rel="stylesheet" href="./fenye.css">
	<link rel="stylesheet" href="./orderlist.css">

</head>

<body>
	<div class="head">
		<ul class="head-user">
			<li><img src="./icon_wp.png" style="height:16px;" alt="">{{userinfo.get('name')}}</li>
			<li><img src="./icon_tuichu.png" style="height:16px;" alt="">退出</li>
		</ul>
	</div>
	<div class="order-list">
		<div class="order-list-left">
			<div class="order-list-content">
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">姓名:</div><input class="order-list-content-search-right orderlist-username" type="text" value={{condition.get('order_username')}}></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">账期:</div>
					<select class="order-list-content-search-right order-zhangqi" id="order-zhangqi" type="text">
					%if condition['order_zhangqi']:
						<option value="">{{condition.get('order_zhangqi')}}</option>
					%else:
						<option value="">全部</option>
					%end
					<option value="">M0</option>
					<option value="">M1</option>
					<option value="">M2</option>
					<option value="">M3</option>
					<option value="">M4</option>
					<option value="">M5</option>
					<option value="">M6</option>
					<option value="">M7</option>
					<option value="">M8</option>
					<option value="">M9</option>
					<option value="">M10</option>
					<option value="">M11</option>
					<option value="">M12</option>
					</select>
				</div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">学校:</div><input class="order-list-content-search-right order-school" type="text" value={{condition.get('order_school')}}>
				</div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">家庭住址:</div><input class="order-list-content-search-right order-jtzz" type="text" value={{condition.get('order_jtzz')}}></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">家庭区域:</div><input class="order-list-content-search-right order-jtqy" type="text" value={{condition.get('order_jtqy')}}></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">订单日期:</div><input class="order-list-content-search-right order-jdrq Wdate" type="text" onClick="WdatePicker()" value={{condition.get('order_jdrq')}}></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">接单日期:</div><input class="order-list-content-search-right order-shxx Wdate" type="text" onClick="WdatePicker()" value={{condition.get('order_shxx')}}>
				</div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">订单状态:</div>
					<select class="order-list-content-search-right order-ddzt" id="order-ddzt" type="text">
				%if condition['order_ddzt']:
					<option value="">{{condition.get('order_ddzt')}}</option>
				%else:
                	<option value="">全部</option>
				%end
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
				
				<div class="clear"></div>
				<div class="order-search-btn">
					<input type="button" class="search-btn" onclick="searchBtn()" value="搜索">
					<input type="button" class="reset-btn" onclick="resetBtn()" value="重置">
				</div>


			</div>
			<table class="order-list-table">
				<thead>
					<tr>
						<th class="select-result-content" style="display:none" colspan="8">
							已选条件：<span class="chooseinputval">
								{{condition.get('order_username')}} {{condition.get('order_zhangqi')}} {{condition.get('order_school')}}
								{{condition.get('order_jtzz')}} {{condition.get('order_jtqy')}} {{condition.get('order_jdrq')}}
								{{condition.get('order_shxx')}} {{condition.get('order_ddzt')}}
							</span>
						</th>
						
					</tr>
					<tr>
						<td colspan="8" style="border:none;height:10px;"></td>
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
					%for item in orders_list:
					<tr>
						<td class="ordernumber"> <a href={{item.get('detailurl')}} target="_blank">
							{{item.get('ordernumber')}}</a></td>
						<td>
							<div class="name" title={{item.get('name')}}>{{item.get('name')}}</div>
						</td>
						<td>{{item.get('phone')}}</td>
						<td>{{item.get('qiankuan')}}</td>
						<td>{{item.get('orderdata')}}</td>
						<td>{{item.get('acquiringdata')}}</td>
						<td>
							<div class="schoolName" title={{item.get('school')}}>{{item.get('school')}}</div>
						</td>
						<td>{{item.get('state')}}</td>
					%end
				</tbody>

			</table>
			<div class="clear"></div>
			<div id="div_pager" style="text-align:center;"></div>
			<input type="hidden" class="totalPage" value={{fenyeinfo.get('total_pages')}}>
			<input type="hidden" class="totalRecords" value={{fenyeinfo.get('total_orders')}}>
			<input type="hidden" class="session_info" value={{userinfo.get('session')}}>
		</div>

		<div class="order-list-right">
			<form id="uploadForm">
				<input name='testmd5' id='jisuan_md5' hidden />
				<input name='name' id='wherefrom' type="text" placeholder="请输入订单来源" />
				<input type="file" id='myfile' name='data' value="选择文件" />
				<input type="button" value="上传" class='upload' onclick='ajaxupLoad()'/>
			</form>
			<img class='loadding' src='./loading.gif'/>
			<a href={{fenyeinfo.get('detail_url')}} target="_blank"><input type="button" value="手动创建" style="border:1px solid #ccc;outline:none;background:url(./icon-zhanghushezhi.png) no-repeat 10px;width:80%;height:30px;background-size:20px;"></a>
			%if userinfo['is_admin']==1:
			<a id='setting' href={{fenyeinfo.get('setting_url')}} target="_blank">
				<input type="button" value="设置" style="margin-top:30px;border:1px solid #ccc;outline:none;background:url(./icon-zhanghushezhi.png) no-repeat 10px;width:80%;height:30px;background-size:20px;"/>
			</a>
			%end
		</div>
	</div>
	<script>
		var log=document.getElementById("jisuan_md5");
			document.getElementById("myfile").addEventListener("change", function() {
				var blobSlice = File.prototype.slice || File.prototype.mozSlice || File.prototype.webkitSlice,
					file = this.files[0],
					chunkSize = 2097152, // read in chunks of 2MB
					chunks = Math.ceil(file.size / chunkSize),
					currentChunk = 0,
					spark = new SparkMD5.ArrayBuffer(),
					frOnload = function(e){
						//log.innerHTML+="\nread chunk number "+parseInt(currentChunk+1)+" of "+chunks;
						spark.append(e.target.result); // append array buffer
						currentChunk++;
						if (currentChunk < chunks)
							loadNext();
						else
						   //log.innerHTML+="\nfinished loading :)\n\ncomputed hash:\n"+spark.end()+"\n\nyou can select another file now!\n";
						   log.value=spark.end();
						   //alert(spark.end())
					},
					frOnerror = function () {
						log.value="\noops, something went wrong.";
					};
				function loadNext() {
					var fileReader = new FileReader();
					fileReader.onload = frOnload;
					fileReader.onerror = frOnerror;
					var start = currentChunk * chunkSize,
						end = ((start + chunkSize) >= file.size) ? file.size : start + chunkSize;
					fileReader.readAsArrayBuffer(blobSlice.call(file, start, end));
				};
				//log.style.display="inline-block";
				//log.innerHTML="file name: "+file.name+" ("+file.size.toString().replace(/\B(?=(?:\d{3})+(?!\d))/g, ',')+" bytes)\n";
				loadNext();
				
			});
			

	</script>
</body>

</html>