CREATE DATABASE IF NOT EXISTS `python` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `python`;

CREATE TABLE IF NOT EXISTS `newscontent` (
  `no` int(20) NOT NULL AUTO_INCREMENT,
  `newsTitle` varchar(255) DEFAULT NULL,
  `newsDate` varchar(255) DEFAULT NULL,
  `newsKind` varchar(255) DEFAULT NULL,
  `newsContent` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`no`)
) 
