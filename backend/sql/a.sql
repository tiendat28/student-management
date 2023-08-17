SELECT
    s.name as subject_name,
    concat(u.first_name, ' ', u.last_name) as teacher_name,
    ARRAY_agg(u2.first_name || ' ' || u2.last_name) as student_names,
    s.class_room
FROM
    subject s
JOIN
    teacher t ON s.teacher_id = t.id
JOIN
    "user" u ON t.user_id = u.id
JOIN
    student st ON s.student_ids @> ARRAY[st.id]
JOIN
    "user" u2 ON st.user_id = u2.id
GROUP BY
    s.name, u.first_name, u.last_name, s.class_room;

SELECT
    concat(u.first_name, ' ', u.last_name) as teacher_name,
    ARRAY_agg(s.name) as subjects
FROM
    teacher t
JOIN
    "user" u ON t.user_id = u.id
JOIN
    subject s ON t.id = s.teacher_id
GROUP BY
    u.first_name, u.last_name;

SELECT
    concat(u.first_name, ' ', u.last_name) as student_name,
   ARRAY_agg(s.name) as subjects
FROM
    student st
JOIN
    "user" u ON st.user_id = u.id
JOIN
    subject s ON st.id = ANY(s.student_ids)
GROUP BY
    u.first_name, u.last_name;
    
SELECT 
    subject.id as id,
    subject.name as name,
    concat(u2.first_name, ' ', u2.last_name) as teacher_name,
    ARRAY_agg(u1.first_name || ' ' || u1.last_name) as student_names,
    subject.class_room as class,
    subject.timetable as timetable,
    subject.active

FROM
    subject
JOIN
    teacher on subject.teacher_id = teacher.id
JOIN
    student ON subject.student_ids @> ARRAY[student.id]
JOIN
    "user" u2 ON teacher.user_id = u2.id
JOIN
    "user" u1 ON student.user_id = u1.id
GROUP BY
    subject.id, u2.first_name, u2.last_name;