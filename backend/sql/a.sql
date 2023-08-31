SELECT
    concat("user".first_name, ' ', "user".last_name) as aname,
    questions.q_text,
    answers.select_answer
FROM
    answers
JOIN
    "user" ON answers.user_id = "user".id
JOIN
    questions ON answers.q_id = questions.id;

SELECT * FROM pg_log ORDER BY log_time DESC