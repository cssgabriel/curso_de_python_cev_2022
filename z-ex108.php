<?php

require_once("z-line.php");
require_once("z-Read.php");
require_once("z-ex108/moeda.php");
// require_once("z-Numbers.php");

$read = new Read();
$moeda = new Moeda();
$num = $read->read_float("Digite um valor: R$ ");
echo "O dobro de {$moeda->moeda($num)} é {$moeda->dobro($num)}\n";
echo "A metade de {$moeda->moeda($num)} é {$moeda->metade($num)}\n";
$taxa = $read->read_float("Qual taxa você deseja aplicar? ");
echo "{$moeda->moeda($num)} mais {$taxa}% vai para R$ {$moeda->aumentar($num, $taxa)}\n";
echo "{$moeda->moeda($num)} menos {$taxa}% vai para R$ {$moeda->diminuir($num, $taxa)}\n";