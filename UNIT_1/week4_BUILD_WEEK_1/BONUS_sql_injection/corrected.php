<?php
// L’uso di query preparate (tutti i parametri trattati come dati) e 
// dichiarazioni precompilate è una delle migliori pratiche per 
// proteggere le applicazioni web dalle vulnerabilità SQL Injection. 
// Questo metodo garantisce che gli input degli utenti vengano trattati in modo sicuro,
// prevenendo l’esecuzione di codice SQL non autorizzato.

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

// Preparazione della query SQL con un segnaposto (?) per il parametro id.
$stmt = $conn->prepare("SELECT * FROM users WHERE id = ?");

// Il metodo bind_param associa il parametro $user_input alla query. 
// Il tipo di dato i indica che il parametro è un intero.
$stmt->bind_param("i", $user_input);

// Esecuzione della query
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows > 0) {
    // Output dei dati
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Name: " . $row["name"]. " - Email: " . $row["email"]. " - Birthdate: " . $row["birthdate"]. " - Address: " . $row["address"]. " - Phone: " . $row["phone"]. "<br>";
    }
} else {
    echo "0 results";
}

// Chiusura della dichiarazione e della connessione
$stmt->close();
$conn->close();
?>
