-- MySQL dump 10.13  Distrib 5.7.16, for osx10.11 (x86_64)
--
-- Host: localhost    Database: meas_development
-- ------------------------------------------------------
-- Server version	5.7.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add Token',7,'add_token'),(20,'Can change Token',7,'change_token'),(21,'Can delete Token',7,'delete_token'),(22,'Can add test',8,'add_test'),(23,'Can change test',8,'change_test'),(24,'Can delete test',8,'delete_test'),(25,'Can add key point',9,'add_keypoint'),(26,'Can change key point',9,'change_keypoint'),(27,'Can delete key point',9,'delete_keypoint'),(28,'Can add education level',10,'add_educationlevel'),(29,'Can change education level',10,'change_educationlevel'),(30,'Can delete education level',10,'delete_educationlevel'),(31,'Can add subject',11,'add_subject'),(32,'Can change subject',11,'change_subject'),(33,'Can delete subject',11,'delete_subject'),(34,'Can add paper',12,'add_paper'),(35,'Can change paper',12,'change_paper'),(36,'Can delete paper',12,'delete_paper'),(37,'Can add topic',13,'add_topic'),(38,'Can change topic',13,'change_topic'),(39,'Can delete topic',13,'delete_topic'),(40,'Can add concept',14,'add_concept'),(41,'Can change concept',14,'change_concept'),(42,'Can delete concept',14,'delete_concept'),(43,'Can add question',15,'add_question'),(44,'Can change question',15,'change_question'),(45,'Can delete question',15,'delete_question'),(49,'Can add answer part',17,'add_answerpart'),(50,'Can change answer part',17,'change_answerpart'),(51,'Can delete answer part',17,'delete_answerpart'),(52,'Can add formula',18,'add_formula'),(53,'Can change formula',18,'change_formula'),(54,'Can delete formula',18,'delete_formula'),(55,'Can add formula index',19,'add_formulaindex'),(56,'Can change formula index',19,'change_formulaindex'),(57,'Can delete formula index',19,'delete_formulaindex');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (2,'pbkdf2_sha256$30000$ANtUOB7gaide$TuqYJupPndENNdXfsa7CI5d53LUUb1cjEUVh/jeTP90=','2016-11-21 02:23:40.115313',0,'phucls_student','Phuc','123','sple@ntu.edu.vn',0,1,'2016-11-20 13:25:49.487489'),(6,'pbkdf2_sha256$30000$wj3tET1FQ1PM$P7Lrlp8McUVd+aKAqIk6Grql7x+QTMjSftbKQYB0UQo=','2016-12-28 03:22:20.619835',1,'kokseong','','','test@example.com',1,1,'2016-11-21 03:11:27.040837'),(10,'pbkdf2_sha256$30000$4PJdwRm5rk3b$27HYMKzIDVWd+0ob38Xz6e9BLVbQ+bBNAU1BLjtBmuM=','2017-01-09 14:00:12.967613',1,'edward','','','',1,1,'2016-12-07 06:55:54.543778'),(11,'pbkdf2_sha256$30000$qYD7kDCJCF7Y$WachHu9BK6qXDCqQuuVp0W+rsoJA+hOZSw5dcM28uYA=','2016-12-09 19:41:37.565924',0,'michael','michael','michael','michaelj003@e.ntu.edu.sg',0,1,'2016-12-09 19:41:37.476299'),(12,'pbkdf2_sha256$30000$h3G7QiTEUjZc$/4Svypcfv4B+UeYaH2pd2RQUMI2OgtO1oaCXuni27cg=','2017-01-12 01:23:03.303494',1,'phucls','','','phucls288@gmail.com',1,1,'2017-01-12 01:04:49.097406'),(13,'pbkdf2_sha256$30000$PrM2k2vZEODr$4PqCI2b6O1AGKq44HvIPjTRAm0faSx0Wfnw0N58gymg=','2017-01-16 00:07:17.701260',1,'dekauliya','','','deka0001@e.ntu.edu.sg',1,1,'2017-01-12 01:06:08.668396');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(4,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(7,'authtoken','token'),(5,'contenttypes','contenttype'),(17,'meas_models','answerpart'),(14,'meas_models','concept'),(10,'meas_models','educationlevel'),(18,'meas_models','formula'),(19,'meas_models','formulaindex'),(9,'meas_models','keypoint'),(12,'meas_models','paper'),(15,'meas_models','question'),(11,'meas_models','subject'),(8,'meas_models','test'),(13,'meas_models','topic'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-11-20 13:23:19.346142'),(2,'auth','0001_initial','2016-11-20 13:23:19.595759'),(3,'admin','0001_initial','2016-11-20 13:23:19.661267'),(4,'admin','0002_logentry_remove_auto_add','2016-11-20 13:23:19.705221'),(5,'contenttypes','0002_remove_content_type_name','2016-11-20 13:23:19.775051'),(6,'auth','0002_alter_permission_name_max_length','2016-11-20 13:23:19.792993'),(7,'auth','0003_alter_user_email_max_length','2016-11-20 13:23:19.810308'),(8,'auth','0004_alter_user_username_opts','2016-11-20 13:23:19.826220'),(9,'auth','0005_alter_user_last_login_null','2016-11-20 13:23:19.860305'),(10,'auth','0006_require_contenttypes_0002','2016-11-20 13:23:19.863046'),(11,'auth','0007_alter_validators_add_error_messages','2016-11-20 13:23:19.876140'),(12,'auth','0008_alter_user_username_max_length','2016-11-20 13:23:19.901207'),(13,'authtoken','0001_initial','2016-11-20 13:23:19.955172'),(14,'authtoken','0002_auto_20160226_1747','2016-11-20 13:23:20.042317'),(16,'sessions','0001_initial','2016-11-20 13:23:20.516399'),(32,'meas_models','0001_initial','2017-01-17 18:03:34.958528'),(33,'meas_models','0002_auto_20161123_2101','2017-01-17 18:03:34.982262'),(34,'meas_models','0003_auto_20161124_1428','2017-01-17 18:03:34.987064'),(35,'meas_models','0004_auto_20161124_1522','2017-01-17 18:03:34.990316'),(36,'meas_models','0005_auto_20161130_1328','2017-01-17 18:03:34.992325'),(37,'meas_models','0006_paper_subject','2017-01-17 18:03:34.996226'),(38,'meas_models','0007_concept_order','2017-01-17 18:03:34.999433'),(39,'meas_models','0008_formula','2017-01-17 18:03:35.001425'),(40,'meas_models','0009_question_formulas','2017-01-17 18:03:35.003399'),(41,'meas_models','0010_remove_question_source','2017-01-17 18:03:35.005262'),(42,'meas_models','0011_auto_20170115_2135','2017-01-17 18:03:35.006970'),(43,'meas_models','0012_formula_formula','2017-01-17 18:03:35.008785'),(44,'meas_models','0013_auto_20170116_2251','2017-01-17 18:03:35.010649'),(45,'meas_models','0014_auto_20170117_1646','2017-01-17 18:03:35.012457'),(46,'meas_models','0015_auto_20170117_1721','2017-01-17 18:03:35.015786'),(47,'meas_models','0016_auto_20170117_2325','2017-01-17 18:03:35.019145'),(48,'meas_models','0001_squashed_0016_auto_20170117_2325','2017-01-17 18:03:35.024196'),(49,'meas_models','0002_remove_formula_question','2017-01-17 18:26:57.104365'),(50,'meas_models','0003_formula_question','2017-01-17 18:26:57.221344'),(51,'meas_models','0004_formulaindex_idf','2017-01-18 11:21:54.302573'),(52,'meas_models','0005_auto_20170118_1923','2017-01-18 11:23:08.104529'),(53,'meas_models','0006_remove_formulaindex_idf','2017-01-18 11:26:01.427214');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0i1c022sy1w3fyxqu5pem9a63vibtp5v','ZGIzMWExMzU2MTIxMWMzNjU3Y2E1YjQ3M2ZiNmVkNGE1YTRhMjgyNDp7Il9hdXRoX3VzZXJfaGFzaCI6IjE5MDY4MjE3MjBlZmJkZjc1NmJjMzY3MDc0ZDE1OWNlYWNiOGU5YzYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMCJ9','2017-01-23 14:00:12.970352'),('14nd43r8sau5f1lbosgxig2xdkoeptuh','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-01-17 12:45:32.917057'),('1bpyiq79p0s04s2iljz9xr7ks1pnp092','ZTIyNDg4MTY5YjQ4YjU5N2YzODc4NzUxMjcyZTY2YzMxZjViNjIxMzp7Il9hdXRoX3VzZXJfaGFzaCI6IjFlNDNiYmViMTY0Zjk1MGQ4NTM4NzY2OWIxYmJkNDMzNzBkMTMzMDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI2In0=','2016-12-21 06:24:53.620214'),('1z97iutkkg2sc6hgjyff91wpavkm88i9','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-08 08:00:48.547279'),('3643mqqbt333vrotbxr440z3p15klx6e','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-01-17 02:39:47.309580'),('3fxae7ad96jik70np4jxs2rg1lcd91g2','NDE1ZjQ2OWI4ODg1NDRmYjFhOWU3MTI3MjZiYmY0NTMwM2E3NmZhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjgzNGJkNmJlNjVmMjllNmQyMGM3NWJjMzljNzQwN2Y3ZTczZWYzYzIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMyJ9','2017-01-26 01:06:21.203820'),('4wfvqu5jchwmi42te52mbrzb61ua66id','NDE1ZjQ2OWI4ODg1NDRmYjFhOWU3MTI3MjZiYmY0NTMwM2E3NmZhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjgzNGJkNmJlNjVmMjllNmQyMGM3NWJjMzljNzQwN2Y3ZTczZWYzYzIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMyJ9','2017-01-27 16:20:03.421823'),('62ntrn0hakefmsvk0garcqf2j0h6g5hz','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-01-05 04:38:11.471841'),('7wlnei08zk9niouytlibygdtapirpymr','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-05 02:18:55.075267'),('8pko6meflo9cjgt7vjso4pcldonlgwq7','ZTIyNDg4MTY5YjQ4YjU5N2YzODc4NzUxMjcyZTY2YzMxZjViNjIxMzp7Il9hdXRoX3VzZXJfaGFzaCI6IjFlNDNiYmViMTY0Zjk1MGQ4NTM4NzY2OWIxYmJkNDMzNzBkMTMzMDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI2In0=','2017-01-11 03:22:20.622229'),('azuk7oj3d809il814c8sjxppanxmt6i7','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-05 02:53:44.949953'),('bs2ytyo97cwpqbn2xk2dco82riwludnc','ZTIyNDg4MTY5YjQ4YjU5N2YzODc4NzUxMjcyZTY2YzMxZjViNjIxMzp7Il9hdXRoX3VzZXJfaGFzaCI6IjFlNDNiYmViMTY0Zjk1MGQ4NTM4NzY2OWIxYmJkNDMzNzBkMTMzMDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI2In0=','2016-12-05 03:11:37.323585'),('bsw757pk9v4j5fdogr91whsdc01isrt5','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-20 03:20:19.458155'),('caph5cdfe5visyjip5fonzwbgnmm83x7','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-20 06:07:58.847443'),('cjflgox566bkexm1ilanegqt5k6b57hf','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-20 06:22:04.447159'),('czj3xklu2b4sukyyj64v9rdtumhqn8e1','MmIyMTk5M2Y0ZWQ4YjQ2OTFiMDM2ODBjOTY3NTk3NjY0YWU4ZTJhZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjZhZjM1MGI3Zjg2NzU1YTI2MDk2ZGJkZjI4YWIwYzkwMjcxNTgxYWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMSJ9','2016-12-23 19:41:37.577947'),('g4ec0mu03hnwkc1cf2yenomw1syarf9d','YjUzZjJkZTA0NjYzYWRjNGI5NTY0YzAwMTc5MTA1MmZmMzYxNjUwMzp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ2YjRiMDJhZmJhYzMwNTU0MTMyOTNiNDZjOGM0ZjBjMjI1MzEzNTEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMiJ9','2017-01-26 01:23:03.306153'),('g6fgmwr0ndqfvsoc6x76ixmvgrkh709h','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-22 00:38:44.361212'),('iteba90lntqg9h78jhtyewe1qllfwllb','ZTIyNDg4MTY5YjQ4YjU5N2YzODc4NzUxMjcyZTY2YzMxZjViNjIxMzp7Il9hdXRoX3VzZXJfaGFzaCI6IjFlNDNiYmViMTY0Zjk1MGQ4NTM4NzY2OWIxYmJkNDMzNzBkMTMzMDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI2In0=','2016-12-05 08:46:29.527091'),('iut6dnxqqxhp7puiur3jggtwc2abqcxs','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-01-03 08:43:01.840387'),('l3dwuvz0foehq056kh9bw4ooyv4swkm2','ZTIyNDg4MTY5YjQ4YjU5N2YzODc4NzUxMjcyZTY2YzMxZjViNjIxMzp7Il9hdXRoX3VzZXJfaGFzaCI6IjFlNDNiYmViMTY0Zjk1MGQ4NTM4NzY2OWIxYmJkNDMzNzBkMTMzMDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI2In0=','2016-12-05 08:07:17.378883'),('md4hmsk14lviffvjnlb8gpja9ktb9xeq','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-20 10:49:06.029985'),('oyzp5744zxz3tq3hwh4k6kbqhc9mb3lm','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-14 10:33:25.939498'),('pqi7rabpur83i8y324k5i77dycza4mg5','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-05 02:59:56.231822'),('rklzj3ifb3r0m548pt4xwj9j8l6dil89','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-15 01:49:59.804648'),('tzwgm86eusessq82az3b5bwdsq8el21w','OGZhZDJmMTM0YjA0MmVhYzAyOTY5ODIzNjczMGI1NTU4MTRjNjQxMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFlNDNiYmViMTY0Zjk1MGQ4NTM4NzY2OWIxYmJkNDMzNzBkMTMzMDMiLCJfYXV0aF91c2VyX2lkIjoiNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-12-23 02:43:23.023382'),('u3uart2796xjfp6barsogv5rk8w9q6oo','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-26 08:01:33.319031'),('wcr1n9b71nuqbuufwx325cd3teucjb1s','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-26 05:39:07.481715'),('wh2gjztgzlnbt5m3hi6v1ktnabzo7x8q','ZGIzMWExMzU2MTIxMWMzNjU3Y2E1YjQ3M2ZiNmVkNGE1YTRhMjgyNDp7Il9hdXRoX3VzZXJfaGFzaCI6IjE5MDY4MjE3MjBlZmJkZjc1NmJjMzY3MDc0ZDE1OWNlYWNiOGU5YzYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMCJ9','2016-12-27 06:45:55.902362'),('wi3yfokhl6sk30eukdspxi4z0tnjkgp2','ZTI2N2Q3N2M1NWRhOTgwYzIwMzA5OTQ2NjBkN2IzNWRkMmVhOTEyODp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzYmM0NjM1MjM5OTg0ODBkNDhjMmJjNzFhNmViOWIxMGU1MGI1Y2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-12-04 13:24:40.046267'),('wxbzt7l2q7o8de7a8wizv1f2phh2jc33','NDE1ZjQ2OWI4ODg1NDRmYjFhOWU3MTI3MjZiYmY0NTMwM2E3NmZhYjp7Il9hdXRoX3VzZXJfaGFzaCI6IjgzNGJkNmJlNjVmMjllNmQyMGM3NWJjMzljNzQwN2Y3ZTczZWYzYzIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMyJ9','2017-01-26 01:58:08.914146');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meas_models_answerpart`
--

DROP TABLE IF EXISTS `meas_models_answerpart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meas_models_answerpart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `part_name` varchar(1) NOT NULL,
  `part_content` longtext NOT NULL,
  `part_respone_type` varchar(10) NOT NULL,
  `question_id` int(11) NOT NULL,
  `respone_type_1` varchar(10) DEFAULT NULL,
  `respone_type_2` varchar(10) DEFAULT NULL,
  `respone_type_3` varchar(10) DEFAULT NULL,
  `respone_type_4` varchar(10) DEFAULT NULL,
  `subpart_content_1` longtext,
  `subpart_content_2` longtext,
  `subpart_content_3` longtext,
  `subpart_content_4` longtext,
  `subpart_name_1` varchar(10) DEFAULT NULL,
  `subpart_name_2` varchar(10) DEFAULT NULL,
  `subpart_name_3` varchar(10) DEFAULT NULL,
  `subpart_name_4` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `meas_models_answerpart_7aa0f6ee` (`question_id`),
  CONSTRAINT `meas_models_answ_question_id_ca7898a1_fk_meas_models_question_id` FOREIGN KEY (`question_id`) REFERENCES `meas_models_question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meas_models_answerpart`
--

LOCK TABLES `meas_models_answerpart` WRITE;
/*!40000 ALTER TABLE `meas_models_answerpart` DISABLE KEYS */;
INSERT INTO `meas_models_answerpart` VALUES (1,'a','eaw','Numberic',47,'12321','Numberic','Text','Text','12321','ewa','23231','312413','i','ii','iii','iv'),(2,'a','1,2','Numberic',48,'Numberic','Numberic','Text','EXPRESSION','a = 12 or b = 123','123','$x^2$','$\\frac{2x}{5x^2}','i','ii','iii','iv'),(3,'b','eawe','Numberic',48,'Text','Text','Text','Text',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,'c','eawe','Numberic',48,'Text','Text','Text','Text',NULL,NULL,'asdfasf',NULL,NULL,NULL,'iii',NULL),(5,'a','2','Numberic',15,'Sketch','Text','Text','Text','tsret',NULL,NULL,NULL,'i',NULL,NULL,NULL),(6,'b','-11','Numberic',15,'Text','Text','Text','Text',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(7,'a','2,4 or -2, 0, k =8','Numberic',17,'Text','Text','Text','Text',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(8,'a','wqeq','Numberic',21,'Text','Text','Text','Text',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(9,'b','1231','Numberic',21,'Text','Text','Text','Text',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(10,'c','weawe','Numberic',21,'Text','Text','Text','Text',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(15,'a','123','Numberic',53,'Numberic','Numberic','Numberic','Numberic','123','123','123','123','i','ii','iii','iv');
/*!40000 ALTER TABLE `meas_models_answerpart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meas_models_concept`
--

DROP TABLE IF EXISTS `meas_models_concept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meas_models_concept` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `topic_id` int(11) NOT NULL,
  `order` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `meas_models_concept_19b4d727` (`topic_id`),
  CONSTRAINT `meas_models_concept_topic_id_eac03a60_fk_meas_models_topic_id` FOREIGN KEY (`topic_id`) REFERENCES `meas_models_topic` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meas_models_concept`
--

LOCK TABLES `meas_models_concept` WRITE;
/*!40000 ALTER TABLE `meas_models_concept` DISABLE KEYS */;
INSERT INTO `meas_models_concept` VALUES (2,'Linear Law','Linear Law',6,1),(3,'Simple Coordinate Geometry','Simple Coordinate Geometry',6,1),(4,'Double angle formula','Double angle formula',8,1),(5,'Differentiation Techniques','Differentiation Techniques',10,1),(6,'Rates of change','Rates of change',10,1),(11,'test','test',1,1),(17,'Roots of Quadratic Equations','Sum of roots and product of roots of a quadratic equation',1,1),(18,'Nature of roots of Quadratic Equations','Discriminant = $b^2-4ac$',1,1),(19,'Quadratic expression is always positive or negative','$ax^2+bx+c$ is always positive or negative',1,1),(20,'Straight line and curve','Intersection problem leading to Quadratic Equations',1,1),(21,'Power rule','$y=ax^n$\r\n$\\frac{dy}{dx}=anx^{n-1}$\r\n',10,1),(23,'Basic Trigonometric Identities','Basic Identities',9,1),(24,'Angle-Sum and Angle-Difference Identities','Addition Formulae',9,3),(25,'Double Angle Formulae','Double Angle Formulae',9,1),(26,'R-Formulae','R-Formulae',9,1);
/*!40000 ALTER TABLE `meas_models_concept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meas_models_educationlevel`
--

DROP TABLE IF EXISTS `meas_models_educationlevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meas_models_educationlevel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meas_models_educationlevel`
--

LOCK TABLES `meas_models_educationlevel` WRITE;
/*!40000 ALTER TABLE `meas_models_educationlevel` DISABLE KEYS */;
INSERT INTO `meas_models_educationlevel` VALUES (1,'A\'level','Covers subjects in Junior College'),(2,'O\'level','Covers subjects in Secondary School'),(3,'Elementary','Covers subjects in Primary School');
/*!40000 ALTER TABLE `meas_models_educationlevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meas_models_formula`
--

DROP TABLE IF EXISTS `meas_models_formula`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meas_models_formula` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `constant_term` varchar(1024) DEFAULT NULL,
  `inorder_term` varchar(1024) DEFAULT NULL,
  `sorted_term` varchar(1024) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `structure_term` varchar(1024) DEFAULT NULL,
  `variable_term` varchar(1024) DEFAULT NULL,
  `question_id` int(11),
  PRIMARY KEY (`id`),
  KEY `meas_models_formula_7aa0f6ee` (`question_id`),
  CONSTRAINT `meas_models_form_question_id_754da866_fk_meas_models_question_id` FOREIGN KEY (`question_id`) REFERENCES `meas_models_question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1246 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meas_models_formula`
--

LOCK TABLES `meas_models_formula` WRITE;
/*!40000 ALTER TABLE `meas_models_formula` DISABLE KEYS */;
INSERT INTO `meas_models_formula` VALUES (1133,'a \\ne 0','[\'cn\']','[[], [], []]','[[], [], [], [u\'\\u2260\']]',1,'[]','[\'var\']',4),(1134,'x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}.','[\'mrow$msqrt$mrow$cn\', \'mrow$cn\', \'mrow$msqrt$mrow$msup$cn\']','[[u\'=$\\u2212$msqrt$msup\', u\'\\u2212$msqrt$msup$\\u2212\', u\'msqrt$msup$\\u2212$.\'], [u\'=$\\u2212$msqrt\', u\'\\u2212$msqrt$msup\', u\'msqrt$msup$\\u2212\', u\'msup$\\u2212$.\'], [u\'=$\\u2212\', u\'\\u2212$msqrt\', \'msqrt$msup\', u\'msup$\\u2212\', u\'\\u2212$.\']]','[[\'.$=$msqrt$msup\', u\'=$msqrt$msup$\\u2212\', u\'msqrt$msup$\\u2212$\\u2212\'], [\'.$=$msqrt\', \'=$msqrt$msup\', u\'msqrt$msup$\\u2212\', u\'msup$\\u2212$\\u2212\'], [\'.$=\', \'=$msqrt\', \'msqrt$msup\', u\'msup$\\u2212\', u\'\\u2212$\\u2212\'], [\'.\', \'=\', \'msqrt\', \'msup\', u\'\\u2212\', u\'\\u2212\']]',1,'[u\'mrow$\\u2212\', \'mrow$msqrt\', \'mrow$msqrt$mrow$msup\', u\'mrow$msqrt$mrow$\\u2212\']','[\'var\', \'mrow$var\', \'mrow$msqrt$mrow$msup$var\', \'mrow$msqrt$mrow$var\']',4),(1135,'ax^2 + bx + c = 0','[\'msup$cn\', \'cn\']','[[\'msup$+$+$=\'], [\'msup$+$+\', \'+$+$=\'], [\'msup$+\', \'+$+\', \'+$=\']]','[[\'+$+$=$msup\'], [\'+$+$=\', \'+$=$msup\'], [\'+$+\', \'+$=\', \'=$msup\'], [\'+\', \'+\', \'=\', \'msup\']]',1,'[]','[\'var\', \'msup$var\']',4),(1136,'a \\ne 0','[\'cn\']','[[], [], []]','[[], [], [], [u\'\\u2260\']]',1,'[]','[\'var\']',5),(1137,'x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}.','[\'mrow$msqrt$mrow$cn\', \'mrow$cn\', \'mrow$msqrt$mrow$msup$cn\']','[[u\'=$\\u2212$msqrt$msup\', u\'\\u2212$msqrt$msup$\\u2212\', u\'msqrt$msup$\\u2212$.\'], [u\'=$\\u2212$msqrt\', u\'\\u2212$msqrt$msup\', u\'msqrt$msup$\\u2212\', u\'msup$\\u2212$.\'], [u\'=$\\u2212\', u\'\\u2212$msqrt\', \'msqrt$msup\', u\'msup$\\u2212\', u\'\\u2212$.\']]','[[\'.$=$msqrt$msup\', u\'=$msqrt$msup$\\u2212\', u\'msqrt$msup$\\u2212$\\u2212\'], [\'.$=$msqrt\', \'=$msqrt$msup\', u\'msqrt$msup$\\u2212\', u\'msup$\\u2212$\\u2212\'], [\'.$=\', \'=$msqrt\', \'msqrt$msup\', u\'msup$\\u2212\', u\'\\u2212$\\u2212\'], [\'.\', \'=\', \'msqrt\', \'msup\', u\'\\u2212\', u\'\\u2212\']]',1,'[u\'mrow$\\u2212\', \'mrow$msqrt\', \'mrow$msqrt$mrow$msup\', u\'mrow$msqrt$mrow$\\u2212\']','[\'var\', \'mrow$var\', \'mrow$msqrt$mrow$msup$var\', \'mrow$msqrt$mrow$var\']',5),(1138,'ax^2 + bx + c = 0','[\'msup$cn\', \'cn\']','[[\'msup$+$+$=\'], [\'msup$+$+\', \'+$+$=\'], [\'msup$+\', \'+$+\', \'+$=\']]','[[\'+$+$=$msup\'], [\'+$+$=\', \'+$=$msup\'], [\'+$+\', \'+$=\', \'=$msup\'], [\'+\', \'+\', \'=\', \'msup\']]',1,'[]','[\'var\', \'msup$var\']',5),(1139,'(2\\alpha+1)(2\\beta+1)','[\'mrow$cn\']','[[\'($+$)$(\', \'+$)$($+\', \')$($+$)\'], [\'($+$)\', \'+$)$(\', \')$($+\', \'($+$)\'], [\'($+\', \'+$)\', \')$(\', \'($+\', \'+$)\']]','[[\'($($)$)\', \'($)$)$+\', \')$)$+$+\'], [\'($($)\', \'($)$)\', \')$)$+\', \')$+$+\'], [\'($(\', \'($)\', \')$)\', \')$+\', \'+$+\'], [\'(\', \'(\', \')\', \')\', \'+\', \'+\']]',1,'[\'mrow$(\', \'mrow$+\', \'mrow$)\', \'mrow$(\', \'mrow$+\', \'mrow$)\']','[\'mrow$var\']',15),(1140,'\\frac{1}{\\alpha}+\\frac{1}{\\beta}','[\'mfrac$mrow$cn\']','[[], [\'mfrac$+$mfrac\'], [\'mfrac$+\', \'+$mfrac\']]','[[], [\'+$mfrac$mfrac\'], [\'+$mfrac\', \'mfrac$mfrac\'], [\'+\', \'mfrac\', \'mfrac\']]',1,'[]','[\'mfrac$mrow$var\']',15),(1141,'\\beta','[]','[]','[]',1,'[]','[\'var\']',15),(1142,'\\alpha','[]','[]','[]',1,'[]','[\'var\']',15),(1143,'2x^2+6x-3=0','[\'cn\', \'msup$cn\']','[[u\'msup$+$\\u2212$=\'], [u\'msup$+$\\u2212\', u\'+$\\u2212$=\'], [\'msup$+\', u\'+$\\u2212\', u\'\\u2212$=\']]','[[u\'+$=$msup$\\u2212\'], [\'+$=$msup\', u\'=$msup$\\u2212\'], [\'+$=\', \'=$msup\', u\'msup$\\u2212\'], [\'+\', \'=\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',15),(1144,'\\alpha^2','[\'msup$cn\']','[[], [], []]','[[], [], [], [\'msup\']]',1,'[]','[\'msup$var\']',16),(1145,'2x^2=1-4x','[\'cn\', \'msup$cn\']','[[], [u\'msup$=$\\u2212\'], [\'msup$=\', u\'=$\\u2212\']]','[[], [u\'=$msup$\\u2212\'], [\'=$msup\', u\'msup$\\u2212\'], [\'=\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',16),(1146,'\\beta^2','[\'msup$cn\']','[[], [], []]','[[], [], [], [\'msup\']]',1,'[]','[\'msup$var\']',16),(1147,'\\alpha','[]','[]','[]',1,'[]','[\'var\']',16),(1148,'\\beta','[]','[]','[]',1,'[]','[\'var\']',16),(1149,'x^2+(2-k)x+k=0','[\'mrow$cn\', \'msup$cn\', \'cn\']','[[u\'msup$+$($\\u2212\', u\'+$($\\u2212$)\', u\'($\\u2212$)$+\', u\'\\u2212$)$+$=\'], [\'msup$+$(\', u\'+$($\\u2212\', u\'($\\u2212$)\', u\'\\u2212$)$+\', \')$+$=\'], [\'msup$+\', \'+$(\', u\'($\\u2212\', u\'\\u2212$)\', \')$+\', \'+$=\']]','[[\'($)$+$+\', \')$+$+$=\', \'+$+$=$msup\', u\'+$=$msup$\\u2212\'], [\'($)$+\', \')$+$+\', \'+$+$=\', \'+$=$msup\', u\'=$msup$\\u2212\'], [\'($)\', \')$+\', \'+$+\', \'+$=\', \'=$msup\', u\'msup$\\u2212\'], [\'(\', \')\', \'+\', \'+\', \'=\', \'msup\', u\'\\u2212\']]',1,'[\'mrow$(\', u\'mrow$\\u2212\', \'mrow$)\']','[\'mrow$var\', \'var\', \'msup$var\']',17),(1150,'k','[]','[]','[]',1,'[]','[\'var\']',17),(1151,'y=\\frac{36}{(2x+1)^2}','[\'mfrac$mrow$msup$cn\', \'mfrac$mrow$msup$mrow$cn\', \'mfrac$mrow$cn\']','[[\'=$mfrac$msup$(\', \'mfrac$msup$($+\', \'msup$($+$)\'], [\'=$mfrac$msup\', \'mfrac$msup$(\', \'msup$($+\', \'($+$)\'], [\'=$mfrac\', \'mfrac$msup\', \'msup$(\', \'($+\', \'+$)\']]','[[\'($)$+$=\', \')$+$=$mfrac\', \'+$=$mfrac$msup\'], [\'($)$+\', \')$+$=\', \'+$=$mfrac\', \'=$mfrac$msup\'], [\'($)\', \')$+\', \'+$=\', \'=$mfrac\', \'mfrac$msup\'], [\'(\', \')\', \'+\', \'=\', \'mfrac\', \'msup\']]',1,'[\'mfrac$mrow$msup\', \'mfrac$mrow$msup$mrow$(\', \'mfrac$mrow$msup$mrow$+\', \'mfrac$mrow$msup$mrow$)\']','[\'var\', \'mfrac$mrow$msup$mrow$var\']',20),(1152,'(\\alpha+3)(\\beta+3)','[\'mrow$cn\']','[[\'($+$)$(\', \'+$)$($+\', \')$($+$)\'], [\'($+$)\', \'+$)$(\', \')$($+\', \'($+$)\'], [\'($+\', \'+$)\', \')$(\', \'($+\', \'+$)\']]','[[\'($($)$)\', \'($)$)$+\', \')$)$+$+\'], [\'($($)\', \'($)$)\', \')$)$+\', \')$+$+\'], [\'($(\', \'($)\', \')$)\', \')$+\', \'+$+\'], [\'(\', \'(\', \')\', \')\', \'+\', \'+\']]',1,'[\'mrow$(\', \'mrow$+\', \'mrow$)\', \'mrow$(\', \'mrow$+\', \'mrow$)\']','[\'mrow$var\']',21),(1153,'\\beta','[]','[]','[]',1,'[]','[\'var\']',21),(1154,'x^2+3x+1=0','[\'msup$cn\', \'cn\']','[[\'msup$+$+$=\'], [\'msup$+$+\', \'+$+$=\'], [\'msup$+\', \'+$+\', \'+$=\']]','[[\'+$+$=$msup\'], [\'+$+$=\', \'+$=$msup\'], [\'+$+\', \'+$=\', \'=$msup\'], [\'+\', \'+\', \'=\', \'msup\']]',1,'[]','[\'var\', \'msup$var\']',21),(1155,'\\frac{2}{\\alpha}+\\frac{2}{\\beta}','[\'mfrac$mrow$cn\']','[[], [\'mfrac$+$mfrac\'], [\'mfrac$+\', \'+$mfrac\']]','[[], [\'+$mfrac$mfrac\'], [\'+$mfrac\', \'mfrac$mfrac\'], [\'+\', \'mfrac\', \'mfrac\']]',1,'[]','[\'mfrac$mrow$var\']',21),(1156,'(\\alpha-\\beta)^2','[\'msup$cn\']','[[u\'msup$($\\u2212$)\'], [u\'msup$($\\u2212\', u\'($\\u2212$)\'], [\'msup$(\', u\'($\\u2212\', u\'\\u2212$)\']]','[[u\'($)$msup$\\u2212\'], [\'($)$msup\', u\')$msup$\\u2212\'], [\'($)\', \')$msup\', u\'msup$\\u2212\'], [\'(\', \')\', \'msup\', u\'\\u2212\']]',1,'[\'msup$mrow$(\', u\'msup$mrow$\\u2212\', \'msup$mrow$)\']','[\'msup$mrow$var\']',21),(1157,'\\alpha','[]','[]','[]',1,'[]','[\'var\']',21),(1158,'2x^2-x-2=0','[\'cn\', \'msup$cn\']','[[u\'msup$\\u2212$\\u2212$=\'], [u\'msup$\\u2212$\\u2212\', u\'\\u2212$\\u2212$=\'], [u\'msup$\\u2212\', u\'\\u2212$\\u2212\', u\'\\u2212$=\']]','[[u\'=$msup$\\u2212$\\u2212\'], [u\'=$msup$\\u2212\', u\'msup$\\u2212$\\u2212\'], [\'=$msup\', u\'msup$\\u2212\', u\'\\u2212$\\u2212\'], [\'=\', \'msup\', u\'\\u2212\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',22),(1159,'\\alpha','[]','[]','[]',1,'[]','[\'var\']',22),(1160,'\\beta','[]','[]','[]',1,'[]','[\'var\']',22),(1161,'-2x^2+4k-2k^2-1','[\'cn\', \'msup$cn\']','[[u\'\\u2212$msup$+$\\u2212\', u\'msup$+$\\u2212$msup\', u\'+$\\u2212$msup$\\u2212\'], [u\'\\u2212$msup$+\', u\'msup$+$\\u2212\', u\'+$\\u2212$msup\', u\'\\u2212$msup$\\u2212\'], [u\'\\u2212$msup\', \'msup$+\', u\'+$\\u2212\', u\'\\u2212$msup\', u\'msup$\\u2212\']]','[[u\'+$msup$msup$\\u2212\', u\'msup$msup$\\u2212$\\u2212\', u\'msup$\\u2212$\\u2212$\\u2212\'], [\'+$msup$msup\', u\'msup$msup$\\u2212\', u\'msup$\\u2212$\\u2212\', u\'\\u2212$\\u2212$\\u2212\'], [\'+$msup\', \'msup$msup\', u\'msup$\\u2212\', u\'\\u2212$\\u2212\', u\'\\u2212$\\u2212\'], [\'+\', \'msup\', \'msup\', u\'\\u2212\', u\'\\u2212\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',27),(1162,'k','[]','[]','[]',1,'[]','[\'var\']',27),(1163,'y=mx-8','[\'cn\']','[[], [], [u\'=$\\u2212\']]','[[], [], [u\'=$\\u2212\'], [\'=\', u\'\\u2212\']]',1,'[]','[\'var\']',28),(1164,'y=x^2-5x+m','[\'msup$cn\', \'cn\']','[[u\'=$msup$\\u2212$+\'], [u\'=$msup$\\u2212\', u\'msup$\\u2212$+\'], [\'=$msup\', u\'msup$\\u2212\', u\'\\u2212$+\']]','[[u\'+$=$msup$\\u2212\'], [\'+$=$msup\', u\'=$msup$\\u2212\'], [\'+$=\', \'=$msup\', u\'msup$\\u2212\'], [\'+\', \'=\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',28),(1165,'m^2+6m-7 \\geq 0','[\'msup$cn\', \'cn\']','[[u\'msup$+$\\u2212$\\u2265\'], [u\'msup$+$\\u2212\', u\'+$\\u2212$\\u2265\'], [\'msup$+\', u\'+$\\u2212\', u\'\\u2212$\\u2265\']]','[[u\'+$msup$\\u2212$\\u2265\'], [u\'+$msup$\\u2212\', u\'msup$\\u2212$\\u2265\'], [\'+$msup\', u\'msup$\\u2212\', u\'\\u2212$\\u2265\'], [\'+\', \'msup\', u\'\\u2212\', u\'\\u2265\']]',1,'[]','[\'var\', \'msup$var\']',28),(1166,'(x+1)(2x-1)=p-2','[\'mrow$cn\', \'cn\']','[[\'($+$)$(\', u\'+$)$($\\u2212\', u\')$($\\u2212$)\', u\'($\\u2212$)$=\', u\'\\u2212$)$=$\\u2212\'], [\'($+$)\', \'+$)$(\', u\')$($\\u2212\', u\'($\\u2212$)\', u\'\\u2212$)$=\', u\')$=$\\u2212\'], [\'($+\', \'+$)\', \')$(\', u\'($\\u2212\', u\'\\u2212$)\', \')$=\', u\'=$\\u2212\']]','[[\'($($)$)\', \'($)$)$+\', \')$)$+$=\', u\')$+$=$\\u2212\', u\'+$=$\\u2212$\\u2212\'], [\'($($)\', \'($)$)\', \')$)$+\', \')$+$=\', u\'+$=$\\u2212\', u\'=$\\u2212$\\u2212\'], [\'($(\', \'($)\', \')$)\', \')$+\', \'+$=\', u\'=$\\u2212\', u\'\\u2212$\\u2212\'], [\'(\', \'(\', \')\', \')\', \'+\', \'=\', u\'\\u2212\', u\'\\u2212\']]',1,'[\'mrow$(\', \'mrow$+\', \'mrow$)\', \'mrow$(\', u\'mrow$\\u2212\', \'mrow$)\']','[\'mrow$var\', \'var\']',29),(1167,'2x^2-4x+3=p','[\'cn\', \'msup$cn\']','[[u\'msup$\\u2212$+$=\'], [u\'msup$\\u2212$+\', u\'\\u2212$+$=\'], [u\'msup$\\u2212\', u\'\\u2212$+\', \'+$=\']]','[[u\'+$=$msup$\\u2212\'], [\'+$=$msup\', u\'=$msup$\\u2212\'], [\'+$=\', \'=$msup\', u\'msup$\\u2212\'], [\'+\', \'=\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',29),(1168,'p(x+1)(x-3)=x-4p-2','[\'mrow$cn\', \'cn\']','[[\'($+$)$(\', u\'+$)$($\\u2212\', u\')$($\\u2212$)\', u\'($\\u2212$)$=\', u\'\\u2212$)$=$\\u2212\', u\')$=$\\u2212$\\u2212\'], [\'($+$)\', \'+$)$(\', u\')$($\\u2212\', u\'($\\u2212$)\', u\'\\u2212$)$=\', u\')$=$\\u2212\', u\'=$\\u2212$\\u2212\'], [\'($+\', \'+$)\', \')$(\', u\'($\\u2212\', u\'\\u2212$)\', \')$=\', u\'=$\\u2212\', u\'\\u2212$\\u2212\']]','[[\'($($)$)\', \'($)$)$+\', \')$)$+$=\', u\')$+$=$\\u2212\', u\'+$=$\\u2212$\\u2212\', u\'=$\\u2212$\\u2212$\\u2212\'], [\'($($)\', \'($)$)\', \')$)$+\', \')$+$=\', u\'+$=$\\u2212\', u\'=$\\u2212$\\u2212\', u\'\\u2212$\\u2212$\\u2212\'], [\'($(\', \'($)\', \')$)\', \')$+\', \'+$=\', u\'=$\\u2212\', u\'\\u2212$\\u2212\', u\'\\u2212$\\u2212\'], [\'(\', \'(\', \')\', \')\', \'+\', \'=\', u\'\\u2212\', u\'\\u2212\', u\'\\u2212\']]',1,'[\'mrow$(\', \'mrow$+\', \'mrow$)\', \'mrow$(\', u\'mrow$\\u2212\', \'mrow$)\']','[\'var\', \'mrow$var\']',29),(1169,'3x^2=2x+p-1','[\'cn\', \'msup$cn\']','[[u\'msup$=$+$\\u2212\'], [\'msup$=$+\', u\'=$+$\\u2212\'], [\'msup$=\', \'=$+\', u\'+$\\u2212\']]','[[u\'+$=$msup$\\u2212\'], [\'+$=$msup\', u\'=$msup$\\u2212\'], [\'+$=\', \'=$msup\', u\'msup$\\u2212\'], [\'+\', \'=\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',29),(1170,'p','[]','[]','[]',1,'[]','[\'var\']',29),(1171,'x^2+p^2=3px-1','[\'msup$cn\', \'cn\']','[[\'msup$+$msup$=\', u\'+$msup$=$\\u2212\'], [\'msup$+$msup\', \'+$msup$=\', u\'msup$=$\\u2212\'], [\'msup$+\', \'+$msup\', \'msup$=\', u\'=$\\u2212\']]','[[\'+$=$msup$msup\', u\'=$msup$msup$\\u2212\'], [\'+$=$msup\', \'=$msup$msup\', u\'msup$msup$\\u2212\'], [\'+$=\', \'=$msup\', \'msup$msup\', u\'msup$\\u2212\'], [\'+\', \'=\', \'msup\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',29),(1172,'px^2-6x+p=0','[\'msup$cn\', \'cn\']','[[u\'msup$\\u2212$+$=\'], [u\'msup$\\u2212$+\', u\'\\u2212$+$=\'], [u\'msup$\\u2212\', u\'\\u2212$+\', \'+$=\']]','[[u\'+$=$msup$\\u2212\'], [\'+$=$msup\', u\'=$msup$\\u2212\'], [\'+$=\', \'=$msup\', u\'msup$\\u2212\'], [\'+\', \'=\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',29),(1173,'x(x-2)=x-2p','[\'mrow$cn\', \'cn\']','[[u\'($\\u2212$)$=\', u\'\\u2212$)$=$\\u2212\'], [u\'($\\u2212$)\', u\'\\u2212$)$=\', u\')$=$\\u2212\'], [u\'($\\u2212\', u\'\\u2212$)\', \')$=\', u\'=$\\u2212\']]','[[u\'($)$=$\\u2212\', u\')$=$\\u2212$\\u2212\'], [\'($)$=\', u\')$=$\\u2212\', u\'=$\\u2212$\\u2212\'], [\'($)\', \')$=\', u\'=$\\u2212\', u\'\\u2212$\\u2212\'], [\'(\', \')\', \'=\', u\'\\u2212\', u\'\\u2212\']]',1,'[\'mrow$(\', u\'mrow$\\u2212\', \'mrow$)\']','[\'var\', \'mrow$var\']',29),(1174,'k','[]','[]','[]',1,'[]','[\'var\']',30),(1175,'x^2-2kx+k^2=3+x','[\'msup$cn\', \'cn\']','[[u\'msup$\\u2212$+$msup\', u\'\\u2212$+$msup$=\', \'+$msup$=$+\'], [u\'msup$\\u2212$+\', u\'\\u2212$+$msup\', \'+$msup$=\', \'msup$=$+\'], [u\'msup$\\u2212\', u\'\\u2212$+\', \'+$msup\', \'msup$=\', \'=$+\']]','[[\'+$+$=$msup\', \'+$=$msup$msup\', u\'=$msup$msup$\\u2212\'], [\'+$+$=\', \'+$=$msup\', \'=$msup$msup\', u\'msup$msup$\\u2212\'], [\'+$+\', \'+$=\', \'=$msup\', \'msup$msup\', u\'msup$\\u2212\'], [\'+\', \'+\', \'=\', \'msup\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',30),(1176,'2x^2+p=2(x-1)','[\'mrow$cn\', \'cn\', \'msup$cn\']','[[\'msup$+$=$(\', u\'+$=$($\\u2212\', u\'=$($\\u2212$)\'], [\'msup$+$=\', \'+$=$(\', u\'=$($\\u2212\', u\'($\\u2212$)\'], [\'msup$+\', \'+$=\', \'=$(\', u\'($\\u2212\', u\'\\u2212$)\']]','[[\'($)$+$=\', \')$+$=$msup\', u\'+$=$msup$\\u2212\'], [\'($)$+\', \')$+$=\', \'+$=$msup\', u\'=$msup$\\u2212\'], [\'($)\', \')$+\', \'+$=\', \'=$msup\', u\'msup$\\u2212\'], [\'(\', \')\', \'+\', \'=\', \'msup\', u\'\\u2212\']]',1,'[\'mrow$(\', u\'mrow$\\u2212\', \'mrow$)\']','[\'var\', \'mrow$var\', \'msup$var\']',31),(1177,'p>-\\frac{3}{2}','[\'mfrac$mrow$cn\']','[[], [], [u\'>$\\u2212\']]','[[], [], [u\'>$\\u2212\'], [\'>\', u\'\\u2212\']]',1,'[]','[\'var\']',31),(1178,'k','[]','[]','[]',1,'[]','[\'var\']',32),(1179,'y=2x+3','[\'cn\']','[[], [], [\'=$+\']]','[[], [], [\'+$=\'], [\'+\', \'=\']]',1,'[]','[\'var\']',32),(1180,'x^2+xy=k','[\'msup$cn\']','[[], [\'msup$+$=\'], [\'msup$+\', \'+$=\']]','[[], [\'+$=$msup\'], [\'+$=\', \'=$msup\'], [\'+\', \'=\', \'msup\']]',1,'[]','[\'var\', \'msup$var\']',32),(1181,'x','[]','[]','[]',1,'[]','[\'var\']',33),(1182,'c','[]','[]','[]',1,'[]','[\'var\']',33),(1183,'y=3x^2-2x+c-1','[\'cn\', \'msup$cn\']','[[u\'=$msup$\\u2212$+\', u\'msup$\\u2212$+$\\u2212\'], [u\'=$msup$\\u2212\', u\'msup$\\u2212$+\', u\'\\u2212$+$\\u2212\'], [\'=$msup\', u\'msup$\\u2212\', u\'\\u2212$+\', u\'+$\\u2212\']]','[[u\'+$=$msup$\\u2212\', u\'=$msup$\\u2212$\\u2212\'], [\'+$=$msup\', u\'=$msup$\\u2212\', u\'msup$\\u2212$\\u2212\'], [\'+$=\', \'=$msup\', u\'msup$\\u2212\', u\'\\u2212$\\u2212\'], [\'+\', \'=\', \'msup\', u\'\\u2212\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',33),(1184,'p','[]','[]','[]',1,'[]','[\'var\']',34),(1185,'y=x^2+px-p+3','[\'msup$cn\', \'cn\']','[[u\'=$msup$+$\\u2212\', u\'msup$+$\\u2212$+\'], [\'=$msup$+\', u\'msup$+$\\u2212\', u\'+$\\u2212$+\'], [\'=$msup\', \'msup$+\', u\'+$\\u2212\', u\'\\u2212$+\']]','[[\'+$+$=$msup\', u\'+$=$msup$\\u2212\'], [\'+$+$=\', \'+$=$msup\', u\'=$msup$\\u2212\'], [\'+$+\', \'+$=\', \'=$msup\', u\'msup$\\u2212\'], [\'+\', \'+\', \'=\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',34),(1186,'x','[]','[]','[]',1,'[]','[\'var\']',34),(1187,'kx^2+1&gt;2kx-k','[\'msup$cn\', \'cn\']','[[u\'msup$+$>$\\u2212\'], [\'msup$+$>\', u\'+$>$\\u2212\'], [\'msup$+\', \'+$>\', u\'>$\\u2212\']]','[[u\'+$>$msup$\\u2212\'], [\'+$>$msup\', u\'>$msup$\\u2212\'], [\'+$>\', \'>$msup\', u\'msup$\\u2212\'], [\'+\', \'>\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',35),(1188,'k','[]','[]','[]',1,'[]','[\'var\']',35),(1189,'-3x^2+6x+k-1','[\'cn\', \'msup$cn\']','[[u\'\\u2212$msup$+$+\', u\'msup$+$+$\\u2212\'], [u\'\\u2212$msup$+\', \'msup$+$+\', u\'+$+$\\u2212\'], [u\'\\u2212$msup\', \'msup$+\', \'+$+\', u\'+$\\u2212\']]','[[u\'+$+$msup$\\u2212\', u\'+$msup$\\u2212$\\u2212\'], [\'+$+$msup\', u\'+$msup$\\u2212\', u\'msup$\\u2212$\\u2212\'], [\'+$+\', \'+$msup\', u\'msup$\\u2212\', u\'\\u2212$\\u2212\'], [\'+\', \'+\', \'msup\', u\'\\u2212\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',35),(1190,'x','[]','[]','[]',1,'[]','[\'var\']',35),(1191,'3x^2-3x&gt;x+k','[\'cn\', \'msup$cn\']','[[u\'msup$\\u2212$>$+\'], [u\'msup$\\u2212$>\', u\'\\u2212$>$+\'], [u\'msup$\\u2212\', u\'\\u2212$>\', \'>$+\']]','[[u\'+$>$msup$\\u2212\'], [\'+$>$msup\', u\'>$msup$\\u2212\'], [\'+$>\', \'>$msup\', u\'msup$\\u2212\'], [\'+\', \'>\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',35),(1192,'2x^2+2x+k','[\'cn\', \'msup$cn\']','[[], [\'msup$+$+\'], [\'msup$+\', \'+$+\']]','[[], [\'+$+$msup\'], [\'+$+\', \'+$msup\'], [\'+\', \'+\', \'msup\']]',1,'[]','[\'var\', \'msup$var\']',35),(1193,'2x^2=8x+3','[\'cn\', \'msup$cn\']','[[], [\'msup$=$+\'], [\'msup$=\', \'=$+\']]','[[], [\'+$=$msup\'], [\'+$=\', \'=$msup\'], [\'+\', \'=\', \'msup\']]',1,'[]','[\'var\', \'msup$var\']',37),(1194,'\\alpha','[]','[]','[]',1,'[]','[\'var\']',37),(1195,'\\beta','[]','[]','[]',1,'[]','[\'var\']',37),(1196,'x^2=2x-1','[\'msup$cn\', \'cn\']','[[], [u\'msup$=$\\u2212\'], [\'msup$=\', u\'=$\\u2212\']]','[[], [u\'=$msup$\\u2212\'], [\'=$msup\', u\'msup$\\u2212\'], [\'=\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',38),(1197,'\\alpha','[]','[]','[]',1,'[]','[\'var\']',38),(1198,'x^2+(1-k)x-k=0','[\'mrow$cn\', \'msup$cn\', \'cn\']','[[u\'msup$+$($\\u2212\', u\'+$($\\u2212$)\', u\'($\\u2212$)$\\u2212\', u\'\\u2212$)$\\u2212$=\'], [\'msup$+$(\', u\'+$($\\u2212\', u\'($\\u2212$)\', u\'\\u2212$)$\\u2212\', u\')$\\u2212$=\'], [\'msup$+\', \'+$(\', u\'($\\u2212\', u\'\\u2212$)\', u\')$\\u2212\', u\'\\u2212$=\']]','[[\'($)$+$=\', \')$+$=$msup\', u\'+$=$msup$\\u2212\', u\'=$msup$\\u2212$\\u2212\'], [\'($)$+\', \')$+$=\', \'+$=$msup\', u\'=$msup$\\u2212\', u\'msup$\\u2212$\\u2212\'], [\'($)\', \')$+\', \'+$=\', \'=$msup\', u\'msup$\\u2212\', u\'\\u2212$\\u2212\'], [\'(\', \')\', \'+\', \'=\', \'msup\', u\'\\u2212\', u\'\\u2212\']]',1,'[\'mrow$(\', u\'mrow$\\u2212\', \'mrow$)\']','[\'mrow$var\', \'var\', \'msup$var\']',39),(1199,'4p^2=25q','[\'cn\', \'msup$cn\']','[[], [], [\'msup$=\']]','[[], [], [\'=$msup\'], [\'=\', \'msup\']]',1,'[]','[\'var\', \'msup$var\']',40),(1200,'x^2+px+q=0','[\'msup$cn\', \'cn\']','[[\'msup$+$+$=\'], [\'msup$+$+\', \'+$+$=\'], [\'msup$+\', \'+$+\', \'+$=\']]','[[\'+$+$=$msup\'], [\'+$+$=\', \'+$=$msup\'], [\'+$+\', \'+$=\', \'=$msup\'], [\'+\', \'+\', \'=\', \'msup\']]',1,'[]','[\'var\', \'msup$var\']',40),(1201,'4\\alpha','[\'cn\']','[]','[]',1,'[]','[\'var\']',40),(1202,'\\alpha','[]','[]','[]',1,'[]','[\'var\']',40),(1203,'x^2-3x-2=0','[\'msup$cn\', \'cn\']','[[u\'msup$\\u2212$\\u2212$=\'], [u\'msup$\\u2212$\\u2212\', u\'\\u2212$\\u2212$=\'], [u\'msup$\\u2212\', u\'\\u2212$\\u2212\', u\'\\u2212$=\']]','[[u\'=$msup$\\u2212$\\u2212\'], [u\'=$msup$\\u2212\', u\'msup$\\u2212$\\u2212\'], [\'=$msup\', u\'msup$\\u2212\', u\'\\u2212$\\u2212\'], [\'=\', \'msup\', u\'\\u2212\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',41),(1204,'\\frac{k}{\\alpha}','[]','[[], [], []]','[[], [], [], [\'mfrac\']]',1,'[]','[\'mfrac$mrow$var\']',41),(1205,'k','[]','[]','[]',1,'[]','[\'var\']',41),(1206,'\\beta','[]','[]','[]',1,'[]','[\'var\']',41),(1207,'x^2-6x+p=0','[\'msup$cn\', \'cn\']','[[u\'msup$\\u2212$+$=\'], [u\'msup$\\u2212$+\', u\'\\u2212$+$=\'], [u\'msup$\\u2212\', u\'\\u2212$+\', \'+$=\']]','[[u\'+$=$msup$\\u2212\'], [\'+$=$msup\', u\'=$msup$\\u2212\'], [\'+$=\', \'=$msup\', u\'msup$\\u2212\'], [\'+\', \'=\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',41),(1208,'p','[]','[]','[]',1,'[]','[\'var\']',41),(1209,'\\frac{k}{\\beta}','[]','[[], [], []]','[[], [], [], [\'mfrac\']]',1,'[]','[\'mfrac$mrow$var\']',41),(1210,'\\alpha','[]','[]','[]',1,'[]','[\'var\']',41),(1211,'k','[]','[]','[]',1,'[]','[\'var\']',42),(1212,'kx^2+(k-1)x+2k+3=0','[\'mrow$cn\', \'msup$cn\', \'cn\']','[[u\'msup$+$($\\u2212\', u\'+$($\\u2212$)\', u\'($\\u2212$)$+\', u\'\\u2212$)$+$+\', \')$+$+$=\'], [\'msup$+$(\', u\'+$($\\u2212\', u\'($\\u2212$)\', u\'\\u2212$)$+\', \')$+$+\', \'+$+$=\'], [\'msup$+\', \'+$(\', u\'($\\u2212\', u\'\\u2212$)\', \')$+\', \'+$+\', \'+$=\']]','[[\'($)$+$+\', \')$+$+$+\', \'+$+$+$=\', \'+$+$=$msup\', u\'+$=$msup$\\u2212\'], [\'($)$+\', \')$+$+\', \'+$+$+\', \'+$+$=\', \'+$=$msup\', u\'=$msup$\\u2212\'], [\'($)\', \')$+\', \'+$+\', \'+$+\', \'+$=\', \'=$msup\', u\'msup$\\u2212\'], [\'(\', \')\', \'+\', \'+\', \'+\', \'=\', \'msup\', u\'\\u2212\']]',1,'[\'mrow$(\', u\'mrow$\\u2212\', \'mrow$)\']','[\'var\', \'mrow$var\', \'msup$var\']',42),(1213,'3x^2-3kx+k-6=0','[\'cn\', \'msup$cn\']','[[u\'msup$\\u2212$+$\\u2212\', u\'\\u2212$+$\\u2212$=\'], [u\'msup$\\u2212$+\', u\'\\u2212$+$\\u2212\', u\'+$\\u2212$=\'], [u\'msup$\\u2212\', u\'\\u2212$+\', u\'+$\\u2212\', u\'\\u2212$=\']]','[[u\'+$=$msup$\\u2212\', u\'=$msup$\\u2212$\\u2212\'], [\'+$=$msup\', u\'=$msup$\\u2212\', u\'msup$\\u2212$\\u2212\'], [\'+$=\', \'=$msup\', u\'msup$\\u2212\', u\'\\u2212$\\u2212\'], [\'+\', \'=\', \'msup\', u\'\\u2212\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',45),(1214,'\\alpha^2+\\beta^2=\\frac{20}{3}\r\n','[\'msup$cn\', \'mfrac$mrow$cn\']','[[\'msup$+$msup$=\'], [\'msup$+$msup\', \'+$msup$=\'], [\'msup$+\', \'+$msup\', \'msup$=\']]','[[\'+$=$msup$msup\'], [\'+$=$msup\', \'=$msup$msup\'], [\'+$=\', \'=$msup\', \'msup$msup\'], [\'+\', \'=\', \'msup\', \'msup\']]',1,'[]','[\'msup$var\']',45),(1215,'k','[]','[]','[]',1,'[]','[\'var\']',45),(1216,'\\alpha','[]','[]','[]',1,'[]','[\'var\']',45),(1217,'\\beta','[]','[]','[]',1,'[]','[\'var\']',45),(1218,'\\alpha^2','[\'msup$cn\']','[[], [], []]','[[], [], [], [\'msup\']]',1,'[]','[\'msup$var\']',46),(1219,'4x^2-x+36=0','[\'cn\', \'msup$cn\']','[[u\'msup$\\u2212$+$=\'], [u\'msup$\\u2212$+\', u\'\\u2212$+$=\'], [u\'msup$\\u2212\', u\'\\u2212$+\', \'+$=\']]','[[u\'+$=$msup$\\u2212\'], [\'+$=$msup\', u\'=$msup$\\u2212\'], [\'+$=\', \'=$msup\', u\'msup$\\u2212\'], [\'+\', \'=\', \'msup\', u\'\\u2212\']]',1,'[]','[\'var\', \'msup$var\']',46),(1220,'\\beta^2','[\'msup$cn\']','[[], [], []]','[[], [], [], [\'msup\']]',1,'[]','[\'msup$var\']',46),(1221,'\\alpha^2+\\beta^2','[\'msup$cn\']','[[], [\'msup$+$msup\'], [\'msup$+\', \'+$msup\']]','[[], [\'+$msup$msup\'], [\'+$msup\', \'msup$msup\'], [\'+\', \'msup\', \'msup\']]',1,'[]','[\'msup$var\']',48),(1222,'\\frac{1}{\\alpha}+\\frac{1}{\\beta} [3]','[\'mrow$cn\', \'mfrac$mrow$cn\']','[[\'mfrac$+$mfrac$[\', \'+$mfrac$[$]\'], [\'mfrac$+$mfrac\', \'+$mfrac$[\', \'mfrac$[$]\'], [\'mfrac$+\', \'+$mfrac\', \'mfrac$[\', \'[$]\']]','[[\'+$[$]$mfrac\', \'[$]$mfrac$mfrac\'], [\'+$[$]\', \'[$]$mfrac\', \']$mfrac$mfrac\'], [\'+$[\', \'[$]\', \']$mfrac\', \'mfrac$mfrac\'], [\'+\', \'[\', \']\', \'mfrac\', \'mfrac\']]',1,'[\'mrow$[\', \'mrow$]\']','[\'mfrac$mrow$var\']',48),(1223,'2x^2+3x+4=0','[\'cn\', \'msup$cn\']','[[\'msup$+$+$=\'], [\'msup$+$+\', \'+$+$=\'], [\'msup$+\', \'+$+\', \'+$=\']]','[[\'+$+$=$msup\'], [\'+$+$=\', \'+$=$msup\'], [\'+$+\', \'+$=\', \'=$msup\'], [\'+\', \'+\', \'=\', \'msup\']]',1,'[]','[\'var\', \'msup$var\']',48),(1224,'\\alpha','[]','[]','[]',1,'[]','[\'var\']',48),(1225,'\\beta','[]','[]','[]',1,'[]','[\'var\']',48),(1226,'\\theta','[]','[]','[]',1,'[]','[\'var\']',55),(1227,'3\\cos \\theta + 4\\sin \\theta','[\'cn\']','[[], [\'cos$+$sin\'], [\'cos$+\', \'+$sin\']]','[[], [\'+$cos$sin\'], [\'+$cos\', \'cos$sin\'], [\'+\', \'cos\', \'sin\']]',1,'[]','[\'var\']',55),(1228,'2\\sin x+\\cos x','[\'cn\']','[[], [\'sin$+$cos\'], [\'sin$+\', \'+$cos\']]','[[], [\'+$cos$sin\'], [\'+$cos\', \'cos$sin\'], [\'+\', \'cos\', \'sin\']]',1,'[]','[\'var\']',56),(1229,'x','[]','[]','[]',1,'[]','[\'var\']',56),(1230,'0^\\circ \\leq x \\leq 360^\\circ','[\'msup$cn\']','[[u\'\\u2218$\\u2264$\\u2264$\\u2218\'], [u\'\\u2218$\\u2264$\\u2264\', u\'\\u2264$\\u2264$\\u2218\'], [u\'\\u2218$\\u2264\', u\'\\u2264$\\u2264\', u\'\\u2264$\\u2218\']]','[[u\'\\u2218$\\u2218$\\u2264$\\u2264\'], [u\'\\u2218$\\u2218$\\u2264\', u\'\\u2218$\\u2264$\\u2264\'], [u\'\\u2218$\\u2218\', u\'\\u2218$\\u2264\', u\'\\u2264$\\u2264\'], [u\'\\u2218\', u\'\\u2218\', u\'\\u2264\', u\'\\u2264\']]',1,'[u\'msup$\\u2218\', u\'msup$\\u2218\']','[\'var\']',56),(1231,'0^\\circ','[\'msup$cn\']','[[], [], []]','[[], [], [], [u\'\\u2218\']]',1,'[u\'msup$\\u2218\']','[]',57),(1232,'2 \\cos x - 5 \\sin x = 3.1.','[\'cn\']','[[u\'cos$\\u2212$sin$=\'], [u\'cos$\\u2212$sin\', u\'\\u2212$sin$=\'], [u\'cos$\\u2212\', u\'\\u2212$sin\', \'sin$=\']]','[[u\'=$cos$sin$\\u2212\'], [\'=$cos$sin\', u\'cos$sin$\\u2212\'], [\'=$cos\', \'cos$sin\', u\'sin$\\u2212\'], [\'=\', \'cos\', \'sin\', u\'\\u2212\']]',1,'[]','[\'var\']',57),(1233,'360^\\circ','[\'msup$cn\']','[[], [], []]','[[], [], [], [u\'\\u2218\']]',1,'[u\'msup$\\u2218\']','[]',57),(1234,'\\cos \\theta +\\sin \\theta','[]','[[], [\'cos$+$sin\'], [\'cos$+\', \'+$sin\']]','[[], [\'+$cos$sin\'], [\'+$cos\', \'cos$sin\'], [\'+\', \'cos\', \'sin\']]',1,'[]','[\'var\']',58),(1235,'\\sqrt{3}\\cos \\theta - \\sin \\theta','[\'msqrt$mrow$cn\']','[[], [u\'cos$\\u2212$sin\'], [u\'cos$\\u2212\', u\'\\u2212$sin\']]','[[], [u\'cos$sin$\\u2212\'], [\'cos$sin\', u\'sin$\\u2212\'], [\'cos\', \'sin\', u\'\\u2212\']]',1,'[]','[\'var\']',59),(1236,'(\\cos x -\\sin x)^2 =1 -\\sin 2x','[\'msup$cn\', \'cn\']','[[u\'msup$($cos$\\u2212\', u\'($cos$\\u2212$sin\', u\'cos$\\u2212$sin$)\', u\'\\u2212$sin$)$=\', u\'sin$)$=$\\u2212\', u\')$=$\\u2212$sin\'], [\'msup$($cos\', u\'($cos$\\u2212\', u\'cos$\\u2212$sin\', u\'\\u2212$sin$)\', \'sin$)$=\', u\')$=$\\u2212\', u\'=$\\u2212$sin\'], [\'msup$(\', \'($cos\', u\'cos$\\u2212\', u\'\\u2212$sin\', \'sin$)\', \')$=\', u\'=$\\u2212\', u\'\\u2212$sin\']]','[[\'($)$=$cos\', \')$=$cos$msup\', \'=$cos$msup$sin\', \'cos$msup$sin$sin\', u\'msup$sin$sin$\\u2212\', u\'sin$sin$\\u2212$\\u2212\'], [\'($)$=\', \')$=$cos\', \'=$cos$msup\', \'cos$msup$sin\', \'msup$sin$sin\', u\'sin$sin$\\u2212\', u\'sin$\\u2212$\\u2212\'], [\'($)\', \')$=\', \'=$cos\', \'cos$msup\', \'msup$sin\', \'sin$sin\', u\'sin$\\u2212\', u\'\\u2212$\\u2212\'], [\'(\', \')\', \'=\', \'cos\', \'msup\', \'sin\', \'sin\', u\'\\u2212\', u\'\\u2212\']]',1,'[\'msup$mrow$(\', \'msup$mrow$cos\', u\'msup$mrow$\\u2212\', \'msup$mrow$sin\', \'msup$mrow$)\']','[\'msup$mrow$var\', \'var\']',60),(1237,'\\frac{sec^2 A}{\\tan A}=2 \\text{ cosec } 2A','[\'mfrac$mrow$msup$cn\', \'cn\']','[[\'mfrac$e$msup$tan\', \'e$msup$tan$=\', \'msup$tan$=$e\'], [\'mfrac$e$msup\', \'e$msup$tan\', \'msup$tan$=\', \'tan$=$e\'], [\'mfrac$e\', \'e$msup\', \'msup$tan\', \'tan$=\', \'=$e\']]','[[\'=$e$e$mfrac\', \'e$e$mfrac$msup\', \'e$mfrac$msup$tan\'], [\'=$e$e\', \'e$e$mfrac\', \'e$mfrac$msup\', \'mfrac$msup$tan\'], [\'=$e\', \'e$e\', \'e$mfrac\', \'mfrac$msup\', \'msup$tan\'], [\'=\', \'e\', \'e\', \'mfrac\', \'msup\', \'tan\']]',1,'[\'mfrac$mrow$e\', \'mfrac$mrow$msup\', \'mfrac$mrow$tan\', \'mrow$e\']','[\'var\', \'mfrac$mrow$var\', \'mfrac$mrow$msup$var\', \'mrow$var\']',61),(1238,'\\sec^2 \\frac{\\theta}{2}=\\frac{2}{1+\\cos \\theta}','[\'msup$cn\', \'mfrac$mrow$cn\']','[[\'msup$sec$mfrac$=\', \'sec$mfrac$=$mfrac\', \'mfrac$=$mfrac$+\', \'=$mfrac$+$cos\'], [\'msup$sec$mfrac\', \'sec$mfrac$=\', \'mfrac$=$mfrac\', \'=$mfrac$+\', \'mfrac$+$cos\'], [\'msup$sec\', \'sec$mfrac\', \'mfrac$=\', \'=$mfrac\', \'mfrac$+\', \'+$cos\']]','[[\'+$=$cos$mfrac\', \'=$cos$mfrac$mfrac\', \'cos$mfrac$mfrac$msup\', \'mfrac$mfrac$msup$sec\'], [\'+$=$cos\', \'=$cos$mfrac\', \'cos$mfrac$mfrac\', \'mfrac$mfrac$msup\', \'mfrac$msup$sec\'], [\'+$=\', \'=$cos\', \'cos$mfrac\', \'mfrac$mfrac\', \'mfrac$msup\', \'msup$sec\'], [\'+\', \'=\', \'cos\', \'mfrac\', \'mfrac\', \'msup\', \'sec\']]',1,'[\'msup$sec\', \'mfrac$mrow$+\', \'mfrac$mrow$cos\']','[\'mfrac$mrow$var\']',62),(1239,'\\cos^4 A -\\sin^4 A = \\cos 2A','[\'msup$cn\', \'cn\']','[[u\'msup$cos$\\u2212$msup\', u\'cos$\\u2212$msup$sin\', u\'\\u2212$msup$sin$=\', \'msup$sin$=$cos\'], [u\'msup$cos$\\u2212\', u\'cos$\\u2212$msup\', u\'\\u2212$msup$sin\', \'msup$sin$=\', \'sin$=$cos\'], [\'msup$cos\', u\'cos$\\u2212\', u\'\\u2212$msup\', \'msup$sin\', \'sin$=\', \'=$cos\']]','[[\'=$cos$cos$msup\', \'cos$cos$msup$msup\', \'cos$msup$msup$sin\', u\'msup$msup$sin$\\u2212\'], [\'=$cos$cos\', \'cos$cos$msup\', \'cos$msup$msup\', \'msup$msup$sin\', u\'msup$sin$\\u2212\'], [\'=$cos\', \'cos$cos\', \'cos$msup\', \'msup$msup\', \'msup$sin\', u\'sin$\\u2212\'], [\'=\', \'cos\', \'cos\', \'msup\', \'msup\', \'sin\', u\'\\u2212\']]',1,'[\'msup$cos\', \'msup$sin\']','[\'var\']',63),(1240,'\\frac{\\sin A}{1+\\cos A}=\\tan \\frac{1}{2}A','[\'mfrac$mrow$cn\']','[[\'mfrac$sin$+$cos\', \'sin$+$cos$=\', \'+$cos$=$tan\'], [\'mfrac$sin$+\', \'sin$+$cos\', \'+$cos$=\', \'cos$=$tan\'], [\'mfrac$sin\', \'sin$+\', \'+$cos\', \'cos$=\', \'=$tan\']]','[[\'+$=$cos$mfrac\', \'=$cos$mfrac$sin\', \'cos$mfrac$sin$tan\'], [\'+$=$cos\', \'=$cos$mfrac\', \'cos$mfrac$sin\', \'mfrac$sin$tan\'], [\'+$=\', \'=$cos\', \'cos$mfrac\', \'mfrac$sin\', \'sin$tan\'], [\'+\', \'=\', \'cos\', \'mfrac\', \'sin\', \'tan\']]',1,'[\'mfrac$mrow$sin\', \'mfrac$mrow$+\', \'mfrac$mrow$cos\']','[\'var\', \'mfrac$mrow$var\']',64),(1241,'\\frac{1+\\tan^2 A}{1-\\tan^2 A}=\\sec 2A','[\'mfrac$mrow$msup$cn\', \'cn\', \'mfrac$mrow$cn\']','[[\'mfrac$+$msup$tan\', u\'+$msup$tan$\\u2212\', u\'msup$tan$\\u2212$msup\', u\'tan$\\u2212$msup$tan\', u\'\\u2212$msup$tan$=\', \'msup$tan$=$sec\'], [\'mfrac$+$msup\', \'+$msup$tan\', u\'msup$tan$\\u2212\', u\'tan$\\u2212$msup\', u\'\\u2212$msup$tan\', \'msup$tan$=\', \'tan$=$sec\'], [\'mfrac$+\', \'+$msup\', \'msup$tan\', u\'tan$\\u2212\', u\'\\u2212$msup\', \'msup$tan\', \'tan$=\', \'=$sec\']]','[[\'+$=$mfrac$msup\', \'=$mfrac$msup$msup\', \'mfrac$msup$msup$sec\', \'msup$msup$sec$tan\', \'msup$sec$tan$tan\', u\'sec$tan$tan$\\u2212\'], [\'+$=$mfrac\', \'=$mfrac$msup\', \'mfrac$msup$msup\', \'msup$msup$sec\', \'msup$sec$tan\', \'sec$tan$tan\', u\'tan$tan$\\u2212\'], [\'+$=\', \'=$mfrac\', \'mfrac$msup\', \'msup$msup\', \'msup$sec\', \'sec$tan\', \'tan$tan\', u\'tan$\\u2212\'], [\'+\', \'=\', \'mfrac\', \'msup\', \'msup\', \'sec\', \'tan\', \'tan\', u\'\\u2212\']]',1,'[\'mfrac$mrow$+\', \'mfrac$mrow$msup\', \'mfrac$mrow$msup$tan\', u\'mfrac$mrow$\\u2212\', \'mfrac$mrow$msup\', \'mfrac$mrow$msup$tan\']','[\'var\', \'mfrac$mrow$var\']',65),(1242,'x^2+4x+5=0','[\'msup$cn\', \'cn\']','[[\'msup$+$+$=\'], [\'msup$+$+\', \'+$+$=\'], [\'msup$+\', \'+$+\', \'+$=\']]','[[\'+$+$=$msup\'], [\'+$+$=\', \'+$=$msup\'], [\'+$+\', \'+$=\', \'=$msup\'], [\'+\', \'+\', \'=\', \'msup\']]',1,'[]','[\'var\', \'msup$var\']',70),(1243,'\\alpha^2 + \\beta^2','[\'msup$cn\']','[[], [\'msup$+$msup\'], [\'msup$+\', \'+$msup\']]','[[], [\'+$msup$msup\'], [\'+$msup\', \'msup$msup\'], [\'+\', \'msup\', \'msup\']]',1,'[]','[\'msup$var\']',70),(1244,'\\alpha','[]','[]','[]',1,'[]','[\'var\']',70),(1245,'\\beta','[]','[]','[]',1,'[]','[\'var\']',70);
/*!40000 ALTER TABLE `meas_models_formula` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meas_models_formulaindex`
--

DROP TABLE IF EXISTS `meas_models_formulaindex`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meas_models_formulaindex` (
  `indexkey` varchar(255) NOT NULL,
  `docsids` longtext,
  `df` int(10) unsigned NOT NULL,
  PRIMARY KEY (`indexkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meas_models_formulaindex`
--

LOCK TABLES `meas_models_formulaindex` WRITE;
/*!40000 ALTER TABLE `meas_models_formulaindex` DISABLE KEYS */;
INSERT INTO `meas_models_formulaindex` VALUES ('(','#1139#1149#1151#1152#1156#1166#1168#1173#1176#1198#1212#1236#',12),('($(','#1139#1152#1166#1168#',4),('($($)','#1139#1152#1166#1168#',4),('($($)$)','#1139#1152#1166#1168#',4),('($)','#1139#1149#1151#1152#1156#1166#1168#1173#1176#1198#1212#1236#',12),('($)$)','#1139#1152#1166#1168#',4),('($)$)$+','#1139#1152#1166#1168#',4),('($)$+','#1149#1151#1176#1198#1212#',5),('($)$+$+','#1149#1212#',2),('($)$+$=','#1151#1176#1198#',3),('($)$=','#1173#1236#',2),('($)$=$cos','#1236#',1),('($)$=$−','#1173#',1),('($)$msup','#1156#',1),('($)$msup$−','#1156#',1),('($+','#1139#1151#1152#1166#1168#',5),('($+$)','#1139#1151#1152#1166#1168#',5),('($+$)$(','#1139#1152#1166#1168#',4),('($cos','#1236#',1),('($cos$−','#1236#',1),('($cos$−$sin','#1236#',1),('($−','#1149#1156#1166#1168#1173#1176#1198#1212#',8),('($−$)','#1149#1156#1166#1168#1173#1176#1198#1212#',8),('($−$)$+','#1149#1212#',2),('($−$)$=','#1166#1168#1173#',3),('($−$)$−','#1198#',1),(')','#1139#1149#1151#1152#1156#1166#1168#1173#1176#1198#1212#1236#',12),(')$(','#1139#1152#1166#1168#',4),(')$($+','#1139#1152#',2),(')$($+$)','#1139#1152#',2),(')$($−','#1166#1168#',2),(')$($−$)','#1166#1168#',2),(')$)','#1139#1152#1166#1168#',4),(')$)$+','#1139#1152#1166#1168#',4),(')$)$+$+','#1139#1152#',2),(')$)$+$=','#1166#1168#',2),(')$+','#1139#1149#1151#1152#1166#1168#1176#1198#1212#',9),(')$+$+','#1139#1149#1152#1212#',4),(')$+$+$+','#1212#',1),(')$+$+$=','#1149#1212#',2),(')$+$=','#1149#1151#1166#1168#1176#1198#',6),(')$+$=$mfrac','#1151#',1),(')$+$=$msup','#1176#1198#',2),(')$+$=$−','#1166#1168#',2),(')$=','#1166#1168#1173#1236#',4),(')$=$cos','#1236#',1),(')$=$cos$msup','#1236#',1),(')$=$−','#1166#1168#1173#1236#',4),(')$=$−$sin','#1236#',1),(')$=$−$−','#1168#1173#',2),(')$msup','#1156#',1),(')$msup$−','#1156#',1),(')$−','#1198#',1),(')$−$=','#1198#',1),('+','#1135#1138#1139#1140#1143#1149#1151#1152#1154#1155#1161#1164#1165#1166#1167#1168#1169#1171#1172#1175#1176#1179#1180#1183#1185#1187#1189#1191#1192#1193#1198#1200#1207#1212#1213#1214#1219#1221#1222#1223#1227#1228#1234#1238#1240#1241#1242#1243#',48),('+$(','#1149#1198#1212#',3),('+$($−','#1149#1198#1212#',3),('+$($−$)','#1149#1198#1212#',3),('+$)','#1139#1151#1152#1166#1168#',5),('+$)$(','#1139#1152#1166#1168#',4),('+$)$($+','#1139#1152#',2),('+$)$($−','#1166#1168#',2),('+$+','#1135#1138#1139#1149#1152#1154#1175#1185#1189#1192#1200#1212#1223#1242#',14),('+$+$+','#1212#',1),('+$+$+$=','#1212#',1),('+$+$=','#1135#1138#1149#1154#1175#1185#1200#1212#1223#1242#',10),('+$+$=$msup','#1135#1138#1149#1154#1175#1185#1200#1212#1223#1242#',10),('+$+$msup','#1189#1192#',2),('+$+$msup$−','#1189#',1),('+$+$−','#1189#',1),('+$=','#1135#1138#1143#1149#1151#1154#1164#1166#1167#1168#1169#1171#1172#1175#1176#1179#1180#1183#1185#1193#1198#1200#1207#1212#1213#1214#1219#1223#1238#1240#1241#1242#',32),('+$=$(','#1176#',1),('+$=$($−','#1176#',1),('+$=$cos','#1238#1240#',2),('+$=$cos$mfrac','#1238#1240#',2),('+$=$mfrac','#1151#1241#',2),('+$=$mfrac$msup','#1151#1241#',2),('+$=$msup','#1135#1138#1143#1149#1154#1164#1167#1169#1171#1172#1175#1176#1180#1183#1185#1193#1198#1200#1207#1212#1213#1214#1219#1223#1242#',25),('+$=$msup$msup','#1171#1175#1214#',3),('+$=$msup$−','#1143#1149#1164#1167#1169#1172#1176#1183#1185#1198#1207#1212#1213#1219#',14),('+$=$−','#1166#1168#',2),('+$=$−$−','#1166#1168#',2),('+$>','#1187#1191#',2),('+$>$msup','#1187#1191#',2),('+$>$msup$−','#1187#1191#',2),('+$>$−','#1187#',1),('+$cos','#1227#1228#1234#1238#1240#',5),('+$cos$=','#1240#',1),('+$cos$=$tan','#1240#',1),('+$cos$sin','#1227#1228#1234#',3),('+$mfrac','#1140#1155#1222#',3),('+$mfrac$mfrac','#1140#1155#',2),('+$mfrac$[','#1222#',1),('+$mfrac$[$]','#1222#',1),('+$msup','#1161#1165#1171#1175#1189#1192#1214#1221#1241#1243#',10),('+$msup$=','#1171#1175#1214#',3),('+$msup$=$+','#1175#',1),('+$msup$=$−','#1171#',1),('+$msup$msup','#1161#1221#1243#',3),('+$msup$msup$−','#1161#',1),('+$msup$tan','#1241#',1),('+$msup$tan$−','#1241#',1),('+$msup$−','#1165#1189#',2),('+$msup$−$−','#1189#',1),('+$msup$−$≥','#1165#',1),('+$sin','#1227#1234#',2),('+$[','#1222#',1),('+$[$]','#1222#',1),('+$[$]$mfrac','#1222#',1),('+$−','#1143#1161#1165#1169#1183#1185#1189#1213#',8),('+$−$+','#1185#',1),('+$−$=','#1143#1213#',2),('+$−$msup','#1161#',1),('+$−$msup$−','#1161#',1),('+$−$≥','#1165#',1),('.','#1134#1137#',2),('.$=','#1134#1137#',2),('.$=$msqrt','#1134#1137#',2),('.$=$msqrt$msup','#1134#1137#',2),('=','#1134#1135#1137#1138#1143#1145#1149#1151#1154#1158#1163#1164#1166#1167#1168#1169#1171#1172#1173#1175#1176#1179#1180#1183#1185#1193#1196#1198#1199#1200#1203#1207#1212#1213#1214#1219#1223#1232#1236#1237#1238#1239#1240#1241#1242#',45),('=$(','#1176#',1),('=$($−','#1176#',1),('=$($−$)','#1176#',1),('=$+','#1169#1175#1179#1193#',4),('=$+$−','#1169#',1),('=$cos','#1232#1236#1238#1239#1240#',5),('=$cos$cos','#1239#',1),('=$cos$cos$msup','#1239#',1),('=$cos$mfrac','#1238#1240#',2),('=$cos$mfrac$mfrac','#1238#',1),('=$cos$mfrac$sin','#1240#',1),('=$cos$msup','#1236#',1),('=$cos$msup$sin','#1236#',1),('=$cos$sin','#1232#',1),('=$cos$sin$−','#1232#',1),('=$e','#1237#',1),('=$e$e','#1237#',1),('=$e$e$mfrac','#1237#',1),('=$mfrac','#1151#1238#1241#',3),('=$mfrac$+','#1238#',1),('=$mfrac$+$cos','#1238#',1),('=$mfrac$msup','#1151#1241#',2),('=$mfrac$msup$(','#1151#',1),('=$mfrac$msup$msup','#1241#',1),('=$msqrt','#1134#1137#',2),('=$msqrt$msup','#1134#1137#',2),('=$msqrt$msup$−','#1134#1137#',2),('=$msup','#1135#1138#1143#1145#1149#1154#1158#1164#1167#1169#1171#1172#1175#1176#1180#1183#1185#1193#1196#1198#1199#1200#1203#1207#1212#1213#1214#1219#1223#1242#',30),('=$msup$+','#1185#',1),('=$msup$+$−','#1185#',1),('=$msup$msup','#1171#1175#1214#',3),('=$msup$msup$−','#1171#1175#',2),('=$msup$−','#1143#1145#1149#1158#1164#1167#1169#1172#1176#1183#1185#1196#1198#1203#1207#1212#1213#1219#',18),('=$msup$−$+','#1164#1183#',2),('=$msup$−$−','#1158#1183#1198#1203#1213#',5),('=$sec','#1241#',1),('=$tan','#1240#',1),('=$−','#1134#1137#1145#1163#1166#1168#1171#1173#1196#1236#',10),('=$−$msqrt','#1134#1137#',2),('=$−$msqrt$msup','#1134#1137#',2),('=$−$sin','#1236#',1),('=$−$−','#1166#1168#1173#',3),('=$−$−$−','#1168#',1),('>','#1177#1187#1191#',3),('>$+','#1191#',1),('>$msup','#1187#1191#',2),('>$msup$−','#1187#1191#',2),('>$−','#1177#1187#',2),('cn','#1133#1135#1136#1138#1143#1145#1149#1154#1158#1161#1163#1164#1165#1166#1167#1168#1169#1171#1172#1173#1175#1176#1179#1183#1185#1187#1189#1191#1192#1193#1196#1198#1199#1200#1201#1203#1207#1212#1213#1219#1223#1227#1228#1232#1236#1237#1239#1241#1242#',49),('cos','#1227#1228#1232#1234#1235#1236#1238#1239#1240#',9),('cos$+','#1227#1234#',2),('cos$+$sin','#1227#1234#',2),('cos$=','#1240#',1),('cos$=$tan','#1240#',1),('cos$cos','#1239#',1),('cos$cos$msup','#1239#',1),('cos$cos$msup$msup','#1239#',1),('cos$mfrac','#1238#1240#',2),('cos$mfrac$mfrac','#1238#',1),('cos$mfrac$mfrac$msup','#1238#',1),('cos$mfrac$sin','#1240#',1),('cos$mfrac$sin$tan','#1240#',1),('cos$msup','#1236#1239#',2),('cos$msup$msup','#1239#',1),('cos$msup$msup$sin','#1239#',1),('cos$msup$sin','#1236#',1),('cos$msup$sin$sin','#1236#',1),('cos$sin','#1227#1228#1232#1234#1235#',5),('cos$sin$−','#1232#1235#',2),('cos$−','#1232#1235#1236#1239#',4),('cos$−$msup','#1239#',1),('cos$−$msup$sin','#1239#',1),('cos$−$sin','#1232#1235#1236#',3),('cos$−$sin$)','#1236#',1),('cos$−$sin$=','#1232#',1),('e','#1237#',1),('e$e','#1237#',1),('e$e$mfrac','#1237#',1),('e$e$mfrac$msup','#1237#',1),('e$mfrac','#1237#',1),('e$mfrac$msup','#1237#',1),('e$mfrac$msup$tan','#1237#',1),('e$msup','#1237#',1),('e$msup$tan','#1237#',1),('e$msup$tan$=','#1237#',1),('mfrac','#1140#1151#1155#1204#1209#1222#1237#1238#1240#1241#',10),('mfrac$+','#1140#1155#1222#1238#1241#',5),('mfrac$+$cos','#1238#',1),('mfrac$+$mfrac','#1140#1155#1222#',3),('mfrac$+$mfrac$[','#1222#',1),('mfrac$+$msup','#1241#',1),('mfrac$+$msup$tan','#1241#',1),('mfrac$=','#1238#',1),('mfrac$=$mfrac','#1238#',1),('mfrac$=$mfrac$+','#1238#',1),('mfrac$e','#1237#',1),('mfrac$e$msup','#1237#',1),('mfrac$e$msup$tan','#1237#',1),('mfrac$mfrac','#1140#1155#1222#1238#',4),('mfrac$mfrac$msup','#1238#',1),('mfrac$mfrac$msup$sec','#1238#',1),('mfrac$mrow$+','#1238#1240#1241#',3),('mfrac$mrow$cn','#1140#1151#1155#1177#1214#1222#1238#1240#1241#',9),('mfrac$mrow$cos','#1238#1240#',2),('mfrac$mrow$e','#1237#',1),('mfrac$mrow$msup','#1151#1237#1241#',3),('mfrac$mrow$msup$cn','#1151#1237#1241#',3),('mfrac$mrow$msup$mrow$(','#1151#',1),('mfrac$mrow$msup$mrow$)','#1151#',1),('mfrac$mrow$msup$mrow$+','#1151#',1),('mfrac$mrow$msup$mrow$cn','#1151#',1),('mfrac$mrow$msup$mrow$var','#1151#',1),('mfrac$mrow$msup$tan','#1241#',1),('mfrac$mrow$msup$var','#1237#',1),('mfrac$mrow$sin','#1240#',1),('mfrac$mrow$tan','#1237#',1),('mfrac$mrow$var','#1140#1155#1204#1209#1222#1237#1238#1240#1241#',9),('mfrac$mrow$−','#1241#',1),('mfrac$msup','#1151#1237#1238#1241#',4),('mfrac$msup$(','#1151#',1),('mfrac$msup$($+','#1151#',1),('mfrac$msup$msup','#1241#',1),('mfrac$msup$msup$sec','#1241#',1),('mfrac$msup$sec','#1238#',1),('mfrac$msup$tan','#1237#',1),('mfrac$sin','#1240#',1),('mfrac$sin$+','#1240#',1),('mfrac$sin$+$cos','#1240#',1),('mfrac$sin$tan','#1240#',1),('mfrac$[','#1222#',1),('mfrac$[$]','#1222#',1),('mrow$(','#1139#1149#1152#1166#1168#1173#1176#1198#1212#',9),('mrow$)','#1139#1149#1152#1166#1168#1173#1176#1198#1212#',9),('mrow$+','#1139#1152#1166#1168#',4),('mrow$cn','#1134#1137#1139#1149#1152#1166#1168#1173#1176#1198#1212#1222#',12),('mrow$e','#1237#',1),('mrow$msqrt','#1134#1137#',2),('mrow$msqrt$mrow$cn','#1134#1137#',2),('mrow$msqrt$mrow$msup','#1134#1137#',2),('mrow$msqrt$mrow$msup$cn','#1134#1137#',2),('mrow$msqrt$mrow$msup$var','#1134#1137#',2),('mrow$msqrt$mrow$var','#1134#1137#',2),('mrow$msqrt$mrow$−','#1134#1137#',2),('mrow$var','#1134#1137#1139#1149#1152#1166#1168#1173#1176#1198#1212#1237#',12),('mrow$[','#1222#',1),('mrow$]','#1222#',1),('mrow$−','#1134#1137#1149#1166#1168#1173#1176#1198#1212#',9),('msqrt','#1134#1137#',2),('msqrt$mrow$cn','#1235#',1),('msqrt$msup','#1134#1137#',2),('msqrt$msup$−','#1134#1137#',2),('msqrt$msup$−$.','#1134#1137#',2),('msqrt$msup$−$−','#1134#1137#',2),('msup','#1134#1135#1137#1138#1143#1144#1145#1146#1149#1151#1154#1156#1158#1161#1164#1165#1167#1169#1171#1172#1175#1176#1180#1183#1185#1187#1189#1191#1192#1193#1196#1198#1199#1200#1203#1207#1212#1213#1214#1218#1219#1220#1221#1223#1236#1237#1238#1239#1241#1242#1243#',51),('msup$(','#1151#1156#1236#',3),('msup$($+','#1151#',1),('msup$($+$)','#1151#',1),('msup$($cos','#1236#',1),('msup$($cos$−','#1236#',1),('msup$($−','#1156#',1),('msup$($−$)','#1156#',1),('msup$+','#1135#1138#1143#1149#1154#1161#1165#1171#1176#1180#1185#1187#1189#1192#1198#1200#1212#1214#1221#1223#1242#1243#',22),('msup$+$(','#1149#1198#1212#',3),('msup$+$($−','#1149#1198#1212#',3),('msup$+$+','#1135#1138#1154#1189#1192#1200#1223#1242#',8),('msup$+$+$=','#1135#1138#1154#1200#1223#1242#',6),('msup$+$+$−','#1189#',1),('msup$+$=','#1176#1180#',2),('msup$+$=$(','#1176#',1),('msup$+$>','#1187#',1),('msup$+$>$−','#1187#',1),('msup$+$msup','#1171#1214#1221#1243#',4),('msup$+$msup$=','#1171#1214#',2),('msup$+$−','#1143#1161#1165#1185#',4),('msup$+$−$+','#1185#',1),('msup$+$−$=','#1143#',1),('msup$+$−$msup','#1161#',1),('msup$+$−$≥','#1165#',1),('msup$=','#1145#1169#1171#1175#1193#1196#1199#1214#',8),('msup$=$+','#1169#1175#1193#',3),('msup$=$+$−','#1169#',1),('msup$=$−','#1145#1171#1196#',3),('msup$cn','#1135#1138#1143#1144#1145#1146#1149#1154#1156#1158#1161#1164#1165#1167#1169#1171#1172#1175#1176#1180#1183#1185#1187#1189#1191#1192#1193#1196#1198#1199#1200#1203#1207#1212#1213#1214#1218#1219#1220#1221#1223#1230#1231#1233#1236#1238#1239#1242#1243#',49),('msup$cos','#1239#',1),('msup$cos$−','#1239#',1),('msup$cos$−$msup','#1239#',1),('msup$mrow$(','#1156#1236#',2),('msup$mrow$)','#1156#1236#',2),('msup$mrow$cos','#1236#',1),('msup$mrow$sin','#1236#',1),('msup$mrow$var','#1156#1236#',2),('msup$mrow$−','#1156#1236#',2),('msup$msup','#1161#1171#1175#1214#1221#1239#1241#1243#',8),('msup$msup$sec','#1241#',1),('msup$msup$sec$tan','#1241#',1),('msup$msup$sin','#1239#',1),('msup$msup$sin$−','#1239#',1),('msup$msup$−','#1161#1171#1175#',3),('msup$msup$−$−','#1161#',1),('msup$sec','#1238#1241#',2),('msup$sec$mfrac','#1238#',1),('msup$sec$mfrac$=','#1238#',1),('msup$sec$tan','#1241#',1),('msup$sec$tan$tan','#1241#',1),('msup$sin','#1236#1239#',2),('msup$sin$=','#1239#',1),('msup$sin$=$cos','#1239#',1),('msup$sin$sin','#1236#',1),('msup$sin$sin$−','#1236#',1),('msup$sin$−','#1239#',1),('msup$tan','#1237#1241#',2),('msup$tan$=','#1237#1241#',2),('msup$tan$=$e','#1237#',1),('msup$tan$=$sec','#1241#',1),('msup$tan$−','#1241#',1),('msup$tan$−$msup','#1241#',1),('msup$var','#1135#1138#1143#1144#1145#1146#1149#1154#1158#1161#1164#1165#1167#1169#1171#1172#1175#1176#1180#1183#1185#1187#1189#1191#1192#1193#1196#1198#1199#1200#1203#1207#1212#1213#1214#1218#1219#1220#1221#1223#1242#1243#',42),('msup$−','#1134#1137#1143#1145#1149#1156#1158#1161#1164#1165#1167#1169#1171#1172#1175#1176#1183#1185#1187#1189#1191#1196#1198#1203#1207#1212#1213#1219#',28),('msup$−$+','#1164#1167#1172#1175#1183#1207#1213#1219#',8),('msup$−$+$=','#1167#1172#1207#1219#',4),('msup$−$+$msup','#1175#',1),('msup$−$+$−','#1183#1213#',2),('msup$−$.','#1134#1137#',2),('msup$−$>','#1191#',1),('msup$−$>$+','#1191#',1),('msup$−$−','#1134#1137#1158#1161#1183#1189#1198#1203#1213#',9),('msup$−$−$=','#1158#1203#',2),('msup$−$−$−','#1161#',1),('msup$−$≥','#1165#',1),('msup$∘','#1230#1231#1233#',3),('sec','#1238#1241#',2),('sec$mfrac','#1238#',1),('sec$mfrac$=','#1238#',1),('sec$mfrac$=$mfrac','#1238#',1),('sec$tan','#1241#',1),('sec$tan$tan','#1241#',1),('sec$tan$tan$−','#1241#',1),('sin','#1227#1228#1232#1234#1235#1236#1239#1240#',8),('sin$)','#1236#',1),('sin$)$=','#1236#',1),('sin$)$=$−','#1236#',1),('sin$+','#1228#1240#',2),('sin$+$cos','#1228#1240#',2),('sin$+$cos$=','#1240#',1),('sin$=','#1232#1239#',2),('sin$=$cos','#1239#',1),('sin$sin','#1236#',1),('sin$sin$−','#1236#',1),('sin$sin$−$−','#1236#',1),('sin$tan','#1240#',1),('sin$−','#1232#1235#1236#1239#',4),('sin$−$−','#1236#',1),('tan','#1237#1240#1241#',3),('tan$=','#1237#1241#',2),('tan$=$e','#1237#',1),('tan$=$sec','#1241#',1),('tan$tan','#1241#',1),('tan$tan$−','#1241#',1),('tan$−','#1241#',1),('tan$−$msup','#1241#',1),('tan$−$msup$tan','#1241#',1),('var','#1133#1134#1135#1136#1137#1138#1141#1142#1143#1145#1147#1148#1149#1150#1151#1153#1154#1157#1158#1159#1160#1161#1162#1163#1164#1165#1166#1167#1168#1169#1170#1171#1172#1173#1174#1175#1176#1177#1178#1179#1180#1181#1182#1183#1184#1185#1186#1187#1188#1189#1190#1191#1192#1193#1194#1195#1196#1197#1198#1199#1200#1201#1202#1203#1205#1206#1207#1208#1210#1211#1212#1213#1215#1216#1217#1219#1223#1224#1225#1226#1227#1228#1229#1230#1232#1234#1235#1236#1237#1239#1240#1241#1242#1244#1245#',95),('[','#1222#',1),('[$]','#1222#',1),('[$]$mfrac','#1222#',1),('[$]$mfrac$mfrac','#1222#',1),(']','#1222#',1),(']$mfrac','#1222#',1),(']$mfrac$mfrac','#1222#',1),('−','#1134#1137#1143#1145#1149#1156#1158#1161#1163#1164#1165#1166#1167#1168#1169#1171#1172#1173#1175#1176#1177#1183#1185#1187#1189#1191#1196#1198#1203#1207#1212#1213#1219#1232#1235#1236#1239#1241#',38),('−$)','#1149#1156#1166#1168#1173#1176#1198#1212#',8),('−$)$+','#1149#1212#',2),('−$)$+$+','#1212#',1),('−$)$+$=','#1149#',1),('−$)$=','#1166#1168#1173#',3),('−$)$=$−','#1166#1168#1173#',3),('−$)$−','#1198#',1),('−$)$−$=','#1198#',1),('−$+','#1164#1167#1172#1175#1183#1185#1207#1213#1219#',9),('−$+$=','#1167#1172#1207#1219#',4),('−$+$msup','#1175#',1),('−$+$msup$=','#1175#',1),('−$+$−','#1183#1213#',2),('−$+$−$=','#1213#',1),('−$.','#1134#1137#',2),('−$=','#1143#1158#1198#1203#1213#',5),('−$>','#1191#',1),('−$>$+','#1191#',1),('−$msqrt','#1134#1137#',2),('−$msqrt$msup','#1134#1137#',2),('−$msqrt$msup$−','#1134#1137#',2),('−$msup','#1161#1189#1239#1241#',4),('−$msup$+','#1161#1189#',2),('−$msup$+$+','#1189#',1),('−$msup$+$−','#1161#',1),('−$msup$sin','#1239#',1),('−$msup$sin$=','#1239#',1),('−$msup$tan','#1241#',1),('−$msup$tan$=','#1241#',1),('−$msup$−','#1161#',1),('−$sin','#1232#1235#1236#',3),('−$sin$)','#1236#',1),('−$sin$)$=','#1236#',1),('−$sin$=','#1232#',1),('−$−','#1134#1137#1158#1161#1166#1168#1173#1183#1189#1198#1203#1213#1236#',13),('−$−$=','#1158#1203#',2),('−$−$−','#1161#1168#',2),('−$≥','#1165#',1),('∘','#1230#1231#1233#',3),('∘$∘','#1230#',1),('∘$∘$≤','#1230#',1),('∘$∘$≤$≤','#1230#',1),('∘$≤','#1230#',1),('∘$≤$≤','#1230#',1),('∘$≤$≤$∘','#1230#',1),('≠','#1133#1136#',2),('≤','#1230#',1),('≤$∘','#1230#',1),('≤$≤','#1230#',1),('≤$≤$∘','#1230#',1),('≥','#1165#',1);
/*!40000 ALTER TABLE `meas_models_formulaindex` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meas_models_keypoint`
--

DROP TABLE IF EXISTS `meas_models_keypoint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meas_models_keypoint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `concept_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `meas_models_keypoi_concept_id_c65b7b8f_fk_meas_models_concept_id` (`concept_id`),
  CONSTRAINT `meas_models_keypoi_concept_id_c65b7b8f_fk_meas_models_concept_id` FOREIGN KEY (`concept_id`) REFERENCES `meas_models_concept` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meas_models_keypoint`
--

LOCK TABLES `meas_models_keypoint` WRITE;
/*!40000 ALTER TABLE `meas_models_keypoint` DISABLE KEYS */;
INSERT INTO `meas_models_keypoint` VALUES (2,'Key point 1  for test','Content 1',2),(3,'Key point 1  for test','Content 1',3),(5,'Key point 1  for test','Content 1',2),(6,'Key point 1  for test','Content 1',3),(8,'test','test',11),(12,'Sum-of-Roots','Given that the equation $ax^2+bx+c=0$ has 2 roots $\\alpha$ and $\\beta$, the sum of roots, $\\alpha+\\beta = -\\frac{b}{a}$',17),(13,'Product-of-Roots','Given that the equation $ax^2+bx+c=0$ has 2 roots $\\alpha$ and $\\beta$, the product of roots, $\\alpha\\beta =\\frac{c}{a}$',17),(18,'Always positive','a>0 , $b^2-4ac<0$',19),(19,'Always negative','a<0 , $b^2-4ac<0$',19),(20,'No intersection','$b^2-4ac<0$',20),(21,'The line is a tangent to the curve','$b^2-4ac=0$',20),(22,'Intersection at 2 different points','$b^2-4ac>0$',20),(41,'Sine Addition Formulae','$\\sin (A \\pm B) = \\sin A \\cos B \\pm \\cos A \\sin B$',24),(42,'Cosine Addition Formulae','$\\cos (A \\pm B) = \\cos A \\cos B \\mp \\sin A \\sin B$',24),(43,'Tangent Addition Formulae','$\\tan (A \\pm B) = \\frac{\\tan A \\pm \\tan B}{1\\mp \\tan A\\tan B}$',24),(49,'The-Sine-R-Formulae','For $a>0$, $b>0$ and $\\alpha$ is acute, we have $a \\sin \\theta \\pm b \\cos \\theta = R \\sin (\\theta \\pm \\alpha)$ , where $R=\\sqrt{a^2+b^2}$ and $\\tan \\alpha = \\frac{b}{a}$.',26),(50,'The-Cosine-R-Formulae','For $a>0$, $b>0$ and $\\alpha$ is acute, we have $a \\cos \\theta \\pm b \\sin \\theta = R \\cos (\\theta \\mp \\alpha)$ , where $R=\\sqrt{a^2+b^2}$ and $\\tan \\alpha = \\frac{b}{a}$.',26),(51,'2-distinct-real-roots','$b^2-4ac>0$',18),(52,'2-equal-roots','$b^2-4ac=0$',18),(53,'No-real-roots','$b^2-4ac<0$',18),(54,'2-real-roots','$b^2-4ac \\geq 0$',18),(55,'Pythagorean Identity 1','$\\sin^2 \\theta +\\cos^2 \\theta = 1$',23),(56,'Pythagorean Identity 2','$1+\\tan^2 \\theta = \\sec^2 \\theta$',23),(57,'Pythagorean Identity 3','$1+\\cot^2 \\theta = cosec^2 \\theta$',23),(70,'Sine-Double-Angle','$\\sin 2A = 2\\sin A \\cos A$',25),(71,'Cosine-Double-Angle','$\\cos 2A = \\cos^2 A - \\sin^2 A = 2\\cos^2 A -1 = 1-2\\sin^2 A$',25),(72,'Tangent-Double-Angle','$\\tan 2A = \\frac{2\\tan A}{1-\\tan^2 A}$',25);
/*!40000 ALTER TABLE `meas_models_keypoint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meas_models_paper`
--

DROP TABLE IF EXISTS `meas_models_paper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meas_models_paper` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `month` varchar(20) NOT NULL,
  `number` int(11) NOT NULL,
  `no_of_question` int(11) DEFAULT NULL,
  `subject_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `meas_models_paper_ffaba1d1` (`subject_id`),
  CONSTRAINT `meas_models_paper_subject_id_e2f65402_fk_meas_models_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `meas_models_subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meas_models_paper`
--

LOCK TABLES `meas_models_paper` WRITE;
/*!40000 ALTER TABLE `meas_models_paper` DISABLE KEYS */;
INSERT INTO `meas_models_paper` VALUES (8,1997,'6',1,0,1),(9,1997,'6',2,0,1),(10,1997,'11',1,0,1),(11,1997,'11',2,0,1),(12,1998,'6',1,0,1),(13,1998,'6',2,0,1),(14,1998,'11',1,0,1),(15,1998,'11',2,0,1),(16,1999,'6',1,0,1),(17,1999,'6',2,0,1),(18,1999,'11',1,0,1),(19,1999,'11',2,0,1),(20,2000,'6',1,0,1),(21,2000,'6',2,0,1),(22,2000,'11',1,0,1),(23,2000,'11',2,0,1),(24,2001,'6',1,0,1),(26,2001,'11',1,0,1),(27,2001,'11',2,0,1),(28,2002,'6',1,0,1),(29,2002,'6',2,0,1),(30,2002,'11',1,0,1),(31,2002,'11',2,0,1),(32,2003,'6',1,0,1),(33,2003,'6',2,0,1),(34,2003,'11',1,0,1),(35,2003,'11',2,0,1),(36,2004,'11',1,0,1),(37,2004,'11',2,0,1),(38,2005,'11',1,0,1),(39,2005,'11',2,0,1),(40,2006,'11',1,0,1),(41,2005,'11',2,0,1),(42,2007,'11',1,0,1),(43,2007,'11',2,0,1),(44,2008,'11',1,0,1),(45,2008,'11',2,0,1),(46,2009,'11',1,0,1),(47,2009,'11',2,0,1),(48,2010,'11',1,0,1),(49,2010,'11',2,0,1),(50,2015,'11',1,0,1),(51,2015,'11',2,0,1);
/*!40000 ALTER TABLE `meas_models_paper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meas_models_question`
--

DROP TABLE IF EXISTS `meas_models_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meas_models_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_type` varchar(2) NOT NULL,
  `used_for` varchar(2) NOT NULL,
  `mark` int(11) NOT NULL,
  `difficulty_level` varchar(1) NOT NULL,
  `respone_type` varchar(10) NOT NULL,
  `content` longtext NOT NULL,
  `solution` longtext NOT NULL,
  `concept_id` int(11) NOT NULL,
  `keypoint_id` int(11) DEFAULT NULL,
  `paper_id` int(11) DEFAULT NULL,
  `answer` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `meas_models_questi_concept_id_2821a4c0_fk_meas_models_concept_id` (`concept_id`),
  KEY `meas_models_ques_keypoint_id_bb366db4_fk_meas_models_keypoint_id` (`keypoint_id`),
  KEY `meas_models_question_paper_id_86003a5f_fk_meas_models_paper_id` (`paper_id`),
  CONSTRAINT `meas_models_ques_keypoint_id_bb366db4_fk_meas_models_keypoint_id` FOREIGN KEY (`keypoint_id`) REFERENCES `meas_models_keypoint` (`id`),
  CONSTRAINT `meas_models_questi_concept_id_2821a4c0_fk_meas_models_concept_id` FOREIGN KEY (`concept_id`) REFERENCES `meas_models_concept` (`id`),
  CONSTRAINT `meas_models_question_paper_id_86003a5f_fk_meas_models_paper_id` FOREIGN KEY (`paper_id`) REFERENCES `meas_models_paper` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meas_models_question`
--

LOCK TABLES `meas_models_question` WRITE;
/*!40000 ALTER TABLE `meas_models_question` DISABLE KEYS */;
INSERT INTO `meas_models_question` VALUES (4,'EX','NO',1,'1','Text','<pre>\r\nWhen $a \\ne 0$, there are two solutions to \\(ax^2 + bx + c = 0\\) and they are\r\n$$x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}.$$</pre>\r\n','<pre>\r\nWhen $a \\ne 0$, there are two solutions to \\(ax^2 + bx + c = 0\\) and they are\r\n$$x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}.$$</pre>\r\n',2,2,NULL,'Test'),(5,'PR','ON',1,'1','Text','When $a \\ne 0$, there are two solutions to \\(ax^2 + bx + c = 0\\) and they are </br>\r\n$x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}.$','<pre>\r\nWhen $a \\ne 0$, there are two solutions to \\(ax^2 + bx + c = 0\\) and they are\r\n$x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}.$</pre>\r\n',2,2,NULL,'Test'),(8,'PR','ON',2,'1','Text','<p>test phuc</p>\r\n','<p>test phuc</p>\r\n',2,2,NULL,'Test'),(11,'PR','NO',3,'1','Text','<p>test</p>\r\n','<p>test</p>\r\n',2,NULL,NULL,'Test'),(12,'PR','ON',1,'1','Text','<p>abc</p>\r\n','<p>abc</p>\r\n',3,NULL,NULL,'Test'),(13,'EX','NO',0,'1','Text','<p>phuctest</p>\r\n','<p>phuctest</p>\r\n',2,NULL,NULL,'Test'),(14,'PR','NO',0,'1','Text','<p>phuctest</p>\r\n','<p>phuctest</p>\r\n',2,NULL,NULL,'Test'),(15,'PR','NO',0,'1','Text','<p>The equation $2x^2+6x-3=0$ has roots $\\alpha$ and $\\beta$. Find the values of</p>\r\n\r\n<p>(a) $\\frac{1}{\\alpha}+\\frac{1}{\\beta}$</p> \r\n\r\n<p>(b) $(2\\alpha+1)(2\\beta+1)$</p> \r\n ','For $2x^2+6x-3=0$, </br>\r\nsum of roots = $\\alpha+\\beta= -\\frac{b}{a}= - \\frac{6}{2}= -3$</br>\r\nproduct of roots = $\\alpha \\beta = \\frac{c}{a} = \\frac{-3}{2}= - \\frac{3}{2}$</br>\r\n(a) $\\frac{1}{\\alpha}+\\frac{1}{\\beta}=\\frac{\\alpha+\\beta}{\\alpha \\beta}= \\frac{-3}{- \\frac{3}{2}}=2$</br>\r\n\r\n(b) \r\n\\begin{align*}\r\n(2\\alpha+1)(2\\beta+1)&= 4\\alpha \\beta + 2\\alpha + 2\\beta + 1\\\\\r\n				&= 4\\alpha \\beta + 2 (\\alpha +\\beta) + 1\\\\\r\n				&= 4\\left(-\\frac{3}{2}\\right)+2(-3)+1\\\\\r\n				&= -11\\\\\r\n\\end{align*}\r\n\r\n',17,12,NULL,'Test'),(16,'PR','NO',0,'1','Text','<p>The equation $2x^2=1-4x$ has roots $\\alpha$ and $\\beta$. Form an equation (with integer coefficients) whose roots are $\\alpha^2$ and $\\beta^2$.</p>\r\n','<pre>\r\nFor $2x^2=1-4x$, that is, $2x^2+4x-1=0$,\\\\</pre>\r\n\r\n<pre>\r\n$\\alpha+\\beta=-\\frac{4}{2}=-2$\\\\</pre>\r\n\r\n<pre>\r\nand</pre>\r\n\r\n<pre>\r\n$\\alpha\\beta=\\frac{-1}{2}=-\\frac{1}{2}$\\\\</pre>\r\n\r\n<pre>\r\nFor the new equation,</pre>\r\n\r\n<pre>\r\n\\begin{align*}</pre>\r\n\r\n<pre>\r\n\\text{sum of roots} &amp;= \\alpha^2 + \\beta^2\\\\</pre>\r\n\r\n<pre>\r\n					&amp;= (\\alpha^2+\\beta^2+2\\alpha\\beta)-2\\alpha\\beta\\\\</pre>\r\n\r\n<pre>\r\n					&amp;=(\\alpha+\\beta)^2-2\\alpha\\beta\\\\</pre>\r\n\r\n<pre>\r\n					&amp;=(-2)^2-2(-\\frac{1}{2})\\\\</pre>\r\n\r\n<pre>\r\n					&amp;=5</pre>\r\n\r\n<pre>\r\n\\end{align*}</pre>\r\n\r\n<pre>\r\nand</pre>\r\n\r\n<pre>\r\n\\begin{align*}</pre>\r\n\r\n<pre>\r\n\\text{product of roots}&amp;=\\alpha^2 . \\beta^2\\\\</pre>\r\n\r\n<pre>\r\n								   &amp;=(\\alpha\\beta)^2\\\\</pre>\r\n\r\n<pre>\r\n								   &amp;=\\left(\\frac{1}{2}\\right)^2\\\\</pre>\r\n\r\n<pre>\r\n								   &amp;=\\frac{1}{4}</pre>\r\n\r\n<pre>\r\n\\end{align*}</pre>\r\n\r\n<pre>\r\nAn equation with roots $\\alpha^2$ and $\\beta^2$ is,\\\\</pre>\r\n\r\n<pre>\r\n$x^2-(\\text{sum of roots})x+(\\text{product of roots})=0$\\\\</pre>\r\n\r\n<pre>\r\n$x^2-5x+\\frac{1}{4}=0$\\\\</pre>\r\n\r\n<pre>\r\n$4x^2-20x+1=0$</pre>\r\n',17,13,NULL,'Test'),(17,'PR','ON',5,'3','Text','Given that the equation $x^2+(2-k)x+k=0$ has non-zero roots which differ by 2, find the value of each root and of $k$.\r\n','Note that $a=1,b=2-k$ and $c=k$.</br>\r\nLet the roots be $\\alpha$ and $\\alpha+2$.\r\n\\begin{align*}\r\n\\text{Sum of roots} = \\alpha+(\\alpha+2)&=-\\frac{2-k}{1}\\\\\r\n2\\alpha+2&=k-2	& (1)\\\\\r\n\\text{Product of roots} = \\alpha(\\alpha+2)&=\\frac{k}{1}\\\\\r\n\\alpha^2+2\\alpha&=k & (2)\\\\\r\n\\text{For equation (1)},\\\\\r\nk&=2\\alpha+4	& (3)\r\n\\end{align*}\r\nSubstituting equation (3) in equation (2),\r\n\\begin{align*}\r\n\\alpha^2+2\\alpha &=2\\alpha+4\\\\\r\n\\alpha^2 &=4\\\\\r\n\\alpha &= 2 \\> \\text{or  } -2\\\\\r\n\\alpha+2 &= 4 \\> \\text{or   } 0\r\n\\end{align*}\r\nSince the roots are non-zero, the roots are 2 and 4.</br>\r\nSubstituting $\\alpha=2$ in equation (3), we get\r\n\\begin{align*}\r\nk&=2(2)+4\\\\\r\n&=8\r\n\\end{align*}',17,12,NULL,'Test'),(20,'EX','NO',0,'1','Text','\r\nThe equation of a curve is $y=\\frac{36}{(2x+1)^2}$.\r\n','',6,NULL,50,'Test'),(21,'PR','ON',4,'3','Text','<p>The equation $x^2+3x+1=0$ has roots $\\alpha$ and $\\beta$. find the values of</p>\r\n\r\n(a) $\\frac{2}{\\alpha}+\\frac{2}{\\beta}$,</br>\r\n(b) $(\\alpha+3)(\\beta+3)$,</br>\r\n(c) $(\\alpha-\\beta)^2$.','$\\alpha+\\beta=-\\frac{3}{1}=- 3$</br>\r\n$\\alpha\\beta = \\frac{1}{1}=1$</br>\r\n(a) \\begin{align*}\r\n\\frac{2}{\\alpha}+\\frac{2}{\\beta} &= \\frac{2\\beta}{\\alpha\\beta}+\\frac{2\\alpha}{\\alpha\\beta}\\\\\r\n													&= \\frac{2\\beta+2\\alpha}{\\alpha\\beta}\\\\\r\n													&= \\frac{2(\\alpha+\\beta)}{\\alpha\\beta}\\\\\r\n													&= \\frac{2(-3)}{1}\\\\\r\n													&= -6\r\n\\end{align*}\r\n(b)\\begin{align*}\r\n(\\alpha+3)(\\beta+3) &= \\alpha\\beta+3(\\alpha+\\beta)+9\\\\\r\n							   &= (1) + 3(-3) + 9\\\\\r\n							   &= 1\r\n\\end{align*}\r\n(c) \\begin{align*}\r\n(\\alpha-\\beta)^2 &= \\alpha^2-2\\alpha\\beta+\\beta^2\\\\\r\n						 &= \\alpha^2+2\\alpha\\beta+\\beta^2 -4\\alpha\\beta\\\\\r\n						 &= (\\alpha+\\beta)^2-4\\alpha\\beta\\\\\r\n						 &= (-3)^2 - 4(1)\\\\\r\n						 &= 5\r\n\\end{align*}',17,NULL,NULL,'Test'),(22,'PR','NO',5,'1','Text','<p>The equation $2x^2-x-2=0$ has roots $\\alpha$ and $\\beta$. Find the values of</p>\r\n','',17,NULL,NULL,'Test'),(27,'PR','NO',0,'1','Text','Show that $-2x^2+4k-2k^2-1$ is always negative for all values of $k$.','\\begin{align*}\r\nb^2-4ac&=(4k)^2-4(-2)(-2k^2-1)\\\\\r\n&=16k^2-16k^2-8\\\\\r\n&=-8\r\n\\end{align*}\r\nsince $b^2-4ac=-8<0$ and $a=-2<0$, $-2x^2+4kx-2k^2-1$ is always negative.',19,19,NULL,'Test'),(28,'PR','NO',0,'1','Text','If the line $y=mx-8$ meets the curve $y=x^2-5x+m$, show that $m^2+6m-7 \\geq 0$.','By equating the two equations, we get:</br>\r\n$x^2-5x+m=mx-8$</br>\r\n$x^2-(5+m)x+m+8=0$</br>\r\nFor the line to meet the curve, this quadratic equation must have real roots.</br>\r\nSo,</br>\r\n$b^2-4ac \\geq 0$</br>\r\n$(5+m)^2-4(1)(m+8)\\geq 0$</br>\r\n$25+10m+m^2-4m-32 \\geq 0$</br>\r\n$m^2+6m-7 \\geq 0$',20,22,NULL,'Test'),(29,'PR','ON',9,'1','Text','<p>Find the value(s) or range of values of $p$ for which the equation</p>\r\n\r\n<p>(a) $px^2-6x+p=0$ has equal real roots,</p>\r\n\r\n<p>(b) $2x^2-4x+3=p$ has real roots,</p>\r\n\r\n<p>(c) $3x^2=2x+p-1$ has distinct real roots,</p>\r\n\r\n<p>(d) $x^2+p^2=3px-1$ has equal real roots,</p>\r\n\r\n<p>(e) $x(x-2)=x-2p$ has no real roots,</p>\r\n\r\n<p>(f) $(x+1)(2x-1)=p-2$ has two unequal real roots,</p>\r\n\r\n<p>(g) $p(x+1)(x-3)=x-4p-2$ has no real roots.</p>\r\n\r\n\\begin{align} \r\n\r\na&=a^2+2 \\\\\r\na&=\\mapsto wa w +weaw\\\\\r\n\\therefore\r\n\\end{align}','<p>\\begin{itemize} \\item[(a)] $b^2-4ac=0$\\\\ $(-6)^2-4(p)(p)=0$\\\\ $4p^2=36$\\\\ $p=\\pm3$ \\item[(b)] $2x^2-4x+3-p=0$\\\\ $b^2-4ac\\geq 0$\\\\ $(-4)^2-4(2)(3-p) \\geq 0$\\\\ $16 \\geq 8(3-p)$\\\\ $2 \\geq 3-p$\\\\ $p \\geq 1$ \\item[(c)] $3x^2-2x+1-p=0$\\\\ $b^2-4ac &gt; 0$\\\\ $(-2)^2-4(3)(1-p)&gt;0$\\\\ $4 &gt; 12 (1-p)$\\\\ $\\frac{1}{3} &gt; 1-p$\\\\ $p&gt;\\frac{2}{3}$ \\item[(d)] $x^2-3px+p^2+1=0$\\\\ $(-3p)^2-4(1)(p^2+1)=0$\\\\ $9p^2-4p^2-4 =0$\\\\ $5p^2=4$\\\\ $p=\\pm \\frac{2 \\sqrt{5}}{5}$ \\item[(e)] $x^2-3x+2p=0$\\\\ $b^2-4ac &lt; 0$\\\\ $(-3)^2-4(1)(2p) &lt; 0$\\\\ $9 &lt; 8p$\\\\ $p &gt; \\frac{9}{8}$ \\item[(f)] $(x+1)(2x-1)=p-2$\\\\ $2x^2+x+1-p=$\\\\ $b^2-4ac &gt;0$\\\\ $(1)^2-4(2)(1-p)&gt;0$\\\\ $1-8+8p&gt;0$\\\\ $p&gt;\\frac{7}{8}$ \\item[(g)] $p(x+1)(x-3)=x-4p-2$\\\\ $px^2 -2px -3p = x-4p-2$\\\\ $px^2-(2p+1)x+p+2=0$\\\\ $b^2-4ac&lt;0$\\\\ $(2p+1)^2-4(p)(p+2)&lt;0$\\\\ $4p^2+4p+1-4p^2-8p&lt;0$\\\\ $1&lt;4p$\\\\ $p&gt;\\frac{1}{4}$ \\end{itemize}</p>\r\n',18,NULL,NULL,'Test'),(30,'PR','ON',0,'1','Text','What is the least value of $k$ if the roots of the equation $x^2-2kx+k^2=3+x$ are real?','From $x^2-2kx+k^2=3+x$\\\\\r\n$x^2-(2k+1)x+k^2-3=0$\\\\\r\n$b^2-4ac \\geq 0$\\\\\r\n$(2k+1)^2-4(1)(k^2-3) \\geq 0$\\\\\r\n$4k^2+4k+1-4k^2+12 \\geq 0$\\\\\r\n$4k \\geq -13$\\\\\r\n$ k \\geq -\\frac{13}{4}$\\\\\r\nTherefore, least value of $k$ is $-\\frac{13}{4}$.',18,NULL,NULL,'Test'),(31,'PR','ON',0,'1','Text','Show that the roots of the equation $2x^2+p=2(x-1)$ are not real if $p>-\\frac{3}{2}$.','From $2x^2+p=2(x-1)$\\\\\r\n$2x^2-2x+p+2=0$\\\\\r\n\\begin{align*}\r\n\\text{discriminant} &=b^2-4ac \\\\\r\n						     &=(-2)^2-4(2)(p+2) \\\\\r\n						     &=4-8p-16 \\\\\r\n						     &=12-8p \\\\\r\n						     &= 8\\left(\\frac{3}{2}-p\\right) \\\\					      \r\n\\text{if } p >- \\frac{3}{2}, \\text{discriminant}&< 0 	 \\> (\\text{shown})			     \r\n\\end{align*} ',18,NULL,NULL,'Test'),(32,'PR','NO',0,'1','Text','<p>Find the range of values of $k$ given that the line $y=2x+3$ intersects the curve $x^2+xy=k$ at two distinct points.</p>\r\n','<p>Given: line $y=2x+3$, curve $x^2+xy=k$\\\\ For the points of intersection, we solve the two equations simultaneously.\\\\ $x^2+x(2x+3)=k$\\\\ $3x^2+3x-k=0$\\\\ Since they intersect at 2 distinct points, $b^2-4ac&gt;0$.\\\\ $x^2-4(3)(-k)&gt;0$\\\\ $9+12k&gt;0$\\\\ $3+4k&gt;0$\\\\ $k&gt;-\\frac{3}{4}$</p>\r\n',18,22,NULL,'Test'),(33,'PR','NO',5,'1','Text','The curve $y=3x^2-2x+c-1$ cuts the $x$-axis at two points. Find the range of $c$.','For $3x^2-2x+c-1=0$, there are 2 distinct real solutions.</br>\r\nHence, $b^2-4ac >0$</br>\r\n$(-2)^2-4(3)(c-1)>0$</br>\r\n$4-12c+12>0$</br>\r\n$c < \\frac{4}{3}$',20,NULL,NULL,'Test'),(34,'PR','NO',0,'1','Text','Find the values of $p$ for which the $x$ -axis is a tangent to the curve $y=x^2+px-p+3$. For each of these values, find the coordinates of the point of tangency.','For $x$ -axis to be a tangent to the curve $y=x^2+px-p+3$\\\\\r\nHence, $b^2-4ac=0$ for $x^2+px-p+3=0$\\\\\r\n$(p)^2-4(1)(-p+3)=0$\\\\\r\n$p^2+4p-12=0$\\\\\r\n$(p+6)(p-2)=0$\\\\\r\n$p=-6$ or $p=2$',20,NULL,NULL,'Test'),(35,'PR','NO',0,'1','Text','<p>Find the range of values of $k$ for which</p>\r\n\r\n<p>(a) $2x^2+2x+k$ is always positive,</p>\r\n\r\n<p>(b) $-3x^2+6x+k-1$ is always negative,</p>\r\n\r\n<p>(c) $3x^2-3x&gt;x+k$ for all real values of $x$,</p>\r\n\r\n<p>(d) $kx^2+1&gt;2kx-k$ for all real values of $x$.</p>\r\n','<p>\\item[(a)] For $2x^2+2x+k&gt;0$\\\\ $b^2-4ac&lt;0$\\\\ $(2)^2-4(2)(k)&lt;0$\\\\ $4&lt;8k$\\\\ $k&gt;\\frac{1}{2}$ \\item[(b)] For $-3x^2+6x+k-1&lt;0$\\\\ $b^2-4ac&lt;0$\\\\ $(6)^2-4(-3)(k-1)&lt;0$\\\\ $36+12k-12&lt;0$\\\\ $k&lt;-2$ \\item[(c)] For $3x^2-3x&gt;x+k$\\\\ $3x^2-4x-k&gt;0$\\\\ $b^2-4ac&lt;0$\\\\ $(-4)^2-4(3)(-k)&lt;0$\\\\ $16+12k&lt;0$\\\\ $k&lt;-\\frac{4}{3}$ \\item[(d)] For $kx^2+1&gt;2kx-k$\\\\ $kx^2-2kx+1+k&gt;0$\\\\ $b^2-4ac&lt;0$\\\\ $(-2k)^2-4(k)(1+k)&lt;0$\\\\ $4k^2-4k-4k^2&lt;0$\\\\ $k&gt;0$</p>\r\n',20,NULL,NULL,'Test'),(36,'EX','NO',0,'1','Text','<p>a^2</p>\r\n','',17,NULL,NULL,'Test'),(37,'PR','ON',5,'2','Text','<p>The equation $2x^2=8x+3$ has roots $\\alpha$ and $\\beta$. Obtain an equation whose roots are</p>\r\n','',17,NULL,NULL,'Test'),(38,'PR','NO',6,'1','Text','Given that $\\alpha$ is the root of the equation $x^2=2x-1$, show that','',17,NULL,NULL,'Test'),(39,'PR','NO',6,'1','Text','Given that the equation $x^2+(1-k)x-k=0$ has negative roots which differ by 3, find','',17,NULL,NULL,'Test'),(40,'PR','NO',4,'5','Text','Given that the roots of $x^2+px+q=0$ are $\\alpha$ and $4\\alpha$, show that $4p^2=25q$.','From $x^2+px+q=0$,\r\nsum of roots, $\\alpha+4\\alpha=-\\frac{p}{1}$\\\\\r\n$5\\alpha=-p$\\\\\r\n$\\alpha=-\\frac{p}{5} \\quad (1)$\\\\\r\nproduct of roots, $(\\alpha)(4\\alpha) = \\frac{q}{1}$\\\\\r\n$4\\alpha^2=q \\quad (2)$ \\\\\r\nSubstituting (1) into (2)\\\\\r\n$4 (-\\frac{p}{5})^2=q$\\\\\r\n$4 (\\frac{p^2}{25})=q$\\\\\r\n$4p^2=25q$ (shown)',17,NULL,NULL,'Test'),(41,'PR','BO',9,'4','Text','<p>The equation $x^2-3x-2=0$ has roots $\\alpha$ and $\\beta$, and the equation $x^2-6x+p=0$ has roots $\\frac{k}{\\alpha}$ and $\\frac{k}{\\beta}$. Find the value of $k$ and of $p$.</p>\r\n','<p>From $x^2-3x-2=0$,\\\\ sum of roots = $ -\\frac{-3}{1}$\\\\ $\\alpha+\\beta =3 \\quad (1)$\\\\ product of roots = $ \\frac{-2}{1}$\\\\ $\\alpha\\beta = -2 \\quad (2)$\\\\ From $x^2-6x+p=0$,\\\\ sum of roots = $-\\frac{-6}{1}$\\\\ $\\frac{k}{\\alpha}+\\frac{k}{\\beta}=6$\\\\ $\\frac{k(\\alpha+\\beta)}{\\alpha\\beta}=6 \\quad (3)$\\\\ product of roots = $\\frac{p}{1}$\\\\ $(\\frac{k}{\\alpha})(\\frac{k}{\\beta})=p$\\\\ $p = \\frac{k^2}{\\alpha\\beta} \\quad (4)$\\\\ Substituting (1) and (2) into (3),\\\\ $\\frac{k(3)}{-2}=6$\\\\ $k=-4$\\\\ Substituting $k=-4$ and (2) into (4),\\\\ $p=\\frac{(-4)^2}{-2}$\\\\ $p=-8$</p>\r\n',17,NULL,NULL,'Test'),(42,'PR','NO',6,'3','Text','<p>Given that equation $kx^2+(k-1)x+2k+3=0$, where $k$ is a non-zero integer, find the value of $k$ for which</p>\r\n','',17,NULL,NULL,'Test'),(43,'PR','NO',0,'1','Text','','',17,NULL,NULL,'Test'),(44,'PR','NO',0,'1','Text','','',17,NULL,NULL,'Test'),(45,'PR','NO',4,'3','Text','The roots of the equation $3x^2-3kx+k-6=0$ are $\\alpha$ and $\\beta$. If $\\alpha^2+\\beta^2=\\frac{20}{3}\r\n$, find the possible values of $k$.','Given $\\alpha^2+\\beta^2=\\frac{20}{3} \\quad (1)$\\\\\r\nsum of roots = $-\\frac{-3k}{3}$\\\\\r\n$\\alpha+\\beta = k \\quad (2)$\\\\\r\nproduct of roots = $\\frac{k-6}{2}$\\\\\r\n$\\alpha\\beta = \\frac{k-6}{3} \\quad (3)$\\\\\r\nSince $(\\alpha+\\beta)^2=\\alpha^2+\\beta^2+2\\alpha\\beta \\quad (4)$\\\\\r\nSubstituting (1), (2), (3) into (4)\\\\\r\n$(k)^2=(\\frac{20}{3})+2(\\frac{k-6}{3})$\\\\\r\n$3k^2=20+2k-12$\\\\\r\n$3k^2-2k-8=0$\\\\\r\n$(3k+4)(k-2)=0$\\\\\r\n$k=-\\frac{4}{3}$ or $k=2$\\\\',17,NULL,NULL,'Test'),(46,'PR','NO',6,'1','Text','The roots of the equation $4x^2-x+36=0$ are $\\alpha^2$ and $\\beta^2$. Find','',17,NULL,NULL,'Test'),(47,'PR','PA',2,'3','Text','test','test',2,NULL,NULL,'Test'),(48,'PR','BO',5,'4','Text','The roots of the equation $2x^2+3x+4=0$ are $\\alpha$ and \\(\\beta\\), find </br>\r\n(a) $\\alpha^2+\\beta^2$ [2]</br>\r\n(b) $\\frac{1}{\\alpha}+\\frac{1}{\\beta} [3]$','test test',17,NULL,NULL,'Test'),(53,'PR','NO',0,'1','Text','Testing ENV - phucls','Testing ENV - phucls',2,2,NULL,'Testing ENV - phucls'),(55,'PR','BO',6,'3','Text','Express $3\\cos \\theta + 4\\sin \\theta$ as a single trigonometric term, where $\\theta$ is in degrees. [6] </br>\r\n\r\n','Comparing $3\\cos \\theta + 4\\sin \\theta$ with $a\\cos \\theta +b \\sin \\theta$,</br>\r\nwe have $a=3$ and $b=4$.</br>\r\n$R=\\sqrt{3^2+4^2}$</br>\r\n$R=5$</br>\r\n$\\tan \\alpha = \\frac{4}{3}$</br>\r\n$\\implies \\alpha \\approx 53.130^\\circ$</br>\r\n$3\\cos \\theta + 4\\sin \\theta=R\\cos (\\theta - \\alpha)$</br>',26,50,NULL,'$R\\cos (\\theta - \\alpha)$'),(56,'PR','BO',5,'2','Numberic','Find the maximum and minimum values of $2\\sin x+\\cos x$ and the corresponding values of $x$ where $0^\\circ \\leq x \\leq 360^\\circ$. [5]</br>\r\n\r\n\r\n\r\n','Here, $a=2$ and $b=1$.</br>\r\n$R=\\sqrt{2^2+1^2}$</br>\r\n$R=\\sqrt{5}$</br>\r\n$\\tan \\alpha = \\frac{1}{2}$</br>\r\n$\\implies \\alpha \\approx 26.565^\\circ$</br>\r\n$2\\sin x +\\cos x = R \\sin (x+\\alpha)$</br>\r\n$2\\sin x +\\cos x = \\sqrt{5} \\sin (x+26.565^\\circ)$</br>\r\n$-1 \\leq \\sin (x+\\alpha) \\leq 1$</br>\r\n$\\implies -\\sqrt{5} \\leq \\sqrt{5} \\sin (x+\\alpha) \\leq \\sqrt{5}$.</br>\r\nHence,</br>\r\n$2\\sin x +\\cos x$ has a maximum value of $\\sqrt{5}$ when $\\sin (x+\\alpha)=1$,</br>\r\nthat is, when $x+26.565^\\circ = 90^\\circ$</br>\r\n$x \\approx 63.4^\\circ$</br>\r\nIts minimum value is $-\\sqrt{5}$ when $\\sin (x+\\alpha)=-1$, that is, when</br>\r\n$x+26.565^\\circ=270^\\circ$</br>\r\n$x \\approx 243.4^\\circ$</br>',26,49,NULL,'max = $\\sqrt{5}$, x = $63.4^\\circ$ </br>\r\nmin = $-\\sqrt{5}$, x = $243.4^\\circ$'),(57,'PR','BO',5,'3','Text','Find all the angles between $0^\\circ$ and $360^\\circ$ which satisfy the equation </br>\r\n$$2 \\cos x - 5 \\sin x = 3.1.$$\r\n\r\n','Let $2\\cos x - 5\\sin x = R\\cos (x+\\alpha)$, where $R>0$ and $\\alpha$ acute.</br>\r\n$R=\\sqrt{2^2+5^2}$</br>\r\n$R=\\sqrt{29}$</br>\r\n$\\tan \\alpha = \\frac{5}{2}$</br>\r\n$\\implies \\alpha \\approx 68.199^\\circ$</br>\r\nSo,</br>\r\n\\begin{align*}\r\n2 \\cos x - 5 \\sin x &=3.1\\\\\r\n\\sqrt{29}\\cos (x+69.199^\\circ)	&=3.1\\\\\r\n\\cos (x+69.199^\\circ)	&=\\frac{3.1}{\\sqrt{29}}\\\\\r\n	x+69.199^\\circ			&\\approx 305.146^\\circ, 414.854^\\circ\\\\\r\n								x & \\approx 236.9^\\circ, 346.7^\\circ\\\\\r\n\\end{align*}',26,50,NULL,'$236.9^\\circ, 346.7^\\circ$'),(58,'PR','BO',5,'3','Text','Express the following as a single trigonometric function (in degrees).</br>\r\n $$\\cos \\theta +\\sin \\theta$$\r\n\r\n\r\n\r\n','\\begin{align*}\r\n\\text{Comparing } &\\cos \\theta +\\sin \\theta \\text{ with } a\\cos \\theta +b \\sin \\theta,\\\\\r\n\\text{we have } a&=1 \\text{ and } b=1.\\\\\r\nR&=\\sqrt{1^2+1^2}\\\\\r\nR&=\\sqrt{2}\\\\\r\n\\tan \\alpha& = \\frac{1}{1}\\\\\r\n\\implies \\alpha &= 45^\\circ\\\\\r\n\\sqrt{3}\\cos \\theta - \\sin \\theta	&=R\\cos (\\theta - \\alpha)\\\\\r\n\\sqrt{3}\\cos \\theta - \\sin \\theta	&=\\sqrt{2}\\cos (\\theta - 45^\\circ)\\\\\r\n\\end{align*}',26,NULL,NULL,'$\\sqrt{2}\\cos (\\theta - 45^\\circ)$'),(59,'PR','BO',4,'2','Text','Express the following as a single trigonometric function (in degrees) </br>\r\n\r\n$$\\sqrt{3}\\cos \\theta - \\sin \\theta$$\r\n\r\n','\\begin{align*}\r\n\\text{Comparing} &\\sqrt{3}\\cos \\theta - \\sin \\theta \\text{ with } a\\cos \\theta -b \\sin \\theta,\\\\\r\n\\text{we have } a&=\\sqrt{3} \\text{ and } b= 1.\\\\\r\nR&=\\sqrt{(\\sqrt{3})^2+1^2}\\\\\r\nR&=2\\\\\r\n\\tan \\alpha& = \\frac{1}{\\sqrt{3}}\\\\\r\n\\implies \\alpha &= 30^\\circ\\\\\r\n\\cos \\theta +\\sin \\theta&=R\\cos (\\theta + \\alpha)\\\\\r\n\\cos \\theta +\\sin \\theta&= 2\\cos (\\theta + 30^\\circ)\\\\\r\n\\end{align*}',26,NULL,NULL,'$2\\cos (\\theta + 30^\\circ)$'),(60,'PR','BO',3,'1','Text','Prove that $(\\cos x -\\sin x)^2 =1 -\\sin 2x$ [3] </br>\r\n\r\n','\\begin{align*}\r\n(\\cos x -\\sin x)^2 & = \\cos^2 x - 2\\cos x \\sin x + \\sin^2 x\\\\\r\n					&=  \\sin^2 x+ \\cos^2 x - 2\\cos x \\sin x \\\\\r\n					&=1 -\\sin 2x\\\\\r\n\\end{align*}',25,NULL,NULL,'$1 -\\sin 2x$'),(61,'PR','BO',3,'1','Text','Prove that $\\frac{sec^2 A}{\\tan A}=2 \\text{ cosec } 2A$ [3]\r\n\r\n','\\begin{align*}\r\n\\frac{\\sec^2 A}{\\tan A} & =\\frac{1}{\\cos^2 A \\tan A}\\\\\r\n					&= \\frac{1}{\\cos^2 A \\left(\\frac{\\sin A}{\\cos A}\\right)}\\\\\r\n					&= \\frac{1}{\\sin A \\cos A}\\\\\r\n					&= \\frac{1}{\\frac{1}{2}\\sin 2A}\\\\\r\n					&=2 \\text{ cosec } 2A\\\\\r\n\\end{align*}',25,NULL,NULL,'$2 \\text{ cosec } 2A$'),(62,'PR','BO',3,'2','Text','Prove that $\\sec^2 \\frac{\\theta}{2}=\\frac{2}{1+\\cos \\theta}$ [3]\r\n\r\n','\\begin{align*}\r\n\\sec^2 \\frac{\\theta}{2} & =\\frac{1}{\\cos^2 \\frac{\\theta}{2}}\\\\\r\n					&= \\frac{1}{\\frac{\\cos \\theta+1}{2}}\\\\\r\n					&=\\frac{2}{1+\\cos \\theta}\\\\\r\n\\end{align*}',25,NULL,NULL,'$\\frac{2}{1+\\cos \\theta}$'),(63,'PR','BO',3,'2','Text','Prove that $\\cos^4 A -\\sin^4 A = \\cos 2A$ [3]\r\n\r\n','\\begin{align*}\r\n\\cos^4 A -\\sin^4 A & =(\\cos^2 A - \\sin^2 A)(\\cos^2 A+\\sin^2 A)\\\\\r\n					&= (\\cos 2 A )(1)\\\\\r\n					&=\\cos 2A\\\\\r\n\\end{align*}',25,NULL,NULL,'$\\cos 2A$'),(64,'PR','BO',3,'2','Text','Prove that $\\frac{\\sin A}{1+\\cos A}=\\tan \\frac{1}{2}A$ [3]\r\n\r\n','\\begin{align*}\r\n\\frac{\\sin A}{1+\\cos A} & =\\frac{2\\sin \\frac{A}{2} \\cos \\frac{A}{2}}{2\\cos^2 \\frac{A}{2}}\\\\\r\n					&= \\frac{\\sin \\frac{A}{2}}{\\cos \\frac{A}{2}}\\\\\r\n					&=\\tan \\frac{1}{2}A\\\\\r\n\\end{align*}',25,NULL,NULL,'$\\tan \\frac{1}{2}A$'),(65,'PR','BO',4,'3','Text','Prove that $\\frac{1+\\tan^2 A}{1-\\tan^2 A}=\\sec 2A$ [4]\r\n\r\n','\\begin{align*}\r\n\\frac{1+\\tan^2 A}{1-\\tan^2 A} & = \\frac{1+\\frac{\\sin^2 A}{\\cos^2 A}}{1-\\frac{\\sin^2 A}{\\cos^2 A}}\\\\\r\n					&= \\frac{\\cos^2 A+\\sin^2 A}{\\cos^2 A- \\sin^2 A}\\\\\r\n					&= \\frac{1}{\\cos 2A}\\\\\r\n					&=\\sec 2A\\\\\r\n\\end{align*}',25,NULL,NULL,'$\\sec 2A$'),(70,'PR','BO',4,'2','Text','Given that $\\alpha$ and $\\beta$ are the roots of $x^2+4x+5=0$, find the value of $\\alpha^2 + \\beta^2$.','$\\alpha+\\beta = -4$ <\\br>\r\n$\\alpha \\beta = 5$ <\\br>\r\n$\\alpha^2+\\beta^2=(\\alpha+\\beta)^2-2\\alpha\\beta$ <\\br>\r\n$\\alpha^2+\\beta^2=(-4)^2-2(5)$ <\\br>\r\n$\\alpha^2+\\beta^2=6$ <\\br>',17,NULL,NULL,'6');
/*!40000 ALTER TABLE `meas_models_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meas_models_subject`
--

DROP TABLE IF EXISTS `meas_models_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meas_models_subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `education_level_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `mea_education_level_id_f2b87063_fk_meas_models_educationlevel_id` (`education_level_id`),
  CONSTRAINT `mea_education_level_id_f2b87063_fk_meas_models_educationlevel_id` FOREIGN KEY (`education_level_id`) REFERENCES `meas_models_educationlevel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meas_models_subject`
--

LOCK TABLES `meas_models_subject` WRITE;
/*!40000 ALTER TABLE `meas_models_subject` DISABLE KEYS */;
INSERT INTO `meas_models_subject` VALUES (1,'Additional Mathematics','O Level Advanced Math',2),(2,'Elementary Mathematics','O Level Advanced Math',2),(3,'H2 Mathematics','High School Math',1);
/*!40000 ALTER TABLE `meas_models_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meas_models_test`
--

DROP TABLE IF EXISTS `meas_models_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meas_models_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `test_type` varchar(200) NOT NULL,
  `questions_list` longtext NOT NULL,
  `number_of_questions` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meas_models_test`
--

LOCK TABLES `meas_models_test` WRITE;
/*!40000 ALTER TABLE `meas_models_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `meas_models_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meas_models_topic`
--

DROP TABLE IF EXISTS `meas_models_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meas_models_topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `order` int(10) unsigned DEFAULT NULL,
  `subject_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `meas_models_topic_subject_id_584b18ec_fk_meas_models_subject_id` (`subject_id`),
  CONSTRAINT `meas_models_topic_subject_id_584b18ec_fk_meas_models_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `meas_models_subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meas_models_topic`
--

LOCK TABLES `meas_models_topic` WRITE;
/*!40000 ALTER TABLE `meas_models_topic` DISABLE KEYS */;
INSERT INTO `meas_models_topic` VALUES (1,'Quadratic Equations & inequalities','$ax^2+bx+c=0 \\> \\text{where} \\> a \\neq 0$',0,1),(2,'Indices, Surds, Exponential, Logarithms','$a^n$',1,1),(3,'Polynomials and Partial Fractions','Test',2,1),(4,'Simultaneous Equations','Test',3,1),(5,'Binomial Function','Test',4,1),(6,'Modulus Function','Test',5,1),(7,'Coordinate Geometry','Test',7,1),(8,'Plane Geometry','Test',6,1),(9,'Trigonometry','Test',8,1),(10,'Differentiation','Test',9,1),(11,'Integration & Definite Integrals','Test',11,3),(12,'Kinematics','Test',10,2);
/*!40000 ALTER TABLE `meas_models_topic` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-23 18:18:05
