-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 02-Ago-2019 às 22:10
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
-- Database: `avelar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `salas`
--

CREATE TABLE `salas` (
  `num_sala` int(11) NOT NULL,
  `Sala` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `salas`
--

INSERT INTO `salas` (`num_sala`, `Sala`) VALUES
(1, 'Capela Avelar 1');

-- --------------------------------------------------------

--
-- Estrutura da tabela `velorios`
--

CREATE TABLE `velorios` (
  `Velorio` int(11) DEFAULT NULL,
  `Sala` int(11) NOT NULL,
  `Pessoa` text NOT NULL,
  `Hora_saida` text NOT NULL,
  `Data_sepultamento` text NOT NULL,
  `Cemiterio` text NOT NULL,
  `Status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `velorios`
--

INSERT INTO `velorios` (`Velorio`, `Sala`, `Pessoa`, `Hora_saida`, `Data_sepultamento`, `Cemiterio`, `Status`) VALUES
(NULL, 1, 'Ciclano', '12:08', 'asdas', 'asdasd', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `salas`
--
ALTER TABLE `salas`
  ADD UNIQUE KEY `num_sala` (`num_sala`);

--
-- Indexes for table `velorios`
--
ALTER TABLE `velorios`
  ADD UNIQUE KEY `num_velorio` (`Velorio`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
