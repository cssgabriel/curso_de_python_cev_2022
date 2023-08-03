<?php

$text = trim(readline("Digite seu nome completo: "));
$separa = explode(" ", $text);
echo "Seu primeiro nome é " . $separa[0] . PHP_EOL;
echo "Seu último nome é " . end($separa) . PHP_EOL;