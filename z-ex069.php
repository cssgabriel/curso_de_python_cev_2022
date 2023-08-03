<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$people = [];

while (true) {
  $age = $read->read_int("Idade: ");
  $gender = $read->read_str("Sexo [M/F]: ", ["m","f"]);
  array_push($people, ["age" => $age, "gender" => $gender]);
  $opt = $read->read_str("Quer continuar [S/N]? ", ["n","s"]);
  if ($opt === "n") break;
}

function maior18() {
  global $people;
  return count(array_filter($people, fn($p) => $p['age'] > 18));
}

function men() {
  global $people;
  return count(array_filter($people, fn($p) => $p['gender'] === "m"));
}

function women() {
  global $people;
  return count(array_filter($people, fn($p) => $p['gender'] === "f" && $p['age'] < 20));
}

echo "Total de pessoas com mais de 18 anos: " . maior18() . PHP_EOL;
echo "Ao todo temos " . men() . " homens cadastrados.\n";
echo "E temos " . women() . "  mulheres com menos de 20 anos.\n";
