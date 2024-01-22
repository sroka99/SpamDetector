CREATE TABLE IF NOT EXISTS mails_ham (
    id INT AUTO_INCREMENT PRIMARY KEY,
    received_date DATETIME NOT NULL,
    sender VARCHAR(255) NOT NULL,
    content TEXT
);

CREATE TABLE IF NOT EXISTS mails_spam (
    id INT AUTO_INCREMENT PRIMARY KEY,
    received_date DATETIME NOT NULL,
    sender VARCHAR(255) NOT NULL,
    content TEXT
);
