CREATE DATABASE  IF NOT EXISTS `mathdb` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `mathdb`;
-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: localhost    Database: mathdb
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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=122 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add education_ level',8,'add_education_level'),(23,'Can change education_ level',8,'change_education_level'),(24,'Can delete education_ level',8,'delete_education_level'),(25,'Can add subject',9,'add_subject'),(26,'Can change subject',9,'change_subject'),(27,'Can delete subject',9,'delete_subject'),(28,'Can add block',10,'add_block'),(29,'Can change block',10,'change_block'),(30,'Can delete block',10,'delete_block'),(31,'Can add topic',11,'add_topic'),(32,'Can change topic',11,'change_topic'),(33,'Can delete topic',11,'delete_topic'),(34,'Can add subtopic',12,'add_subtopic'),(35,'Can change subtopic',12,'change_subtopic'),(36,'Can delete subtopic',12,'delete_subtopic'),(37,'Can add paperset',13,'add_paperset'),(38,'Can change paperset',13,'change_paperset'),(39,'Can delete paperset',13,'delete_paperset'),(40,'Can add paper',14,'add_paper'),(41,'Can change paper',14,'change_paper'),(42,'Can delete paper',14,'delete_paper'),(43,'Can add question',15,'add_question'),(44,'Can change question',15,'change_question'),(45,'Can delete question',15,'delete_question'),(46,'Can add solution',16,'add_solution'),(47,'Can change solution',16,'change_solution'),(48,'Can delete solution',16,'delete_solution'),(49,'Can add image',17,'add_image'),(50,'Can change image',17,'change_image'),(51,'Can delete image',17,'delete_image'),(52,'Can add answer type',18,'add_answertype'),(53,'Can change answer type',18,'change_answertype'),(54,'Can delete answer type',18,'delete_answertype'),(55,'Can add answer',19,'add_answer'),(56,'Can change answer',19,'change_answer'),(57,'Can delete answer',19,'delete_answer'),(58,'Can add progress',20,'add_progress'),(59,'Can change progress',20,'change_progress'),(60,'Can delete progress',20,'delete_progress'),(61,'Can add tag definition',21,'add_tagdefinition'),(62,'Can change tag definition',21,'change_tagdefinition'),(63,'Can delete tag definition',21,'delete_tagdefinition'),(64,'Can add tag',22,'add_tag'),(65,'Can change tag',22,'change_tag'),(66,'Can delete tag',22,'delete_tag'),(67,'Can add formula',23,'add_formula'),(68,'Can change formula',23,'change_formula'),(69,'Can delete formula',23,'delete_formula'),(70,'Can add formula_index',24,'add_formula_index'),(71,'Can change formula_index',24,'change_formula_index'),(72,'Can delete formula_index',24,'delete_formula_index'),(73,'Can add assessment',25,'add_assessment'),(74,'Can change assessment',25,'change_assessment'),(75,'Can delete assessment',25,'delete_assessment'),(76,'Can add response',26,'add_response'),(77,'Can change response',26,'change_response'),(78,'Can delete response',26,'delete_response'),(79,'Can add test',27,'add_test'),(80,'Can change test',27,'change_test'),(81,'Can delete test',27,'delete_test'),(82,'Can add test response',28,'add_testresponse'),(83,'Can change test response',28,'change_testresponse'),(84,'Can delete test response',28,'delete_testresponse'),(85,'Can add meta',29,'add_meta'),(86,'Can change meta',29,'change_meta'),(87,'Can delete meta',29,'delete_meta'),(88,'Can add question meta',30,'add_questionmeta'),(89,'Can change question meta',30,'change_questionmeta'),(90,'Can delete question meta',30,'delete_questionmeta'),(91,'Can add test question',31,'add_testquestion'),(92,'Can change test question',31,'change_testquestion'),(93,'Can delete test question',31,'delete_testquestion'),(94,'Can add user profile',32,'add_userprofile'),(95,'Can change user profile',32,'change_userprofile'),(96,'Can delete user profile',32,'delete_userprofile'),(97,'Can add user usage',33,'add_userusage'),(98,'Can change user usage',33,'change_userusage'),(99,'Can delete user usage',33,'delete_userusage'),(100,'Can add comment',34,'add_comment'),(101,'Can change comment',34,'change_comment'),(102,'Can delete comment',34,'delete_comment'),(103,'Can moderate comments',34,'can_moderate'),(104,'Can add comment flag',35,'add_commentflag'),(105,'Can change comment flag',35,'change_commentflag'),(106,'Can delete comment flag',35,'delete_commentflag'),(107,'Can add mptt comment',36,'add_mpttcomment'),(108,'Can change mptt comment',36,'change_mpttcomment'),(109,'Can delete mptt comment',36,'delete_mpttcomment'),(110,'Can add ask',37,'add_ask'),(111,'Can change ask',37,'change_ask'),(112,'Can delete ask',37,'delete_ask'),(113,'Can add askfile',38,'add_askfile'),(114,'Can change askfile',38,'change_askfile'),(115,'Can delete askfile',38,'delete_askfile'),(116,'Can add question c',39,'add_questionc'),(117,'Can change question c',39,'change_questionc'),(118,'Can delete question c',39,'delete_questionc'),(119,'Can add file c',40,'add_filec'),(120,'Can change file c',40,'change_filec'),(121,'Can delete file c',40,'delete_filec');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-15 19:53:50
