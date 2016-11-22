var kkpager = {
		//divID
		pagerid : 'div_pager',
		//当前页码
		pno : 1,
		//总页码
		total : 1,
		//总数据条数
		totalRecords : 0,
		//是否显示总页数
		isShowTotalPage : true,
		//是否显示总记录数
		isShowTotalRecords : true,
		//是否显示页码跳转输入框
		isGoPage : true,
		
		//跳转框得到输入焦点时
		focus_gopage : function (){
			var btnGo = $('#btn_go');
			$('#btn_go_input').attr('hideFocus',true);
			btnGo.show();
			btnGo.css('left','0px');
			$('#go_page_wrap').css('border-color','#6694E3');
			btnGo.animate({left: '+=44'}, 50,function(){
				//$('#go_page_wrap').css('width','88px');
			});
		},
		
		//跳转框失去输入焦点时

		blur_gopage : function(){
			setTimeout(function(){
				var btnGo = $('#btn_go');
				//$('#go_page_wrap').css('width','44px');
				btnGo.animate({
				    left: '-=44'
				  }, 100, function() {
					  $('#btn_go').css('left','0px');
					  $('#btn_go').hide();
					  $('#go_page_wrap').css('border-color','#DFDFDF');
				  });
			},400);
		},
		//跳转框页面跳转
		gopage : function(){
			var str_page = $("#btn_go_input").val();
			if(isNaN(str_page)){
				$("#btn_go_input").val(this.next);
				return;
			}
			var n = parseInt(str_page);
			if(n < 1 || n >this.total){
				$("#btn_go_input").val(this.next);
				return;
			}
			//这里可以按需改window.open
			window.location = this.getLink(n);
		},
		//分页按钮控件初始化
		init : function(config){
			//赋值
			this.pno = isNaN(config.pno) ? 1 : parseInt(config.pno);
			this.total = isNaN(config.total) ? 1 : parseInt(config.total);
			this.totalRecords = isNaN(config.totalRecords) ? 0 : parseInt(config.totalRecords);
			if(config.pagerid){this.pagerid = pagerid;}
			if(config.isShowTotalPage != undefined){this.isShowTotalPage=config.isShowTotalPage;}
			if(config.isShowTotalRecords != undefined){this.isShowTotalRecords=config.isShowTotalRecords;}
			if(config.isGoPage != undefined){this.isGoPage=config.isGoPage;}
			this.hrefFormer = config.hrefFormer || '';
			this.hrefLatter = config.hrefLatter || '';
			if(config.getLink && typeof(config.getLink) == 'function'){this.getLink = config.getLink;}
			//验证
			if(this.pno < 1) this.pno = 1;
			this.total = (this.total <= 1) ? 1: this.total;
			if(this.pno > this.total) this.pno = this.total;
			this.prv = (this.pno<=2) ? 1 : (this.pno-1);
			this.next = (this.pno >= this.total-1) ? this.total : (this.pno + 1);
			this.hasPrv = (this.pno > 1);
			this.hasNext = (this.pno < this.total);
			
			this.inited = true;
		},
		//生成分页控件Html
		generPageHtml : function(){
			if(!this.inited){
				return;
			}
			
			var str_prv='',str_next='';
			if(this.hasPrv){
				str_prv = '<button class="toreturn" onclick="getLink('+this.prv+')" id="prevPage">上一页</button>';
			}else{
				str_prv = '<button class="curr disabled" onclick="getLink('+this.prv+')" disabled="disabled" id="prevPage">上一页</button>';
			}
			
			if(this.hasNext){
				str_next = '<button class="toreturn" onclick="getLink('+this.next+')" id="nextPage">下一页</button>';
			}else{
				str_next = '<button class="curr disabled" disabled="disabled" id="nextPage">下一页</button>';
			}
			
			
			var str = '';
			var dot = '<span>...</span>';
			var total_info='';
			if(this.isShowTotalPage || this.isShowTotalRecords){
				total_info = '<span class="normalsize">共';
				if(this.isShowTotalPage){
					total_info += this.total+'页';
					if(this.isShowTotalRecords){
						total_info += '&nbsp;/&nbsp;';
					}
				}
				if(this.isShowTotalRecords){
					total_info += this.totalRecords+'条数据';
				}
				
				total_info += '</span>';
			}
			
			var gopage_info = '';
			if(this.isGoPage){
				gopage_info = '&nbsp;转到<span id="go_page_wrap" style="display:inline-block;width:44px;height:18px;border:1px solid #DFDFDF;margin:0px 1px;padding:0px;position:relative;left:0px;top:5px;">'+
					'<input type="button" id="btn_go" style="width:44px;height:20px;line-height:20px;padding:0px;font-family:arial,宋体,sans-serif;text-align:center;border:0px;background-color:#0063DC;color:#FFF;position:absolute;left:0px;top:-1px;display:none;" value="确定" />'+
					'<input type="text" id="btn_go_input" onfocus="kkpager.focus_gopage()" onkeypress="if(event.keyCode<48 || event.keyCode>57)return false;" onblur="kkpager.blur_gopage()" style="width:42px;height:16px;text-align:center;border:0px;position:absolute;left:0px;top:0px;outline:none;" value="'+this.next+'" /></span>页';
			}
			
			//分页处理
			if(this.total <= 8){
				for(var i=1;i<=this.total;i++){
					if(this.pno == i){
						str += '<button class="curr" onclick="getLink('+i+')" value="'+i+'">'+i+'</button>';
					}else{
						str += '<button class="toreturn"  onclick="getLink('+i+')" value="'+i+'">'+i+'</button>';
					}
				}
			}else{
				if(this.pno <= 5){
					for(var i=1;i<=7;i++){
						if(this.pno == i){
							str += '<button class="curr" onclick="getLink('+i+')" value="'+i+'">'+i+'</button>';
						}else{
							str += '<button class="toreturn"  onclick="getLink('+i+')" value="'+i+'">'+i+'</button>';
						}
					}
					str += dot;
				}else{
					str += '<button class="toreturn"  onclick="getLink(1)" value="1">1</button>';
					str += '<button class="toreturn"  onclick="getLink(2)" value="2">2</button>';
					str += dot;
					
					var begin = this.pno - 2;
					var end = this.pno + 2;
					if(end > this.total){
						end = this.total;
						begin = end - 4;
						if(this.pno - begin < 2){
							begin = begin-1;
						}
					}else if(end + 1 == this.total){
						end = this.total;
					}
					for(var i=begin;i<=end;i++){
						if(this.pno == i){
						}else{
							str += '<button class="toreturn" onclick="getLink('+i+')" value="'+i+'">'+i+'</button>';
						}
					}
					if(end != this.total){
						str += dot;
					}
				}
			}
			
			str = "&nbsp;"+str_prv + str + str_next  + total_info + gopage_info;
			$("#"+this.pagerid).html(str);
		}
};