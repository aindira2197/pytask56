CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(255)
);

CREATE TABLE queue (
    id INT PRIMARY KEY,
    customer_id INT,
    service VARCHAR(255),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE INDEX idx_customer_id ON queue (customer_id);
CREATE INDEX idx_service ON queue (service);
CREATE INDEX idx_status ON queue (status);

INSERT INTO customers (id, name, phone, email) VALUES
(1, 'John Doe', '1234567890', 'john@example.com'),
(2, 'Jane Doe', '0987654321', 'jane@example.com'),
(3, 'Bob Smith', '5551234567', 'bob@example.com');

INSERT INTO queue (id, customer_id, service, status) VALUES
(1, 1, 'Haircut', 'pending'),
(2, 2, 'Nail trim', 'pending'),
(3, 3, 'Shave', 'pending'),
(4, 1, 'Beard trim', 'in_progress'),
(5, 2, 'Waxing', 'done');

CREATE VIEW queue_status AS
SELECT service, COUNT(*) AS count
FROM queue
GROUP BY service;

CREATE PROCEDURE add_to_queue(
    IN customer_id INT,
    IN service VARCHAR(255)
)
BEGIN
    INSERT INTO queue (customer_id, service, status) VALUES (customer_id, service, 'pending');
END;

CREATE PROCEDURE update_queue_status(
    IN queue_id INT,
    IN status VARCHAR(20)
)
BEGIN
    UPDATE queue SET status = status WHERE id = queue_id;
END;

SELECT * FROM queue;
SELECT * FROM customers;
SELECT * FROM queue_status;

CALL add_to_queue(1, 'Haircut');
CALL update_queue_status(1, 'in_progress');

SELECT * FROM queue;