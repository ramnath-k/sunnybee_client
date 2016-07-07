CREATE TABLE `sunnybee`.`tag_tracker` (
  `idtag_tracker` BIGINT NOT NULL AUTO_INCREMENT,
  `tag_id` VARCHAR(1024) NOT NULL,
  `antenna` VARCHAR(1024) NOT NULL,
  `reader` VARCHAR(1024) NOT NULL,
  `status` INT NOT NULL,
  `updated_time` DATETIME NOT NULL,
  `created_time` DATETIME NOT NULL,
  PRIMARY KEY (`idtag_tracker`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8
