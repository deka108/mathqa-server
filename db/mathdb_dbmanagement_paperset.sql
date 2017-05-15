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
-- Table structure for table `dbmanagement_paperset`
--

DROP TABLE IF EXISTS `dbmanagement_paperset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbmanagement_paperset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` longtext,
  `subject_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `DBManagement_paperset_638462f1` (`subject_id`),
  CONSTRAINT `subject_id_refs_id_51255274` FOREIGN KEY (`subject_id`) REFERENCES `dbmanagement_subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1024 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbmanagement_paperset`
--

LOCK TABLES `dbmanagement_paperset` WRITE;
/*!40000 ALTER TABLE `dbmanagement_paperset` DISABLE KEYS */;
INSERT INTO `dbmanagement_paperset` VALUES (1,'1997 November',3),(2,'1998 November',3),(3,'1999 November',3),(4,'2000 November',3),(5,'2001 November',3),(6,'2002 November',3),(7,'2003 November',3),(8,'2004 November',3),(9,'2005 November',3),(10,'2006 November',3),(11,'2007 November',3),(12,'1995 June',1),(13,'1995 November',1),(14,'1996 June',1),(15,'1996 November',1),(16,'1997 June',1),(17,'1997 November',1),(18,'1998 June',1),(19,'1998 November',1),(20,'1999 June',1),(21,'1999 November',1),(22,'2000 June',1),(23,'2000 November',1),(24,'2001 June',1),(25,'2001 November',1),(26,'2002 June',1),(27,'2002 November',1),(28,'2003 June',1),(29,'2003 November',1),(30,'2004 November',1),(31,'2005 November',1),(32,'2006 November',1),(33,'2007 November',1),(34,'2008 November',1),(35,'2009 November',1),(36,'2010 November',1),(37,'1995 June',2),(38,'1996 June',2),(39,'1997 June',2),(40,'1997 November',2),(41,'1998 June',2),(42,'1998 November',2),(43,'1999 June',2),(44,'1999 November',2),(45,'2000 June',2),(46,'2000 November',2),(47,'2001 June',2),(48,'2001 November',2),(49,'2002 June',2),(50,'2002 November',2),(51,'2003 June',2),(52,'2003 November',2),(53,'2004 November',2),(54,'2005 November',2),(55,'2006 November',2),(56,'2007 November',2),(57,'2008 November',2),(58,'2009 November',2),(59,'2010 November',2),(1001,'St Hilda Primary School SA2',4),(1002,'Nan Hua Primary School SA2',4),(1003,'Nanyang Primary School SA2',4),(1004,'Tao Nan Primary School SA2',4),(1005,'Anglo Chinese School SA2',4),(1006,'Raffles Girls Primary School SA2',4),(1007,'Christian Brothers School SA2',4),(1008,'Singapore Hokkien Huay Kwan SA2',4),(1009,'2008 PSLE Mathematics',4),(1010,'2013 Singapore Chinese Girls School SA2',4),(1011,'2013 Tao Nan Primary School SA2',4),(1012,'2013 Rosyth School SA2',4),(1013,'2013 Raffles Girls School SA2',4),(1014,'2013 Nanyang Primary School SA2',4),(1015,'2013 Nan Hua Primary School SA2',4),(1016,'2013 Singapore Hokkien Huay Kwan SA2',4),(1017,'2013 Methodist Girls Primary School SA2',4),(1018,'2013 CHIJ St Nicholas Primary School SA2',4),(1019,' ',3),(1020,' ',3),(1021,' ',3),(1022,' ',3),(1023,' ',3);
/*!40000 ALTER TABLE `dbmanagement_paperset` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-15 19:53:51
