<html>

<head>
	<meta charset="UTF-8">
	<title>列表页</title>
	<script src="js/jquery-1.11.1.min.js"></script>
	<script src="js/fenye.js"></script>
	<script src="js/orderlist.js"></script>
	<script src="js/WdatePicker.js"></script>
	<script src="js/spark-md5.min.js"></script>

	<link rel="stylesheet" href="css/fenye.css">
	<link rel="stylesheet" href="css/orderlist.css">


</head>

<body>
	<div class="head">
		<ul class="head-user">
			<li><img src="images/icon_wp.png" style="height:16px;" alt="">{{username}}</li>
			<li><img src="images/icon_tuichu.png" style="height:16px;" alt="">退出</li>
		</ul>
	</div>
	<div class="order-list">
		<div class="order-list-left">
			<div class="order-list-content">
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">姓名:</div><input class="order-list-content-search-right orderlist-username" type="text"></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">账期:</div><input class="order-list-content-search-right order-zhangqi" type="text"></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">学校:</div><input class="order-list-content-search-right order-school" type="text">
				</div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">家庭住址:</div><input class="order-list-content-search-right order-jtzz" type="text"></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">家庭区域:</div><input class="order-list-content-search-right order-jtqy" type="text"></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">接单日期:</div><input class="order-list-content-search-right order-jdrq Wdate" type="text" onClick="WdatePicker()"></div>
				<div class="order-list-content-search">
					<div class="order-list-content-search-left">订单状态:</div>
					<select class="order-list-content-search-right order-ddzt" id="order-ddzt" type="text">
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
					<div class="order-list-content-search-left">商户状态:</div><input class="order-list-content-search-right order-shxx" type="text">
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
							已选条件：<span class="chooseinputval"></span>
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
					<tr>
						<td class="ordernumber"> <a href={{detailurl_0}} target="_blank">
							{{ordernumber_0}}</a></td>
						<td>
							<div class="name" title={{name_0}}>{{name_0}}</div>
						</td>
						<td>{{phone_0}}</td>
						<td>{{qiankuan_0}}</td>
						<td>{{orderdata_0}}</td>
						<td>{{acquiringdata_0}}</td>
						<td>
							<div class="schoolName" title={{school_0}}>{{school_0}}</div>
						</td>
						<td>{{state_0}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_1}} target="_blank">
							{{ordernumber_1}}</a></td>
						<td>
							<div class="name" title={{name_1}}>{{name_1}}</div>
						</td>
						<td>{{phone_1}}</td>
						<td>{{qiankuan_1}}</td>
						<td>{{orderdata_1}}</td>
						<td>{{acquiringdata_1}}</td>
						<td>
							<div class="schoolName" title={{school_1}}>{{school_1}}</div>
						</td>
						<td>{{state_1}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_2}} target="_blank">
							{{ordernumber_2}}</a></td>
						<td>
							<div class="name" title={{name_2}}>{{name_2}}</div>
						</td>
						<td>{{phone_2}}</td>
						<td>{{qiankuan_2}}</td>
						<td>{{orderdata_2}}</td>
						<td>{{acquiringdata_2}}</td>
						<td>
							<div class="schoolName" title={{school_2}}>{{school_2}}</div>
						</td>
						<td>{{state_2}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_3}} target="_blank">
							{{ordernumber_3}}</a></td>
						<td>
							<div class="name" title={{name_3}}>{{name_3}}</div>
						</td>
						<td>{{phone_3}}</td>
						<td>{{qiankuan_3}}</td>
						<td>{{orderdata_3}}</td>
						<td>{{acquiringdata_3}}</td>
						<td>
							<div class="schoolName" title={{school_3}}>{{school_3}}</div>
						</td>
						<td>{{state_3}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_4}} target="_blank">
							{{ordernumber_4}}</a></td>
						<td>
							<div class="name" title={{name_4}}>{{name_4}}</div>
						</td>
						<td>{{phone_4}}</td>
						<td>{{qiankuan_4}}</td>
						<td>{{orderdata_4}}</td>
						<td>{{acquiringdata_4}}</td>
						<td>
							<div class="schoolName" title={{school_4}}>{{school_4}}</div>
						</td>
						<td>{{state_4}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_5}} target="_blank">
							{{ordernumber_5}}</a></td>
						<td>
							<div class="name" title={{name_5}}>{{name_5}}</div>
						</td>
						<td>{{phone_5}}</td>
						<td>{{qiankuan_5}}</td>
						<td>{{orderdata_5}}</td>
						<td>{{acquiringdata_5}}</td>
						<td>
							<div class="schoolName" title={{school_5}}>{{school_5}}</div>
						</td>
						<td>{{state_5}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_6}} target="_blank">
							{{ordernumber_6}}</a></td>
						<td>
							<div class="name" title={{name_6}}>{{name_6}}</div>
						</td>
						<td>{{phone_6}}</td>
						<td>{{qiankuan_6}}</td>
						<td>{{orderdata_6}}</td>
						<td>{{acquiringdata_6}}</td>
						<td>
							<div class="schoolName" title={{school_6}}>{{school_6}}</div>
						</td>
						<td>{{state_6}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_7}} target="_blank">
							{{ordernumber_7}}</a></td>
						<td>
							<div class="name" title={{name_7}}>{{name_7}}</div>
						</td>
						<td>{{phone_7}}</td>
						<td>{{qiankuan_7}}</td>
						<td>{{orderdata_7}}</td>
						<td>{{acquiringdata_7}}</td>
						<td>
							<div class="schoolName" title={{school_7}}>{{school_7}}</div>
						</td>
						<td>{{state_7}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_8}} target="_blank">
							{{ordernumber_8}}</a></td>
						<td>
							<div class="name" title={{name_8}}>{{name_8}}</div>
						</td>
						<td>{{phone_8}}</td>
						<td>{{qiankuan_8}}</td>
						<td>{{orderdata_8}}</td>
						<td>{{acquiringdata_8}}</td>
						<td>
							<div class="schoolName" title={{school_8}}>{{school_8}}</div>
						</td>
						<td>{{state_8}}</td>

					</tr>
					<tr>
						<td class="ordernumber"> <a href={{detailurl_9}} target="_blank">
							{{ordernumber_9}}</a></td>
						<td>
							<div class="name" title={{name_9}}>{{name_9}}</div>
						</td>
						<td>{{phone_9}}</td>
						<td>{{qiankuan_9}}</td>
						<td>{{orderdata_9}}</td>
						<td>{{acquiringdata_9}}</td>
						<td>
							<div class="schoolName" title={{school_9}}>{{school_9}}</div>
						</td>
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
			<form id="uploadForm">
				<input name='testmd5' id='jisuan_md5' hidden />
				<input name='name' id='wherefrom' type="text" placeholder="请输入订单来源" />
				<input type="file" id='myfile' name='data' value="选择文件" />
				<input type="button" value="上传" onclick='ajaxupLoad()' />
			</form>
			<a href="orderDetail.html" target="_blank"><input type="button" value="手动创建" style="border:1px solid #ccc;outline:none;background:url(images/icon-zhanghushezhi.png) no-repeat 10px;width:80%;height:30px;background-size:20px;"></a>
			<a href='http://127.0.0.1:8080/setting/jump' target="_blank">
				<input type="button" value="设置" style="margin-top:30px;border:1px solid #ccc;outline:none;background:url(images/icon-zhanghushezhi.png) no-repeat 10px;width:80%;height:30px;background-size:20px;"
				/>
			</a>
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