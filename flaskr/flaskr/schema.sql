DROP TABLE IF EXISTS `entries`;
DROP TABLE IF EXISTS `users`;
CREATE TABLE `entries`(
  `id` INT AUTO_INCREMENT,
  `title` TEXT NOT NULL,
  `text` TEXT NOT NULL,
  PRIMARY KEY (`id`)
);
CREATE TABLE `users`(
  `id` INT AUTO_INCREMENT,
  `userid` TEXT NOT NULL,
  `name` TEXT NOT NULL,
  `psw` TEXT NOT NULL,
  `email` TEXT NOT NULL,
  PRIMARY KEY (`id`)
);