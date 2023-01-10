-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3307
-- Tiempo de generación: 10-12-2022 a las 09:45:36
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `facturas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id_cliente` int(8) NOT NULL,
  `dni` varchar(40) DEFAULT NULL,
  `nombre` varchar(40) DEFAULT NULL,
  `empresa` varchar(40) DEFAULT NULL,
  `direccion` varchar(40) DEFAULT NULL,
  `tlf` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id_cliente`, `dni`, `nombre`, `empresa`, `direccion`, `tlf`) VALUES
(1, '956563', 'John Doe', 'Samsung', 'Av. 3', 52525252),
(2, '9419415', 'Erin Luca', 'Dell', 'Av. 5', 8596261),
(3, '9419555', 'Ann Smith', 'SUNAT', 'Av. 6', 4456422);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `id_empleado` int(8) NOT NULL,
  `nombre` varchar(40) DEFAULT NULL,
  `cargo` varchar(40) DEFAULT NULL,
  `direccion` varchar(40) DEFAULT NULL,
  `tlf` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`id_empleado`, `nombre`, `cargo`, `direccion`, `tlf`) VALUES
(1, 'Williams Monaco', 'vendedor', 'Av. 2', 96465263);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado`
--

CREATE TABLE `estado` (
  `id` int(2) NOT NULL,
  `estado` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estado`
--

INSERT INTO `estado` (`id`, `estado`) VALUES
(1, 'Pagada'),
(2, 'Pendiente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE `factura` (
  `numero_factura` int(8) NOT NULL,
  `id_cliente` int(8) DEFAULT NULL,
  `id_empleado` int(8) DEFAULT NULL,
  `metodo_pago` int(2) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `id_estado` int(2) DEFAULT NULL,
  `subtotal` int(8) DEFAULT NULL,
  `total` int(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `factura`
--

INSERT INTO `factura` (`numero_factura`, `id_cliente`, `id_empleado`, `metodo_pago`, `fecha`, `id_estado`, `subtotal`, `total`) VALUES
(1, 1, 1, 2, '2022-12-09', 1, 5000, 5900),
(125, 2, 1, 1, '2022-12-10', 1, 2000, 2360),
(128, 2, 1, 1, '2022-12-10', 1, 2500, 2950);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura_detalle`
--

CREATE TABLE `factura_detalle` (
  `codigo_detalle` int(8) NOT NULL,
  `numero_factura` int(8) DEFAULT NULL,
  `id_producto` int(8) DEFAULT NULL,
  `cantidad` int(3) DEFAULT NULL,
  `precio` int(8) DEFAULT NULL,
  `total_lineal` int(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `factura_detalle`
--

INSERT INTO `factura_detalle` (`codigo_detalle`, `numero_factura`, `id_producto`, `cantidad`, `precio`, `total_lineal`) VALUES
(1, 1, 1, 1, 500, 500),
(78, 125, 2, 1, 2000, 2000),
(80, 128, 4, 1, 2500, 2500);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `metodo`
--

CREATE TABLE `metodo` (
  `id` int(2) NOT NULL,
  `metodo` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `metodo`
--

INSERT INTO `metodo` (`id`, `metodo`) VALUES
(1, 'Efectivo'),
(2, 'Tarjeta de débito o crédito'),
(3, 'Transferencia'),
(4, 'Paypal');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id_producto` int(8) NOT NULL,
  `nombre` varchar(40) DEFAULT NULL,
  `precio` int(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id_producto`, `nombre`, `precio`) VALUES
(1, 'Mouse', 500),
(2, 'Monitor', 2000),
(3, 'Keyboard', 750),
(4, 'Chair', 2500),
(5, 'Telefono', 500),
(6, 'Tablet', 600),
(7, 'Microfono', 700),
(8, 'Auriculares', 800),
(9, 'Tv', 8900),
(10, 'USB', 100);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(8) NOT NULL,
  `id_empleado` int(8) DEFAULT NULL,
  `usuario` varchar(20) DEFAULT NULL,
  `pin` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `id_empleado`, `usuario`, `pin`) VALUES
(1, 1, 'WillM', 7878);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`id_empleado`);

--
-- Indices de la tabla `estado`
--
ALTER TABLE `estado`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`numero_factura`),
  ADD KEY `id_cliente` (`id_cliente`),
  ADD KEY `id_estado` (`id_estado`),
  ADD KEY `metodo_pago` (`metodo_pago`),
  ADD KEY `id_empleado` (`id_empleado`);

--
-- Indices de la tabla `factura_detalle`
--
ALTER TABLE `factura_detalle`
  ADD PRIMARY KEY (`codigo_detalle`),
  ADD KEY `numero_factura` (`numero_factura`),
  ADD KEY `id_producto` (`id_producto`);

--
-- Indices de la tabla `metodo`
--
ALTER TABLE `metodo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id_producto`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `id_empleado` (`id_empleado`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id_cliente` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `id_empleado` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `estado`
--
ALTER TABLE `estado`
  MODIFY `id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `factura`
--
ALTER TABLE `factura`
  MODIFY `numero_factura` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=129;

--
-- AUTO_INCREMENT de la tabla `factura_detalle`
--
ALTER TABLE `factura_detalle`
  MODIFY `codigo_detalle` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT de la tabla `metodo`
--
ALTER TABLE `metodo`
  MODIFY `id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id_producto` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `factura_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`),
  ADD CONSTRAINT `factura_ibfk_2` FOREIGN KEY (`id_estado`) REFERENCES `estado` (`id`),
  ADD CONSTRAINT `factura_ibfk_3` FOREIGN KEY (`metodo_pago`) REFERENCES `metodo` (`id`),
  ADD CONSTRAINT `factura_ibfk_4` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id_empleado`);

--
-- Filtros para la tabla `factura_detalle`
--
ALTER TABLE `factura_detalle`
  ADD CONSTRAINT `factura_detalle_ibfk_1` FOREIGN KEY (`numero_factura`) REFERENCES `factura` (`numero_factura`),
  ADD CONSTRAINT `factura_detalle_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id_empleado`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
