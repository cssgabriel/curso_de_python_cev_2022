<?php

$frase = strtolower(trim(readline("Digite uma frase: ")));
$frase = implode("", explode(" ", $frase));
$reverse = strrev($frase);

echo $frase === $reverse ? "Este é um palíndromo!" : "Não é um palíndromo.";
