-- Create the List table
CREATE TABLE IF NOT EXISTS List (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted BOOLEAN DEFAULT FALSE
);

-- Create an index on the name column for List (optional)
CREATE INDEX idx_list_name ON List (name);

-- Create the uploaded_data table
CREATE TABLE IF NOT EXISTS uploaded_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data JSON,
    list_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (list_id) REFERENCES List(id)
);

-- Create an index on the list_id column for uploaded_data (optional)
CREATE INDEX idx_uploaded_data_list_id ON uploaded_data (list_id);

-- Create the template table
CREATE TABLE IF NOT EXISTS template (
    id INT AUTO_INCREMENT PRIMARY KEY,
    body TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted BOOLEAN DEFAULT FALSE
);

-- Create the Campaign table
CREATE TABLE IF NOT EXISTS Campaign (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    list_id INT,
    template_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (list_id) REFERENCES List(id),
    FOREIGN KEY (template_id) REFERENCES template(id)
);

-- Create an index on the name column for Campaign (optional)
CREATE INDEX idx_campaign_name ON Campaign (name);

-- Create an index on the list_id column for Campaign (optional)
CREATE INDEX idx_campaign_list_id ON Campaign (list_id);

-- Create an index on the template_id column for Campaign (optional)
CREATE INDEX idx_campaign_template_id ON Campaign (template_id);

-- Create the sent_emails table
CREATE TABLE IF NOT EXISTS sent_emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    list_id INT,
    campaign_id INT,
    uploaded_data_id INT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (list_id) REFERENCES List(id),
    FOREIGN KEY (campaign_id) REFERENCES Campaign(id),
    FOREIGN KEY (uploaded_data_id) REFERENCES uploaded_data(id)
);

-- Create an index on the email column for sent_emails (optional)
CREATE INDEX idx_sent_emails_email ON sent_emails (email);

-- Create an index on the list_id column for sent_emails (optional)
CREATE INDEX idx_sent_emails_list_id ON sent_emails (list_id);

-- Create an index on the campaign_id column for sent_emails (optional)
CREATE INDEX idx_sent_emails_campaign_id ON sent_emails (campaign_id);

-- Create an index on the uploaded_data_id column for sent_emails (optional)
CREATE INDEX idx_sent_emails_uploaded_data_id ON sent_emails (uploaded_data_id);
