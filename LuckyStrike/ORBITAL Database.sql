/*!40101 SET NAMES utf8mb4 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`LuckyStrike` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `LuckyStrike `;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `accounts`;

CREATE TABLE `accounts  ` (
  `user` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `credit` smallint NOT NULL,
  `small_prize` smallint NOT NULL,
  `big_prize` smallint NOT NULL,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `members` */

insert  into `accounts`(`user`,`password`,`credit`,`small_prize`,`big_prize `) values 

('jake','1234',`10`,`0`,`0`),

('nic','1234',`0`,`10`,`0`);


