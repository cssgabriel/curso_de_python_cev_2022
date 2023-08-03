<?php

$name = readline("Digite seu nome completo: ");
echo "Seu nome em letras maiúsculas: " . strtoupper($name) .  PHP_EOL;
echo "Seu nome em letras minúsculas: " . strtolower($name) . PHP_EOL;

$nameCondensed = strlen(implode("", explode(" ",$name)));
echo "Seu nome possui {$nameCondensed} letras.\n";

$firstName = explode(" ", $name)[0];
echo "Seu primeiro nome é {$firstName} e possui " . strlen($firstName) . " letras.";