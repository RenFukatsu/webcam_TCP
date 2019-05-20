<?php
set_time_limit(0);

$sock = stream_socket_server('tcp://127.0.0.1:5007');

while($msgsock = stream_socket_accept($sock)){
    $data = stream_get_contents($msgsock);
    $json = json_decode($data, true);
    echo $json['data']['name'];
    fclose($msgsock);
}
fclose($sock);

?>