<?php

# Exercício já resolvido no arquivo "z-Read.php"
# Toda validação já é feita garantindo o type safety

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");


$read = new Read();
$n = $read->read_int();

echo "Você digitou o número {$n}.";