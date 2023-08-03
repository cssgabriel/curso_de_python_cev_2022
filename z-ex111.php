<?php

require_once("z-line.php");
require_once("z-Read.php");
require_once("z-ex111/utilidades/moeda.php");
// require_once("z-Numbers.php");

$read = new Read();
$moeda = new Moeda();

$num = $read->read_float();
echo $moeda->resumo($num, 15, 15);