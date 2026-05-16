-- MySQL dump 10.13  Distrib 8.4.9, for Linux (x86_64)
--
-- Host: localhost    Database: product_db
-- ------------------------------------------------------
-- Server version	8.4.9

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `description` text,
  `image_url` varchar(500) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Luxury Red Rose Bouquet','Premium fresh red roses wrapped in elegant paper for romantic occasions.','https://images.unsplash.com/photo-1519378058457-4c29a0a2efac',4000,20,'2026-05-15 21:59:50'),(2,'Elegant White Lily Bouquet','Fresh white lilies arranged beautifully for weddings and special occasions.','https://images.unsplash.com/photo-1563241527-3004b7be0ffd',4600,15,'2026-05-15 22:01:02'),(3,'Sunflower Happiness Bundle','Bright and cheerful sunflowers to instantly uplift mood and energy.','https://images.unsplash.com/photo-1470509037663-253afd7f0f51',2500,30,'2026-05-15 22:01:02'),(4,'Pink Tulip Romance Bouquet','Soft pink tulips arranged for romantic and elegant gifting.','https://images.unsplash.com/photo-1520763185298-1b434c919102',3200,25,'2026-05-15 22:01:02'),(5,'Mixed Spring Flower Basket','A colorful mix of seasonal flowers in a decorative basket.','https://images.unsplash.com/photo-1468327768560-75b778cbb551',3800,18,'2026-05-15 22:01:02'),(6,'Lavender Dream Bouquet','Calming lavender bouquet with soothing fragrance and aesthetic charm.','https://images.unsplash.com/photo-1501004318641-b39e6451bec6',2800,18,'2026-05-15 22:21:34'),(7,'Golden Chrysanthemum Basket','Luxurious golden chrysanthemums for festive celebrations.','https://images.unsplash.com/photo-1501004318641-b39e6451bec6',3500,22,'2026-05-15 22:21:34'),(8,'Mixed Spring Flower Box','A premium mix of seasonal flowers in a gift box.','https://images.unsplash.com/photo-1468327768560-75b778cbb551',4200,12,'2026-05-15 22:21:34'),(9,'Orchid Elegance Bouquet','Exotic orchids for premium gifting and corporate events.','https://images.unsplash.com/photo-1470509037663-253afd7f0f51',5500,10,'2026-05-15 22:21:34'),(10,'Pastel Garden Bouquet','Soft pastel flowers perfect for birthdays and celebrations.','https://images.unsplash.com/photo-1504198453319-5ce911bafcde',3000,28,'2026-05-15 22:21:34'),(11,'Romantic Valentine Special Bouquet','Premium red-pink floral mix designed for Valentine gifting.','https://images.unsplash.com/photo-1518895949257-7621c3c786d7',6000,8,'2026-05-15 22:21:34');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-15 22:22:02
