<html>

<head>
	<meta charset="UTF-8">
	<title>详情页面</title>
	<link rel="stylesheet" href="../orderDetail.css">
    <script src="../jquery-1.11.1.min.js"></script>
    <script src="../orderDetail.js"></script>
</head>

<body>
	<div class="head">
		<ul class="head-user">
			<li id = "admin_name">
				<img src="../icon_wp.png" style="height:16px;" alt="">
				<input type="text" name="admin_id" style="display:none" value={{user.get('id')}}>
				{{user.get('name')}}
			</li>
			<li><img src="../icon_tuichu.png" style="height:16px;" alt="">退出</li>
		</ul>
	</div>
	<div class="orderDetail-content">
		<div class="orderDetail-content-title">
			<div style="width:3px;height:20px;background:#FF6600;float:left;margin-right:20px;"></div>
			详情页面
		</div>
		<div class="orderDetail-content-list">
			<div class="orderDetail-content-jichuxinxi", id = {{lender.get('id')}}>
				<div class="jichuxinxi-title">基本信息
					<div class="edit"></div>
					<input type="text" name="lender-id" style="display:none" value={{lender.get('id')}}>
				</div>
				<div class="clear"></div>
				<div class="jichuxinxi-info" style="width:90%;position:relative;height:130px;margin-left:8%;">
					<div>
						<div class="orderDetail-content-jichuxinxi-left">姓名:</div>
						<input name = "name" class="orderDetail-content-jichuxinxi-right" type="text" readonly="true" value={{lender.get('name')}}>
					</div>

					<div>
						<div class="orderDetail-content-jichuxinxi-left">家庭住址:</div>
						<input name = "familyaddr" class="orderDetail-content-jichuxinxi-right" type="text" readonly="true" value={{lender.get('family_addr')}}>
					</div>

					<div>
						<div class="orderDetail-content-jichuxinxi-left">电话:</div>
						<input name = "tel" class="orderDetail-content-jichuxinxi-right" type="text" readonly="true" value={{lender.get('tel')}}>
					</div>

					<div>
						<div class="orderDetail-content-jichuxinxi-left">家庭区域:</div>
						<input name = "familyarea" class="orderDetail-content-jichuxinxi-right" type="text" readonly="true" value={{lender.get('family_area')}}>
					</div>

					<div>
						<div class="orderDetail-content-jichuxinxi-left">身份证:</div>
						<input name = "idcard" class="orderDetail-content-jichuxinxi-right" type="text" readonly="true" value={{lender.get('idcard')}}>
					</div>

					<div>
						<div class="orderDetail-content-jichuxinxi-left">学校:</div>
						<input name = "univers" class="orderDetail-content-jichuxinxi-right" type="text" readonly="true" value={{lender.get('university')}}>
					</div>

					<div>
						<div class="orderDetail-content-jichuxinxi-left">学校区域:</div>
						<input name = "universarea" class="orderDetail-content-jichuxinxi-right" type="text" readonly="true" value={{lender.get('univers_area')}}>
					</div>
				</div>

				<div class="clear"></div>
				<div class="jichuxinxi-btn">
					<button class="btn-save">保存</button>
					<button class="btn-cancel">取消</button>
				</div>
			</div>
			%orderNo = {1:'一', 2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九',10:'十'}
			%orderStatus = {0:'已结清', 1:'联系本人', 2:'联系亲属',3:'联系同学',4:'失联',5:'待外访',6:'外访中',7:'承诺还款',8:'部分还款'}
			%orderIndex = 0
			%for order in orders:
			%orderIndex += 1
			<div class="orderDetail-content-orderStatus">
				<div class="orderStatus-title">
					订单{{orderNo.get(orderIndex)}}：<span>{{orderStatus.get(order.get('status'))}}</span>
					<input type="button" class="daochu">
					<input type="text" name="order-id" style="display:none" value={{order.get('id')}}>
				</div>
				<div class="orderStatus-info">
					<div class="status-edit"></div>
					<div class="orderStatus-content">
                        <div>
							<div class="orderStatus-content-left">订单编号:</div>
							<input name = "dispid" class="orderStatus-content-right" type="text" readonly="true" value={{order.get('disp_id')}}>
						</div>
						<div>
							<div class="orderStatus-content-left">订单状态:</div>
							<select name = "status_select" class="orderStatus-content-right"  disabled="disabled" type="text">
								<option value="0">已结清</option>
								<option value="1">联系本人</option>
								<option value="2">联系亲属</option>
								<option value="3">联系同学</option>
								<option value="4">失联</option>
								<option value="5">待外访</option>
								<option value="6">外访中</option>
								<option value="7">承诺还款</option>
								<option value="8">部分还款</option>
							</select>
							<input name = "status_value" style="display:none" type="text" readonly="true" value={{order.get('status')}}>
						</div>
						<div>
							<div class="orderStatus-content-left">订单来源:</div>
							<input name = "source" class="orderStatus-content-right" type="text" readonly="true" value={{order.get('source')}}>
						</div>
						<div>
							<div class="orderStatus-content-left">月供:</div>
							<input name = "monthpay" class="orderStatus-content-right" type="text" readonly="true" value={{order.get('month_pay')}}>
						</div>
						<div>
							<div class="orderStatus-content-left">账期:</div>
							<input name = "accountday" class="orderStatus-content-right" type="text" readonly="true" value={{order.get('account_day')}}>
						</div>
						<div>
							<div class="orderStatus-content-left">期数:</div>
							<input name = "periods" class="orderStatus-content-right" type="text" readonly="true" value={{order.get('periods')}}>
						</div>
						<div>
							<div class="orderStatus-content-left">产品名称:</div>
							<input name = "product" class="orderStatus-content-right" type="text" readonly="true" value={{order.get('product')}}> 
						</div>
						<div>
							<div class="orderStatus-content-left">已还期数:</div>
							<input name = "paidperiods" class="orderStatus-content-right" type="text" readonly="true" value={{order.get('paid_periods')}}>
						</div>
						<div>
							<div class="orderStatus-content-left">分期金额:</div>
							<input name = "amount" class="orderStatus-content-right" type="text" readonly="true" value={{order.get('amount')}}>
						</div>
						<div>
							<div class="orderStatus-content-left">订单日期:</div>
							<input name = "orderdate" class="orderStatus-content-right" type="text" readonly="true" value={{order.get('order_date')}}>
						</div>
						<div>
							<div class="orderStatus-content-left">滞纳金:</div>
							<input class="orderStatus-content-right" type="text" readonly="true" >
						</div>
						<div>
							<div class="orderStatus-content-left">接单日期:</div>
							<input name = "takeorderdate" class="orderStatus-content-right" type="text" readonly="true" value={{order.get('takeorder_date')}}>
						</div>
						<div>
							<div class="orderStatus-content-left">现总欠款:</div>
							<input class="orderStatus-content-right" type="text" readonly="true">
						</div>
						<div>
							<div class="orderStatus-content-left">已收金额:</div>
							<input name = "recvamount" class="orderStatus-content-right" type="text" readonly="true" value={{order.get('recv_amount')}}>
						</div>
					</div>
					<div class="orderStatus-btn">
						<button class="orderStatusbtn-save">保存</button>
						<button class="orderStatusbtn-cancel">取消</button>
					</div>
				</div>

				<div class="orderStatus-lianxiren">
					<div class="orderStatus-lianxiren-edit"></div>
					<div class="orderStatus-lianxiren-content">
						<div class="parents">
							<div style="width:50px;height:20px;line-height:20px;float:left">父母</div>
							<input name = "parent" class="parentsname" value={{order.get('parent')}} title="刘能中华人民共和国" readonly="true">
							<input name = "parentcall" class="parentsphone" value={{order.get('parent_call')}}>
							<a href="">张三</a><a href="">李四</a>
						</div>
						<div class="sheyou">
							<div style="width:50px;height:20px;line-height:20px;float:left">同寝</div>
							<input name = "roommate" class="sheyouname" value={{order.get('roommate')}} title="刘能中华人民共和国" readonly="true">
							<input name = "roommatecall" class="sheyouphone" value={{order.get('roommate_call')}}>
						</div>
						<div class="tongxue">
							<div style="width:50px;height:20px;line-height:20px;float:left">同学</div>
							<input name = "classmate" class="tongxuename" value={{order.get('classmate')}} title="刘能中华人民共和国" readonly="true">
							<input name = "classmatecall" class="tongxuephone" value={{order.get('classmate_call')}}>
						</div>
					</div>
					<div class="orderStatus-lianxiren-btn">
						<button class="lianxirenbtn-save">保存</button>
						<button class="lianxirenbtn-cancel">取消</button>
					</div>
				</div>
				<div class="orderStatus-upload-image">
					<div class="orderStatus-upload-image-list">
						<image class="orderStatus-image-thumb" src="../1.jpg">
						<image class="orderStatus-image-thumb" src="../2.png">
						<image class="orderStatus-image-thumb" src="../3.jpg">
						<image class="orderStatus-image-thumb" src="../4.jpg">
						<button>上传图片</button>
					</div>
				</div>
				<div class="orderStatus-upload-contract">
					<div class="orderStatus-upload-contract-list">
						<image class="orderStatus-contract-thumb" src="../word_icon.jpg">
						<image class="orderStatus-contract-thumb" src="../pdf_icon.png">
						<button>上传合同</button>
					</div>
				</div>
				<div class="orderStatus-upload-phonelist">
					<div class="orderStatus-upload-phonelist-list">
						<image class="orderStatus-phonelist-thumb" src="../excel_icon.png">
						<button>上传通话详单</button>
					</div>
				</div>
				<div class=""></div>
			</div>
			%end
		</div>
		<div class="orderDetail-content-right">
			<div class="orderDetail-content-right-top">
				<button class="addorderlist">添加订单</button>
			</div>
			<div class="orderDetail-content-caozuo">
				<div class="orderDetail-content-caozuo-title">操作记录
                    <div class="caozuo-title-edit"></div>
                </div>
				<ul class="caozuo-line">
					%for op in operations:
                    <li>
						<div class="width:80%;float:left;position:relative;margin-left:10%;">
							<div class="caozuo-time"><span class="caozuo-time-time">{{op.get('time')}}</span> <span class="caozuo-time-name">{{op.get('admin')}}</span></div>
                            <div class="caozuo-content" readonly="true">{{op.get('op_desc')}}</div>
						</div>

					</li>
					%end
				</ul>
			</div>
		</div>
		

	</div>

	</div>

</body>

</html>