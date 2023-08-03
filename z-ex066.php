<?php

require_once("z-line.php");
require_once("z-Read.php");
require_once("z-Numbers.php");

$read = new Read();
$numbers = new Numbers();

while (true) {
  $n = $read->read_int("Digite um valor (999 para parar): ");
  if ($n === 999) break;
  $numbers->setPushArr($n);
}

echo line();
echo "Você digitou \033[32m{$numbers->getCount()}\033[m números e a média foi \033[32m{$numbers->getAverage()}\033[m\n";
echo "O maior valor foi \033[32m{$numbers->getHighNumber()}\033[m e o menor foi \033[32m{$numbers->getSmallNumber()}\033[m\n";
echo "A soma dos números é \033[32m{$numbers->getSum()}\033[m\n";
echo line();