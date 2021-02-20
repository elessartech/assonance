CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    name TEXT, 
    email TEXT UNIQUE,
    role TEXT,
    password TEXT
);

CREATE TABLE notifications (
    id SERIAL PRIMARY KEY, 
    title TEXT, 
    description TEXT,
    publisher_id INTEGER
);

CREATE TABLE instruments (
    id SERIAL PRIMARY KEY, 
    name TEXT,
    notification_id INTEGER
);

CREATE TABLE genres (
    id SERIAL PRIMARY KEY, 
    name TEXT, 
    notification_id INTEGER
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY, 
    name TEXT,
    notification_id INTEGER
);

CREATE TABLE applications (
    id SERIAL PRIMARY KEY,  
    message TEXT,
    sender_id INTEGER,
    notification_id INTEGER
);