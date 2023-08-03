<?php

$text = strtolower(trim(readline("Digite um texto: ")));
$occurrences = substr_count($text, "a");
echo "A letra 'A' aparece {$occurrences} vezes.\n";
echo "A primeira letra 'A' aparece na posição " . strpos($text, "a") . PHP_EOL;
echo "A última letra 'A' aparece na posição " . strrpos($text, "a") . PHP_EOL;