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
-- Table structure for table `dbmanagement_topic`
--

DROP TABLE IF EXISTS `dbmanagement_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbmanagement_topic` (
  `id` int(11) NOT NULL,
  `block_id` int(11) DEFAULT NULL,
  `title` longtext,
  PRIMARY KEY (`id`),
  KEY `DBManagement_topic_45897ef2` (`block_id`),
  CONSTRAINT `block_id_refs_id_58f256b3` FOREIGN KEY (`block_id`) REFERENCES `dbmanagement_block` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbmanagement_topic`
--

LOCK TABLES `dbmanagement_topic` WRITE;
/*!40000 ALTER TABLE `dbmanagement_topic` DISABLE KEYS */;
INSERT INTO `dbmanagement_topic` VALUES (1,1,'Standard Graphs'),(2,1,'Graphical Transformations'),(3,1,'Graphing with Rational Functions and Parametric Equations'),(4,1,'Special Graphs'),(5,1,'Functions'),(6,1,'Inequalities'),(7,1,'Systems of Linear Equations'),(8,2,'Binomial Series'),(9,2,'Arithmetic and Geometric Series'),(10,2,'Summation of Series'),(11,2,'Mathematical Induction'),(12,3,'Vectors in Two and Three Dimensions'),(13,3,'Scalar and Vector Products'),(14,3,'Equations of Lines'),(15,3,'Equations of Planes'),(16,3,'Three Dimensional Vector Geometry'),(17,4,'Complex Numbers in Cartesian Form'),(18,4,'Complex Numbers in Trigonometric Form'),(19,4,'Complex Numbers in Exponential Form'),(20,4,'Locus of a Complex Number'),(21,5,'Differentiation'),(22,5,'Applications of Differentiation'),(23,5,'Maclaurin\'s Series'),(24,5,'Indefinite Integration'),(25,5,'Definite Integration'),(26,5,'Applications of Definite Integration'),(27,5,'Differential Equations'),(28,6,'Permutations and Combinations'),(29,6,'Probability'),(30,6,'Binomial Distributions'),(31,6,'Poisson Distributions'),(32,6,'Normal Distributions'),(33,6,'Sampling and Estimation'),(34,6,'Hypothesis Testing'),(35,6,'Correlation and Linear Regression'),(36,7,'Others'),(37,11,'Quadratic Equations'),(38,11,'Indices and Surds'),(39,11,'Polynomials'),(40,11,'Partial Fractions'),(41,11,'Simultaneous Equations'),(42,11,'Binomial Expansions'),(43,11,'Exponential and Logarithmic Functions'),(44,11,'Modulus Functions'),(45,12,'Trigonometry'),(46,12,'Coordinate Geometry'),(47,12,'Plane Geometry'),(48,13,'Differentiation'),(49,13,'Integration'),(50,14,'Kinematics'),(51,14,'Set Language '),(52,14,'Functions'),(53,11,'Matrices'),(54,12,'Vectors'),(55,16,'Permutations and Combinations'),(56,12,'Arithmetic Progression and Geometric Progression'),(57,12,'Circular Measure'),(58,17,'Others'),(59,59,'Arithmetic'),(60,60,'Mensuration'),(61,61,'Algebra'),(62,62,'Number Sequence and Problem Solving'),(63,63,'Coordinate Geometry'),(64,64,'Graphs, Kinematics and Variations'),(65,65,'Geometry '),(66,66,'Transformations'),(67,67,'Trigonometry'),(68,68,'Set Language and Notation'),(69,69,'Matrices'),(70,70,'Vectors in Two Dimensions'),(71,71,'Probability'),(72,72,'Statistics'),(73,73,'Others'),(114,114,'Whole Numbers and decimals'),(115,115,'Measurement'),(116,116,'Geometry'),(117,117,'Data Analysis'),(118,118,'Fractions'),(119,119,'Percentage and ratio'),(120,120,'Heuristic-Based'),(121,121,'Algebra');
/*!40000 ALTER TABLE `dbmanagement_topic` ENABLE KEYS */;
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
