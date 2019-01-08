/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : localhost
 Source Database       : dunning

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : utf-8

 Date: 01/08/2019 18:03:05 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `admin`
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `enable` int(11) DEFAULT NULL,
  `is_admin` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `passwd` varchar(20) NOT NULL,
  `user` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `admin`
-- ----------------------------
BEGIN;
INSERT INTO `admin` VALUES ('1', '1', '1', 'admin', 'admin', 'admin');
COMMIT;

-- ----------------------------
--  Table structure for `files`
-- ----------------------------
DROP TABLE IF EXISTS `files`;
CREATE TABLE `files` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) DEFAULT NULL,
  `path` varchar(200) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `files_order_id` (`order_id`),
  CONSTRAINT `files_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `lender`
-- ----------------------------
DROP TABLE IF EXISTS `lender`;
CREATE TABLE `lender` (
  `family_addr` varchar(200) DEFAULT NULL,
  `family_area` varchar(100) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `idcard_id` varchar(255) NOT NULL,
  `is_del` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `tel` varchar(11) NOT NULL,
  `univers_area` varchar(100) DEFAULT NULL,
  `university` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`,`idcard_id`),
  UNIQUE KEY `lender_id_idcard_id` (`id`,`idcard_id`),
  KEY `lender_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `operation`
-- ----------------------------
DROP TABLE IF EXISTS `operation`;
CREATE TABLE `operation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) DEFAULT NULL,
  `after_status` int(11) DEFAULT NULL,
  `before_status` int(11) DEFAULT NULL,
  `files` varchar(200) DEFAULT NULL,
  `is_change_status` int(11) DEFAULT NULL,
  `is_upload` int(11) DEFAULT NULL,
  `lender_id` int(11) DEFAULT NULL,
  `op_desc` varchar(300) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_admin_id` (`admin_id`),
  KEY `operation_lender_id` (`lender_id`),
  CONSTRAINT `operation_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`) ON DELETE CASCADE,
  CONSTRAINT `operation_ibfk_2` FOREIGN KEY (`lender_id`) REFERENCES `lender` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `orders`
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_day` varchar(50) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `call_details` varchar(100) DEFAULT NULL,
  `classmate` varchar(20) DEFAULT NULL,
  `classmate_call` varchar(20) DEFAULT NULL,
  `contract` varchar(100) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `disp_id` varchar(100) DEFAULT NULL,
  `is_del` int(11) DEFAULT NULL,
  `lender_id` int(11) DEFAULT NULL,
  `lender_pic` varchar(100) DEFAULT NULL,
  `modify_time` datetime DEFAULT NULL,
  `month_pay` float DEFAULT NULL,
  `order_date` date DEFAULT NULL,
  `paid_periods` int(11) DEFAULT NULL,
  `parent` varchar(100) DEFAULT NULL,
  `parent_call` varchar(100) DEFAULT NULL,
  `payment_day` varchar(100) DEFAULT NULL,
  `periods` int(11) DEFAULT NULL,
  `product` varchar(100) DEFAULT NULL,
  `received_amount` float DEFAULT NULL,
  `roommate` varchar(100) DEFAULT NULL,
  `roommate_call` varchar(100) DEFAULT NULL,
  `source` varchar(100) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `takeorder_data` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_lender_id` (`lender_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`lender_id`) REFERENCES `lender` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `system`
-- ----------------------------
DROP TABLE IF EXISTS `system`;
CREATE TABLE `system` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `backuptime` time DEFAULT NULL,
  `intval` int(11) DEFAULT NULL,
  `passwd` varchar(20) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
