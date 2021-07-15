-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: mydata
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `uid` varchar(45) NOT NULL,
  `pass` varchar(45) NOT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `uid_UNIQUE` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('admin','admin'),('harry','Harry1999');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pharma`
--

DROP TABLE IF EXISTS `pharma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pharma` (
  `Refid` int NOT NULL,
  `MedName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Refid`),
  UNIQUE KEY `Refid_UNIQUE` (`Refid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pharma`
--

LOCK TABLES `pharma` WRITE;
/*!40000 ALTER TABLE `pharma` DISABLE KEYS */;
INSERT INTO `pharma` VALUES (123,'Narco'),(126,'small'),(160,'Excali'),(190,'WyZo0'),(589,'Crocin'),(659,'avv');
/*!40000 ALTER TABLE `pharma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pharmacy`
--

DROP TABLE IF EXISTS `pharmacy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pharmacy` (
  `ref_no` int NOT NULL,
  `CmpName` varchar(45) DEFAULT NULL,
  `TypeMed` varchar(45) DEFAULT NULL,
  `Medname` varchar(45) DEFAULT NULL,
  `Lotno` varchar(45) NOT NULL,
  `Issue_Date` date NOT NULL,
  `ExpDate` date NOT NULL,
  `uses` varchar(45) DEFAULT NULL,
  `sideeffect` varchar(45) DEFAULT NULL,
  `warning` varchar(45) DEFAULT NULL,
  `dosage` varchar(45) DEFAULT NULL,
  `price` float NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`ref_no`),
  UNIQUE KEY `ref_no_UNIQUE` (`ref_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pharmacy`
--

LOCK TABLES `pharmacy` WRITE;
/*!40000 ALTER TABLE `pharmacy` DISABLE KEYS */;
INSERT INTO `pharmacy` VALUES (121,'WyZo0','Pills','Cronic','8','2021-07-06','2022-07-20','Fever','','','',25.64,10),(123,'Marley','Drugs','Narco','5','2021-06-24','2022-07-22','Sleep','None','None','2',52,12),(145,'Cipla','Tablet','Harry','12','2021-06-26','2021-06-30','Covid','Increase in sugar level','None','3',25.64,6);
/*!40000 ALTER TABLE `pharmacy` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-12 13:13:19
