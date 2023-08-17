drop table IF exists questions cascade;
CREATE TABLE questions (
    id bigserial,
    q_text VARCHAR,
    option1 VARCHAR,
    option2 VARCHAR,
    option3 VARCHAR,
    option4 VARCHAR,
    date_from DATE,
    date_to DATE,
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
)