<?php

# exercício já resolvido no arquivo 'z-Read.php'

require_once("z-line.php");
require_once("z-Read.php");
// require_once("z-ex112/utilidades/moeda.php");
// require_once("z-Numbers.php");

$read = new Read();

$int = $read->read_int();
$float = $read->read_float();
echo "O primeiro número que você digitou foi: {$int}";
echo "O segundo número que você digitou foi: {$float}";