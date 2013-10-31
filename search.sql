-- phpMyAdmin SQL Dump
-- version 4.0.8
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 28, 2013 at 07:12 PM
-- Server version: 5.5.33a-MariaDB-log
-- PHP Version: 5.5.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `searchengine`
--

-- --------------------------------------------------------

--
-- Table structure for table `search`
--

CREATE TABLE IF NOT EXISTS `search` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Rank` tinyint(3) unsigned NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `url` text NOT NULL,
  `keywords` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `search`
--

INSERT INTO `search` (`id`, `Rank`, `title`, `description`, `url`, `keywords`) VALUES
(2, 0, 'Socialnode', 'A microblogging social network ', 'http://socialno.de', 'derp social node socialnode irc twitter facebook blogging url appnode'),
(3, 0, 'Uppit', 'The front page of hyperboria (a Reddit clone)', 'http://[fc3a:956e:4b69:1c1e:5ebc:11a5:3e71:3e7e]', 'Uppit social face of hyperboria reddit Reddit vote content thefinn93 Dan'),
(4, 0, 'Anarchive', 'a distributed library of digital content', 'http://[fcb4:bcb2:1630:bfe3:b4c4:f99b:98b:eca4]/cgi/ansearch.py ', 'files Content library ansuz P2P Anarchive'),
(5, 0, 'Urlcloud', 'A simple file sharing site for hyperboria', 'http://urlcloud.net', 'url cloud file storage hyperboria simple imgur clone new content sharing lib derp urlcloud');
