DROP TABLE IF EXISTS users;
CREATE TABLE users(
  id serial PRIMARY KEY,
  userid TEXT NOT NULL,
  name TEXT NOT NULL,
  psw TEXT NOT NULL,
  email TEXT NOT NULL
);
DROP TABLE IF EXISTS games;
CREATE TABLE games(
  id  serial PRIMARY KEY,
  name TEXT NOT NULL,
  steamid INT
);
DROP TABLE IF EXISTS tags;
CREATE TABLE tags(
  id  serial PRIMARY KEY,
  name TEXT NOT NULL
);
