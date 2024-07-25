\c db;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    names VARCHAR(150) NOT NULL,
    sname VARCHAR(150),
    email VARCHAR(150) UNIQUE NOT NULL,
    passwords VARCHAR(150) NOT NULL,
    secrets VARCHAR(150) NOT NULL,
    tg VARCHAR(150) UNIQUE,
    friends VARCHAR(550),
    roles VARCHAR(10) NOT NULL,
    comment VARCHAR(250),
    birthday VARCHAR(50),
    register_date VARCHAR(50) NOT NULL,
    sex VARCHAR(3) NOT NULL,
    phone VARCHAR(12)
);

CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    locations VARCHAR(150) NOT NULL,
    coordinates_latitude VARCHAR(150) NOT NULL,
    coordinates_longitude VARCHAR(150) NOT NULL,
    img_ways VARCHAR(1050),
    descriptions VARCHAR(500),
    short_description VARCHAR(550),
    story VARCHAR(150) NOT NULL,
    privates VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL
);
