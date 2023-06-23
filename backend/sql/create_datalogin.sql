CREATE Table users(
    id bigserial,
    users TEXT,
    password TEXT,
    surname TEXT,
    name TEXT,
    email TEXT UNIQUE,
    role TEXT,
    active BOOLEAN DEFAULT true,
    constraint pkey_login PRIMARY KEY (id)    
);
SELECT * FROM users;
INSERT INTO users (users, password, surname,  name, active) VALUES ('hnam', '123', 'Hoàng', 'Nam', true);
UPDATE users set surname = 'Mai Thanh' WHERE id = '12'