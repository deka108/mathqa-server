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
-- Table structure for table `dbmanagement_block`
--

DROP TABLE IF EXISTS `dbmanagement_block`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbmanagement_block` (
  `id` int(11) NOT NULL,
  `title` longtext,
  `subject_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `DBManagement_block_638462f1` (`subject_id`),
  CONSTRAINT `subject_id_refs_id_2f714822` FOREIGN KEY (`subject_id`) REFERENCES `dbmanagement_subject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbmanagement_block`
--

LOCK TABLES `dbmanagement_block` WRITE;
/*!40000 ALTER TABLE `dbmanagement_block` DISABLE KEYS */;
INSERT INTO `dbmanagement_block` VALUES (1,'Function and Graph',3),(2,'Sequences and Series',3),(3,'Vectors',3),(4,'Complex Numbers',3),(5,'Calculus',3),(6,'Statistics',3),(7,'Others',3),(11,'Algebra',1),(12,'Geometry and Measurement',1),(13,'Calculus',1),(14,'Numbers and Algebra',1),(16,'Statistics',1),(17,'Others',1),(59,'Arithmetic',2),(60,'Mensuration',2),(61,'Algebra',2),(62,'Number Sequence and Problem Solving',2),(63,'Coordinate Geometry',2),(64,'Graphs, Kinematics and Variations',2),(65,'Geometry ',2),(66,'Transformations',2),(67,'Trigonometry',2),(68,'Set Language and Notation',2),(69,'Matrices',2),(70,'Vectors in Two Dimensions',2),(71,'Probability',2),(72,'Statistics',2),(73,'Others',2),(114,'Whole Numbers and decimals',4),(115,'Measurement',4),(116,'Geometry',4),(117,'Data Analysis',4),(118,'Fractions',4),(119,'Percentage and ratio',4),(120,'Heuristic-Based',4),(121,'Algebra',4);
/*!40000 ALTER TABLE `dbmanagement_block` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-23 23:05:24
