<?php

require_once("z-line.php");
require_once("z-Read.php");
require_once("z-ex109/moeda.php");
// require_once("z-Numbers.php");

$read = new Read();
$moeda = new Moeda();
$num = $read->read_float("Digite um valor: R$ ");
echo "O dobro de {$moeda->moeda($num)} é {$moeda->dobro($num, true)}\n";
echo "A metade de {$moeda->moeda($num)} é {$moeda->metade($num, true)}\n";
$taxa = $read->read_float("Qual taxa você deseja aplicar? ");
echo "{$moeda->moeda($num)} mais {$taxa}% vai para {$moeda->aumentar($num, $taxa, true)}\n";
echo "{$moeda->moeda($num)} menos {$taxa}% vai para {$moeda->diminuir($num, $taxa, true)}\n";