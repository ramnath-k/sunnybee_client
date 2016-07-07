CREATE TABLE `sunnybee`.`store_reader` (
  `idstore_reader` BIGINT NOT NULL AUTO_INCREMENT,
  `reader` VARCHAR(1024) NOT NULL,
  `store` VARCHAR(1024) NOT NULL,
  `status` INT NOT NULL,
  `updated_time` DATETIME NOT NULL,
  `created_time` DATETIME NOT NULL,
  PRIMARY KEY (`idstore_reader`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8
