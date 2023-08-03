<?php

$city = trim(readline("Digite o nome de uma cidade: "));
$validation = (str_contains("santo", strtolower(substr($city, 0, 5))) && $city);
echo $validation;