SELECT * FROM tasks WHERE user_id = 4;
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 3;
SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);
INSERT INTO tasks (title, description, status_id, user_id) VALUES ('Task title', 'Task description', 1, 4);
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');
DELETE FROM tasks WHERE id = 3;
