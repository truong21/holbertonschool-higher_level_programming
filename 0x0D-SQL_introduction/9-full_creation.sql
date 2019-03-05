-- creates a second table and add multiple rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- Insert John
INSERT INTO second_table (`id`, `name`, `score`) VALUES (1, "John", 10);
-- Insert Alex
INSERT INTO second_table (`id`, `name`, `score`) VALUES (2, "Alex", 3);
-- Insert Bob
INSERT INTO second_table (`id`, `name`, `score`) VALUES (3, "Bob", 14);
-- Insert George
INSERT INTO second_table (`id`, `name`, `score`) VALUES (4, "George", 8);
