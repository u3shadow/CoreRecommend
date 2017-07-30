DROP TABLE IF EXISTS `entries`;
CREATE TABLE `entries`(
  `id` INT AUTO_INCREMENT,
  `title` TEXT NOT NULL,
  `text` TEXT NOT NULL,
  PRIMARY KEY (`id`)
);