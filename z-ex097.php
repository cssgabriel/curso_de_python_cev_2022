<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$msg = $read->read_str("Escreva uma mensagem: ");
echo textBox("$msg", null);