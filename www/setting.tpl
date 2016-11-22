<html>

<head>
	<meta charset="UTF-8">
	<title>设置页面</title>
	<link rel="stylesheet" href="setting.css">
	<script src="jquery-1.11.1.min.js"></script>
	<script src="setting.js"></script>
</head>

<body>
	<div class="head">
		<div class="container">
			<ul class="head-user">
			<li><img src="icon_wp.png" style="height:16px;" alt=""><span>{{username}}</span></li>
			<li><img src="icon_tuichu.png" style="height:16px;" alt=""><span>退出</span></li>
		</ul>
		</div>
	</div>
	<div class="setting-list">
		<div class="setting-list-title">
			<div style="widdiv:3px;height:20px;background:#FF6600;float:left;margin-right:20px;"></div>设置页面</div>
		<div class="setting-list-content">
			<div class="wangpan-title">网盘设置
				<div class="edit"></div>
			</div>

			<div class="wangpan-content">
				<div>网盘账号：<input type="text" value={{account}} class="wangpanzhanghao" value="hahah"></div>
				<div>网盘密码：<input type="text" value={{password}} class="wangpanmima"></div>
				<div>备份时刻：<select name="" id="">
					<option value="">{{backuptime}}</option>
					<option value="">20:00</option>
                    <option value="">21:00</option>
                    <option value="">22:00</option>
                    <option value="">23:00</option>
                    <option value="">00:00</option>
                    <option value="">01:00</option>
                    <option value="">02:00</option>
                    <option value="">03:00</option>
                    <option value="">04:00</option>
                    <option value="">05:00</option>
                    <option value="">06:00</option>
                    </select></div>
			</div>
			<div class="wangpan-btn">
				<button class="wangpanbtn-save">保存</button>
				<button class="wangpanbtn-cancel">取消</button>
			</div>
		</div>

		<div class="setting-list-content">
			<div class="guanliyuan-title">管理员设置
				<div class="add">添加</div>
			</div>
			<table class="table-list" >
				<tr>
					<td>账号</td>
					<td>密码</td>
					<td>姓名</td>
					<td>操作</td>
				</tr>
				<tr>
					<td><input type="text" placeholder="请输入账号"></td>
					<td><input type="text" placeholder="请输入密码"></td>
					<td><input type="text" placeholder="请输入姓名"></td>
					<td><button class="delete">删除</button></td>
				</tr>

			</table>
			<div class="guanliyuan-btn">
				<button class="guanliyuanbtn-save">保存</button>
				<button class="guanliyuanbtn-cancel">取消</button>
			</div>
		

		</div>
	</div>
	<div class="userinfo" hidden>{{users}}</div>
</body>

</html>