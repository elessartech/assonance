CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    name TEXT NOT NULL, 
    email TEXT UNIQUE NOT NULL,
    role TEXT,
    password TEXT NOT NULL,
    created_on TEXT  
);

CREATE TABLE notifications (
    id SERIAL PRIMARY KEY, 
    title TEXT NOT NULL, 
    description TEXT,
    publisher_id INTEGER REFERENCES users ON DELETE CASCADE,
    hidden INTEGER DEFAULT 0,
    created_on TEXT
);

CREATE TABLE instruments (
    id SERIAL PRIMARY KEY, 
    name TEXT NOT NULL,
    notification_id INTEGER REFERENCES notifications ON DELETE CASCADE
);

CREATE TABLE genres (
    id SERIAL PRIMARY KEY, 
    name TEXT NOT NULL, 
    notification_id INTEGER REFERENCES notifications ON DELETE CASCADE
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY, 
    name TEXT NOT NULL,
    notification_id INTEGER REFERENCES notifications ON DELETE CASCADE
);

CREATE TABLE applications (
    id SERIAL PRIMARY KEY,  
    message TEXT NOT NULL,
    sender_id INTEGER REFERENCES users ON DELETE CASCADE,
    notification_id INTEGER REFERENCES notifications ON DELETE CASCADE,
    created_on TEXT
);