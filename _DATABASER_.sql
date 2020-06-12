-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 12, 2020 at 03:24 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `emenu`
--

-- --------------------------------------------------------

--
-- Table structure for table `clientorders`
--

CREATE TABLE `clientorders` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `phone_number` int(11) NOT NULL,
  `payment_done` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `type` varchar(20) NOT NULL,
  `price` int(11) NOT NULL,
  `description` varchar(80) NOT NULL,
  `phone_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`id`, `order_id`, `name`, `type`, `price`, `description`, `phone_number`) VALUES
(1, 1, 'Pizza Fungi', 'Pizza', 180, 'with tomate sauce, cheese, fungi', 71390666),
(2, 1, 'Pizza Fungi', 'Pizza', 180, 'with tomate sauce, cheese, fungi', 71390666),
(3, 1, 'Pizza Fungi', 'Pizza', 180, 'with tomate sauce, cheese, fungi', 71390666),
(4, 2, 'Pizza Vegetarian', 'Pizza', 120, 'with tomate sauce, cheese, fungi, olives, pepper, cherry tomatoes', 71390666),
(5, 3, 'Pizza Vegetarian', 'Pizza', 120, 'with tomate sauce, cheese, fungi, olives, pepper, cherry tomatoes', 71390666),
(6, 4, 'Chicago burger', 'Burger', 180, 'with beef, cheese, onions, lettuce, ketchup, mayo', 71390666),
(7, 5, 'Chicago burger', 'Burger', 180, 'with beef, cheese, onions, lettuce, ketchup, mayo', 71390666),
(8, 6, 'Chicago burger', 'Burger', 180, 'with beef, cheese, onions, lettuce, ketchup, mayo', 71390666),
(9, 7, 'Chicago burger', 'Burger', 180, 'with beef, cheese, onions, lettuce, ketchup, mayo', 71390666),
(10, 8, 'Chicago burger', 'Burger', 180, 'with beef, cheese, onions, lettuce, ketchup, mayo', 71390666),
(11, 251, 'Pizza Vegetarian', 'Pizza', 180, 'With: tomatoe sauce, cheese, onions, broccoli, olives, cherry tomatoes', 75269700),
(12, 252, 'Pizza Fungi', 'Pizza', 200, 'With: tomatoe sauce, cheese, mushrooms', 75269700),
(13, 254, 'Pizza Fungi', 'Pizza', 200, 'With: tomatoe sauce, cheese, mushrooms', 75269700),
(14, 255, 'Big Mac', 'Burger', 180, 'with beef, lettuce, cheese, onions, ketchup and mayo', 75269700),
(15, 256, 'Burger test', 'Burger', 150, 'With: tomatoe sauce, cheese, onions, broccoli, olives, cherry tomatoes', 75269700),
(16, 261, 'Pizza Mix', 'Pizza', 200, 'with tomato sauce, cheese, mushroom, pepperoni, prosciutto', 75269700),
(17, 262, 'Big Mac', 'Burger', 180, 'with beef, lettuce, cheese, onions, ketchup and mayo', 75269700),
(18, 263, 'Burger test', 'Burger', 150, 'With: tomatoe sauce, cheese, onions, broccoli, olives, cherry tomatoes', 75269700),
(19, 266, 'Pizza Vegetarian', 'Pizza', 180, 'With: tomatoe sauce, cheese, onions, broccoli, olives, cherry tomatoes', 75269700),
(20, 267, 'Pizza Fungi', 'Pizza', 200, 'With: tomatoe sauce, cheese, mushrooms', 75269700),
(21, 268, 'Pizza Vegetarian', 'Pizza', 180, 'With: tomatoe sauce, cheese, onions, broccoli, olives, cherry tomatoes', 75269700),
(22, 269, 'Pizza Mix', 'Pizza', 200, 'with tomato sauce, cheese, mushroom, pepperoni, prosciutto', 75269700),
(23, 270, 'Pizza Vegetarian', 'Pizza', 180, 'With: tomatoe sauce, cheese, onions, broccoli, olives, cherry tomatoes', 75269700),
(24, 271, 'Pizza Fungi', 'Pizza', 200, 'With: tomatoe sauce, cheese, mushrooms', 75269700),
(25, 272, 'Pizza Vegetarian', 'Pizza', 180, 'With: tomatoe sauce, cheese, onions, broccoli, olives, cherry tomatoes', 75269700),
(26, 273, 'Pizza Fungi', 'Pizza', 200, 'With: tomatoe sauce, cheese, mushrooms', 75269700),
(27, 274, 'Pizza Fungi', 'Pizza', 200, 'With: tomatoe sauce, cheese, mushrooms', 71390666),
(28, 279, 'Big Mac', 'Burger', 180, 'with beef, lettuce, cheese, onions, ketchup and mayo', 71390666),
(29, 278, 'Pizza Mix', 'Pizza', 200, 'with tomato sauce, cheese, mushroom, pepperoni, prosciutto', 71390666),
(30, 276, 'Pizza Fungi', 'Pizza', 200, 'With: tomatoe sauce, cheese, mushrooms', 75269700),
(31, 275, 'Pizza Vegetarian', 'Pizza', 180, 'With: tomatoe sauce, cheese, onions, broccoli, olives, cherry tomatoes', 75269700),
(32, 280, 'Pizza Mix', 'Pizza', 200, 'with tomato sauce, cheese, mushroom, pepperoni, prosciutto', 71390666),
(33, 281, 'Big Mac', 'Burger', 180, 'with beef, lettuce, cheese, onions, ketchup and mayo', 71390666),
(34, 284, 'Pizza Vegetarian', 'Pizza', 180, 'With: tomatoe sauce, cheese, onions, broccoli, olives, cherry tomatoes', 75269700),
(35, 285, 'Big Mac', 'Burger', 180, 'with beef, lettuce, cheese, onions, ketchup and mayo', 75269700);

-- --------------------------------------------------------

--
-- Table structure for table `kitchenorders`
--

CREATE TABLE `kitchenorders` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `order_started` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `meal`
--

CREATE TABLE `meal` (
  `id` int(11) NOT NULL,
  `restaurant_id` int(11) NOT NULL,
  `name` char(50) NOT NULL,
  `type` char(50) NOT NULL,
  `description` char(100) NOT NULL,
  `price` int(11) NOT NULL,
  `prep_time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `meal`
--

INSERT INTO `meal` (`id`, `restaurant_id`, `name`, `type`, `description`, `price`, `prep_time`) VALUES
(7, 4, 'Pizza Vegetarian', 'Pizza', 'With: tomatoe sauce, cheese, onions, broccoli, olives, cherry tomatoes', 180, 7),
(8, 4, 'Burger test', 'Burger', 'With: tomatoe sauce, cheese, onions, broccoli, olives, cherry tomatoes', 150, 10),
(10, 4, 'Pizza Fungi', 'Pizza', 'With: tomatoe sauce, cheese, mushrooms', 200, 7),
(38, 4, 'Big Mac', 'Burger', 'with beef, lettuce, cheese, onions, ketchup and mayo', 180, 8),
(39, 4, 'Pizza Mix', 'Pizza', 'with tomato sauce, cheese, mushroom, pepperoni, prosciutto', 200, 7),
(40, 6, 'Pizza Mix', 'Pizza', 'with tomatoe sauce, cheese , bla bla', 180, 7);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `meal_id` int(11) NOT NULL,
  `active_order` tinyint(1) DEFAULT 1,
  `phone_number` int(11) NOT NULL,
  `quantity` int(11) NOT NULL DEFAULT 1,
  `payment_done` tinyint(1) NOT NULL DEFAULT 0,
  `table_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `request`
--

CREATE TABLE `request` (
  `id` int(11) NOT NULL,
  `description` varchar(100) NOT NULL,
  `time` varchar(32) NOT NULL,
  `restaurant` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `restaurant`
--

CREATE TABLE `restaurant` (
  `id` int(11) NOT NULL,
  `name` char(50) NOT NULL,
  `location` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `restaurant`
--

INSERT INTO `restaurant` (`id`, `name`, `location`) VALUES
(4, 'Pizza Garden', 'Dervish Cara 35'),
(6, 'Mhouse 2', 'Ilindenska 700');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `phone_number` int(11) NOT NULL,
  `name` char(50) NOT NULL,
  `lastname` char(50) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` char(50) NOT NULL,
  `user_type` char(20) NOT NULL,
  `restaurant_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`phone_number`, `name`, `lastname`, `email`, `password`, `user_type`, `restaurant_name`) VALUES
(70123456, 'John', 'Doe', '', '527bd5b5d689e2c32ae974c6229ff785', 'Kitchen', 'PizzaGarden'),
(70390666, 'Lenart', 'Shtul', 'li26983@seeu.edu.mk', '9101ccb30d06f15ee61aae74b5ff912e', 'Client', NULL),
(71123456, 'Manager', 'Manager', '', '1d0258c2440a8d19e716292b231e3190', 'Manager', 'PizzaGarden'),
(71390666, 'Lenart', 'Ibraimi', '', '9101ccb30d06f15ee61aae74b5ff912e', 'Admin', ''),
(75269700, 'Genita', 'Sadiku', '', '666ea1a867a93c82c16785b921746a59', 'Client', ''),
(77390666, 'Leni', 'Hotmail', 'leni_carbon9@hotmail.com', '9101ccb30d06f15ee61aae74b5ff912e', 'Client', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clientorders`
--
ALTER TABLE `clientorders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_order_id` (`order_id`);

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kitchenorders`
--
ALTER TABLE `kitchenorders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_orders_id` (`order_id`);

--
-- Indexes for table `meal`
--
ALTER TABLE `meal`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_restaurant_id` (`restaurant_id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_meal_id` (`meal_id`);

--
-- Indexes for table `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `restaurant`
--
ALTER TABLE `restaurant`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`phone_number`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `clientorders`
--
ALTER TABLE `clientorders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=197;

--
-- AUTO_INCREMENT for table `data`
--
ALTER TABLE `data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `kitchenorders`
--
ALTER TABLE `kitchenorders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT for table `meal`
--
ALTER TABLE `meal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=286;

--
-- AUTO_INCREMENT for table `request`
--
ALTER TABLE `request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `restaurant`
--
ALTER TABLE `restaurant`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `clientorders`
--
ALTER TABLE `clientorders`
  ADD CONSTRAINT `fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `kitchenorders`
--
ALTER TABLE `kitchenorders`
  ADD CONSTRAINT `fk_orders_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`);

--
-- Constraints for table `meal`
--
ALTER TABLE `meal`
  ADD CONSTRAINT `fk_restaurant_id` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `fk_meal_id` FOREIGN KEY (`meal_id`) REFERENCES `meal` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
