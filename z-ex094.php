<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$people = [];
while (true) {
  $name = $read->read_str("Nome: ");
  $age = $read->read_int("Idade: ");
  $gender = $read->read_str("Sexo: [F/M] ", ["f", "m"]);
  $people[] = ["name" => $name, "age" => $age, "gender" => $gender];
  $opt = $read->read_str("Quer continuar? [S/N] ", ["s", "n"]);
  if ($opt === "n") break;
}

$a = count($people);
$b = array_reduce($people, fn($acc, $p) => [$acc[0] += $p["age"], $acc[0] / $a], [0])[1];
$c = implode(", ", array_map(fn($p) => $p["name"] ,array_filter($people, fn($p) => $p['gender'] === "f")));
$d = implode(", ", array_map(fn($p) => $p["name"] ,array_filter($people, fn($p) => $p["age"] > $b)));

echo line();
echo <<<PRINTDATA
A) Ao todo temos {$a} pessoas cadastradas.
B) A média de idade é de {$b}.
C) As mulheres cadastradas foram: {$c}
D) Pessoas que estão acima da média: {$d}

PRINTDATA;