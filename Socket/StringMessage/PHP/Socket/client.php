<?php
error_reporting(E_ALL);

echo "<h2>TCP/IP Connection</h2>\n";

$address = '127.0.0.1';
$port = 5007;


$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_connect($sock, $address, $port);
$msg = "dedede";
socket_write($sock, $msg, strlen($msg));

socket_close($sock);
