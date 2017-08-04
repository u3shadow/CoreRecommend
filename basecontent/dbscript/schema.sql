DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`(
  `id` INT AUTO_INCREMENT,
  `userid` TEXT NOT NULL,
  `name` TEXT NOT NULL,
  `psw` TEXT NOT NULL,
  `email` TEXT NOT NULL,
  PRIMARY KEY (`id`)
);
DROP TABLE IF EXISTS `games`;
CREATE TABLE `games`(
  `id` INT AUTO_INCREMENT,
  `name` TEXT NOT NULL,
  `steamid` INT,
  PRIMARY KEY (`id`)
);
DROP TABLE IF EXISTS `tags`;
CREATE TABLE `tags`(
  `id` INT AUTO_INCREMENT,
  `name` TEXT NOT NULL,
  PRIMARY KEY (`id`)
);
