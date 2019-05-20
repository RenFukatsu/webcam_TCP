<?php
error_reporting(E_ALL);

// The maximum execution time, in seconds. If set to zero, no time limit is imposed.
set_time_limit(0);

$address = '127.0.0.1';
$port = 5007;

$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_bind($sock, $address, $port);
socket_listen($sock, 5);
while($msgsock = socket_accept($sock)){
    $data = socket_read($msgsock, 2048);
    echo $data . "\n";
    socket_close($msgsock);
}
socket_close($sock);
?>
