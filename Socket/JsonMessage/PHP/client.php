<?php

$strJson = '{"seq" : 0, "command" : "get_image", "data" : { "number" : "15", "name" : "Jon"}}';

$socket = stream_socket_client('tcp://127.0.0.1:5007');
fwrite($socket, $strJson);
fclose($socket);

?>