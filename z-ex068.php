<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
//$numbers = new Numbers();
$wins = 0;

while (true) {
  $user = $read->read_int("Digite um valor: ");
  $choice = $read->read_str("Par ou Ímpar [P/I]? ", ["p","i"]);
  $computer = rand(0, 10);
  $total = $user + $computer;

  echo "Você jogou {$user} e o computador jogou {$computer}.\n";
  echo "Total: {$total} -> ";
  $res = $total % 2 === 0 ? "p" : "i";

  echo $res === "p" ? "DEU PAR!\n" : "DEU ÍMPAR\n";
  if ($res === $choice) {
    echo "Você VENCEU!\nVamos jogar novamente.";
    $wins++;
  }
  else {
    echo "Você PERDEU!\nGAME OVER! Você venceu {$wins} vezes consecutivas.";
    break;
  }
}