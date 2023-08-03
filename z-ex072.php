<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$arr = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove","dez", "onze", "doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte"];

$read = new Read();

while (true) {
  $value = $read->read_int("Digite um valor entre 0 e 20: ");
  if ($value < 0 || $value > 20) echo "Valor inválido. Tente novamente.\n";
  else {
    echo "O valor digitador foi {$arr[$value]}\n";
    $opt = $read->read_str("Você quer continuar? [S/N] ", ["s", "n"]);
    if ($opt === "n") break;
  }
}
  