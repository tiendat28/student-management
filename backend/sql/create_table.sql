drop table IF exists "user" cascade;
CREATE TABLE "user" (
    id bigserial,
    username VARCHAR,
    password VARCHAR,
    first_name VARCHAR,
    last_name VARCHAR,
    phone VARCHAR,
    address VARCHAR,
    email VARCHAR,
    sex varchar,
    role VARCHAR,
    active bool DEFAULT true,
    CONSTRAINT pkey_user PRIMARY KEY (id)
);
INSERT INTO "user" (username, password, role, active) values ('admin', 123, 'Manager', TRUE);
drop table IF exists teacher cascade;
CREATE TABLE teacher (
    id bigserial,
    user_id INTEGER,
    active bool DEFAULT true,
    CONSTRAINT pkey_teacher PRIMARY KEY (id)
);
drop table IF exists student cascade;
CREATE TABLE student (
    id bigserial,
    user_id INTEGER,
    subject_id INTEGER,
    active bool DEFAULT true,
    CONSTRAINT pkey_student PRIMARY KEY (id)
);
drop table IF exists subject cascade;
CREATE TABLE subject (
    id bigserial,
    teacher_id INTEGER,
    student_ids INTEGER,
    name VARCHAR,
    class_name VARCHAR,
    timetable VARCHAR,
    active bool DEFAULT true,
    CONSTRAINT pkey_subject PRIMARY KEY (id)
);
drop table IF exists attendance cascade;
CREATE TABLE attendance (
    id bigserial,
    subject_id INTEGER,
    teacher_id INTEGER,
    student_id INTEGER,
    date DATE,
    status VARCHAR,
    active bool DEFAULT true,
    CONSTRAINT pkey_attendance PRIMARY KEY (id)
);
drop table IF exists questions cascade;
CREATE TABLE questions (
    id bigserial,
    q_text VARCHAR,
    option1 VARCHAR,
    option2 VARCHAR,
    option3 VARCHAR,
    option4 VARCHAR,
    date_from VARCHAR,
    date_to VARCHAR,
    score INTEGER,
    correct_answer VARCHAR,
    active bool DEFAULT true,
    CONSTRAINT pkey_questions PRIMARY KEY (id)
);

drop table IF exists answers cascade;
CREATE TABLE answers (
    id bigserial,
    q_id INTEGER,
    user_id INTEGER,
    select_answer VARCHAR,
    is_correct BOOLEAN,
    active bool DEFAULT true,
    CONSTRAINT pkey_answers PRIMARY KEY (id)
);

drop table IF exists todolist cascade;
CREATE TABLE todolist (
    id bigserial,
    subject_id INTEGER,
    teacher_id INTEGER,
    student_id INTEGER,
    name VARCHAR,
    time VARCHAR,
    level VARCHAR,
    status BOOLEAN,
    active bool DEFAULT true,
    CONSTRAINT pkey_todolist PRIMARY KEY (id)
);
