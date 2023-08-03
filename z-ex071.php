<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

echo line();
echo "CAIXA ELETRÔNICO\n";
echo line();

$read = new Read();
$value = $read->read_int("Que valor você quer sacar? R$ ");
$ced = ['50' => 0, '20' => 0, '10' => 0, '1' => 0];

while ($value > 0) {
  if ($value >= 50) {
    $value -= 50;
    $ced['50'] += 1;
    echo "+ 1 cédula de R$ 50.\n";
  }
  else if ($value >= 20) {
    $value -= 20;
    $ced['20'] += 1;
    echo "+ 1 cédula de R$ 20.\n";
  }
  else if ($value >= 10) {
    $value -= 10;
    $ced['10'] += 1;
    echo "+ 1 cédula de R$ 10.\n";
  }
  else {
    $value--;
    $ced['1'] += 1;
    echo "+ 1 cédula de R$ 1.\n";
  }
}
echo line();
echo "{$ced['50']} notas de 50.\n";
echo "{$ced['20']} notas de 20.\n";
echo "{$ced['10']} notas de 10.\n";
echo "{$ced['1']} notas de 1.\n";
echo line();
echo "SAQUE REALIZADO COM SUCESSO.";