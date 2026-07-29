-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_simulacro
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_simulacro
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_simulacro` DEFAULT CHARACTER SET utf8 ;
USE `esquema_simulacro` ;

-- -----------------------------------------------------
-- Table `esquema_simulacro`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_simulacro`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_simulacro`.`viajes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_simulacro`.`viajes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `destino` VARCHAR(45) NOT NULL,
  `fecha_inicio` DATE NOT NULL,
  `fecha_fin` DATE NOT NULL,
  `itinerario` VARCHAR(40) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `organizador_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_viajes_usuarios_idx` (`organizador_id` ASC) VISIBLE,
  CONSTRAINT `fk_viajes_usuarios`
    FOREIGN KEY (`organizador_id`)
    REFERENCES `esquema_simulacro`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_simulacro`.`viajeros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_simulacro`.`viajeros` (
  `viaje_id` INT NOT NULL,
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`viaje_id`, `usuario_id`),
  INDEX `fk_viajes_has_usuarios_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  INDEX `fk_viajes_has_usuarios_viajes1_idx` (`viaje_id` ASC) VISIBLE,
  CONSTRAINT `fk_viajes_has_usuarios_viajes1`
    FOREIGN KEY (`viaje_id`)
    REFERENCES `esquema_simulacro`.`viajes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_viajes_has_usuarios_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `esquema_simulacro`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
