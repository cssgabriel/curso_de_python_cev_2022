<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$numbers = [];

while (true) {
  $n = $read->read_int("Adicione um valor: ");
  if (is_int(array_search($n, $numbers))) echo "Valor já existente. Não poderá ser adicionado!\n";
  else {
    array_push($numbers, $n);
    echo "Valor adicionado com sucesso!\n";
  }
  $opt = $read->read_str("Quer adicionar outro valor? [S/N] ", ["s", "n"]);
  if ($opt === "n") break; 
}

sort($numbers);
echo "Os valores adicionados foram: " . implode(", ", $numbers);
