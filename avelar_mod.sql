-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 08-Ago-2019 às 21:06
-- Versão do servidor: 10.1.31-MariaDB
-- PHP Version: 7.2.4

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
(1, 'Capela Avelar 1'),
(2, 'Capela Avelar 2'),
(3, 'Capela Avelar 3'),
(4, 'Capela Avelar 4'),
(5, 'Capela Avelar 5');

-- --------------------------------------------------------

--
-- Estrutura da tabela `velorios`
--

CREATE TABLE `velorios` (
  `id` int(11) NOT NULL,
  `data_velorio` varchar(10) NOT NULL,
  `hora_inicio_velorio` varchar(5) NOT NULL,
  `num_sala` int(11) NOT NULL,
  `Pessoa` text NOT NULL,
  `Hora_saida` text NOT NULL,
  `Data_sepultamento` text NOT NULL,
  `Cemiterio` text NOT NULL,
  `Status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `velorios`
--

INSERT INTO `velorios` (`id`, `data_velorio`, `hora_inicio_velorio`, `num_sala`, `Pessoa`, `Hora_saida`, `Data_sepultamento`, `Cemiterio`, `Status`) VALUES
(1, '12/09/2019', '12:30', 2, 'Ciclano', '12:08', 'asdas', 'asdasd', 1),
(2, '12/09/2019', '11:40', 1, 'Jorge', '12:40', '12/09/2019', 'bonfim', 0),
(5, '12/09/2019', '11:55', 4, 'Gilson', '13:30', '12/09/2019', 'bonfim', 1),
(6, '12/09/2019', '12:55', 5, 'Geron', '13:30', '12/09/2019', 'bonfim', 1),
(7, '12/09/2019', '12:25', 3, 'Pedro', '13:30', '12/09/2019', 'bonfim', 1);

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
  ADD PRIMARY KEY (`id`),
  ADD KEY `num_sala` (`num_sala`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `velorios`
--
ALTER TABLE `velorios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Limitadores para a tabela `velorios`
--
ALTER TABLE `velorios`
  ADD CONSTRAINT `velorios_ibfk_1` FOREIGN KEY (`num_sala`) REFERENCES `salas` (`num_sala`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
