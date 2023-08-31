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
