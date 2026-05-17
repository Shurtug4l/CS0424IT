// DATABASE MARIADB
// CREATE DATABASE secretdb;
// USE secretdb;

// CREATE TABLE users (
// id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
// name VARCHAR(50) NOT NULL,
// email VARCHAR(50),
// birthdate DATE,
// address VARCHAR(100),
// phone VARCHAR(15)
// );

// INSERT INTO users (name, email, birthdate, address, phone) VALUES
// ('Alice Smith', 'alice@example.com', '1990-01-01', '123 Apple St, Wonderland', '123-456-7890'),
// ('Bob Johnson', 'bob@example.com', '1985-05-15', '456 Orange Ave, Dreamland', '234-567-8901'),
// ('Charlie Brown', 'charlie@example.com', '1992-12-20', '789 Banana Blvd, Fantasyland', '345-678-9012');

// Rileva le vulnerabilità SQL Injection nell’URL specificato e elenca i database disponibili
// sqlmap -u "http://localhost/vulnerable.php?id=1" --dbs

// Estrae tutti i dati dalla tabella users nel database secretdb
// sqlmap -u "http://localhost/vulnerable.php?id=1" -D secretdb -T users --dump


<?php
$servername = "localhost";
$username = "root";
$password = "your_mysql_root_password";
$dbname = "secretdb";

// Creazione connessione
$conn = new mysqli($servername, $username, $password, $dbname);

// Controllo connessione
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Ottenere l'input dell'utente
$user_input = $_GET['id'];

// Query SQL vulnerabile
$sql = "SELECT * FROM users WHERE id = " . $user_input;
echo "Query: $sql<br>";  // Aggiunto per debug
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Output dei dati
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Name: " . $row["name"]. " - Email: " . $row["email"]. " - Birthdate: " . $row["birthdate"]. " - Address: " . $row["address"]. " - Phone: " . $row["phone"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
