-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 02-Ago-2019 às 02:55
-- Versão do servidor: 10.1.37-MariaDB
-- versão do PHP: 7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `salas`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `capela 1 avelar`
--

CREATE TABLE `capela 1 avelar` (
  `Pessoa` text NOT NULL,
  `Horario` text NOT NULL,
  `Sepultamento` text NOT NULL,
  `Cemiterio` text NOT NULL,
  `Status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `capela 1 avelar`
--

INSERT INTO `capela 1 avelar` (`Pessoa`, `Horario`, `Sepultamento`, `Cemiterio`, `Status`) VALUES
('Fulaninho de Tal', '12:31', 'asdasda', 'asdasdas', 0);

-- --------------------------------------------------------

--
-- Estrutura da tabela `capela 2 avelar`
--

CREATE TABLE `capela 2 avelar` (
  `Pessoa` text NOT NULL,
  `Horario` text NOT NULL,
  `Sepultamento` text NOT NULL,
  `Cemiterio` text NOT NULL,
  `Status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `capela 2 avelar`
--

INSERT INTO `capela 2 avelar` (`Pessoa`, `Horario`, `Sepultamento`, `Cemiterio`, `Status`) VALUES
('Jose Cirino de Jesus', '12:45', '02/08/2019', 'Cemitério Municipal', 0);

-- --------------------------------------------------------

--
-- Estrutura da tabela `capela 3 avelar`
--

CREATE TABLE `capela 3 avelar` (
  `Pessoa` text NOT NULL,
  `Horario` text NOT NULL,
  `Sepultamento` text NOT NULL,
  `Cemiterio` text NOT NULL,
  `Status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
