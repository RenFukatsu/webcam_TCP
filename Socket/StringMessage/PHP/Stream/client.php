<?php

$socket = stream_socket_client('tcp://127.0.0.1:5007');
fwrite($socket, 'hi');
fclose($socket);

?>