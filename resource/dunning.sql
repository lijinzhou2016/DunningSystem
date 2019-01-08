/*
Navicat MySQL Data Transfer

Source Server         : dunning
Source Server Version : 50624
Source Host           : localhost:3306
Source Database       : dunning

Target Server Type    : MYSQL
Target Server Version : 50624
File Encoding         : 65001

Date: 2016-12-21 12:41:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(255) NOT NULL DEFAULT '登录用户名',
  `name` varchar(255) NOT NULL COMMENT '管理员姓名',
  `passwd` varchar(255) NOT NULL COMMENT '密码',
  `is_admin` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否管理员',
  `enable` tinyint(4) DEFAULT NULL COMMENT '是否禁用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for files
-- ----------------------------
DROP TABLE IF EXISTS `files`;
CREATE TABLE `files` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) DEFAULT NULL,
  `path` varchar(255) DEFAULT NULL,
  `time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `type` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `file_order_id` (`order_id`),
  CONSTRAINT `file_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for lender
-- ----------------------------
DROP TABLE IF EXISTS `lender`;
CREATE TABLE `lender` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idcard_id` varchar(255) NOT NULL DEFAULT '' COMMENT '身份证号',
  `name` varchar(255) NOT NULL COMMENT '姓名',
  `tel` varchar(255) DEFAULT NULL COMMENT '电话',
  `university` varchar(255) DEFAULT NULL COMMENT '学校',
  `univers_area` varchar(255) DEFAULT NULL COMMENT '学校区域',
  `family_addr` varchar(255) DEFAULT NULL COMMENT '家庭住址',
  `family_area` varchar(255) DEFAULT NULL COMMENT '家庭住址区域',
  `is_del` tinyint(4) NOT NULL COMMENT '删除标志位',
  PRIMARY KEY (`id`,`idcard_id`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for operation
-- ----------------------------
DROP TABLE IF EXISTS `operation`;
CREATE TABLE `operation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lender_id` int(11) DEFAULT NULL,
  `admin_id` int(11) DEFAULT NULL COMMENT '操作的管理员ID',
  `op_desc` varchar(255) DEFAULT '',
  `is_change_status` tinyint(4) DEFAULT NULL COMMENT '是否修改订单状态',
  `before_status` int(11) DEFAULT NULL COMMENT '修改前的状态',
  `after_status` int(11) DEFAULT NULL COMMENT '修改后的状态',
  `is_upload` tinyint(4) DEFAULT NULL COMMENT '是否上传文件',
  `files` varchar(255) DEFAULT '' COMMENT '上传文件名称',
  `time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '操作的时间戳',
  PRIMARY KEY (`id`),
  KEY `operation_user_id_fkey` (`admin_id`),
  KEY `operation_lender_id_fkey` (`lender_id`),
  CONSTRAINT `operation_lender_id_fkey` FOREIGN KEY (`lender_id`) REFERENCES `lender` (`id`),
  CONSTRAINT `operation_user_id_fkey` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '订单id',
  `disp_id` varchar(255) DEFAULT '' COMMENT '显示id',
  `source` varchar(255) DEFAULT '' COMMENT '订单来源',
  `lender_id` int(11) NOT NULL COMMENT '贷款人id',
  `account_day` varchar(255) DEFAULT '' COMMENT '账期？？ 啥意思',
  `product` varchar(255) DEFAULT '' COMMENT '产品名称',
  `amount` double(11,2) DEFAULT '0.00' COMMENT '分期金额（总额）',
  `month_pay` double(11,2) DEFAULT '0.00' COMMENT '每期金额，月供',
  `periods` int(11) DEFAULT '0' COMMENT '期数--通过总额和期数计算月供',
  `paid_periods` int(255) DEFAULT '0' COMMENT '已付期数',
  `received_amount` double(11,2) DEFAULT '0.00' COMMENT '已收金额',
  `order_date` date DEFAULT NULL COMMENT '订单日期',
  `takeorder_data` date DEFAULT NULL COMMENT '接单日期',
  `call_details` varchar(255) DEFAULT '' COMMENT '通话详单文件存放路径',
  `contract` varchar(255) DEFAULT '' COMMENT '合同文件路径',
  `lender_pic` varchar(255) DEFAULT '' COMMENT '借款人信息图片路径，多个文件以分号相隔',
  `parent` varchar(255) DEFAULT '' COMMENT '父母联系人',
  `parent_call` varchar(255) DEFAULT '',
  `roommate` varchar(255) DEFAULT '' COMMENT '室友',
  `roommate_call` varchar(255) DEFAULT '',
  `classmate` varchar(255) DEFAULT '' COMMENT '同学',
  `classmate_call` varchar(255) DEFAULT '',
  `status` int(11) DEFAULT NULL COMMENT '订单状态（联系本人、联系亲属、联系同学、失联、待外访、外访中、承诺还款、部分还款、已结清）',
  `payment_day` varchar(255) DEFAULT '',
  `create_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `modify_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `is_del` tinyint(4) DEFAULT '0' COMMENT '删除标志位',
  PRIMARY KEY (`id`),
  KEY `orders_lender_id_fkey` (`lender_id`),
  CONSTRAINT `orders_lender_id_fkey` FOREIGN KEY (`lender_id`) REFERENCES `lender` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for system
-- ----------------------------
DROP TABLE IF EXISTS `system`;
CREATE TABLE `system` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL COMMENT '网盘用户名',
  `passwd` varchar(255) DEFAULT NULL COMMENT '网盘密码',
  `backuptime` time DEFAULT NULL COMMENT '备份时间',
  `intval` int(11) DEFAULT NULL COMMENT '间隔天数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
