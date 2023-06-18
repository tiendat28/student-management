CREATE Table login(
    id bigserial,
    users TEXT,
    password TEXT,
    surname TEXT,
    name TEXT,
    email TEXT UNIQUE,
    active BOOLEAN DEFAULT true,
    constraint pkey_login PRIMARY KEY (id)    
);
SELECT * FROM login;
INSERT INTO login (users, password, surname,  name, active) VALUES ('hnam', '123', 'Hoàng', 'Nam', true);
UPDATE login set email = 'bang@gmail.com' WHERE id = '4'