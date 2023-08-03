<?php

$person = [];
$older = [0,null];
$womenUnder20 = 0;
for ($i = 0; $i < 5; $i++) {
  $name = trim(readline("Nome: "));
  $age = (int) readline("Idade: ");
  $gender = strtolower(trim(readline("Sexo [F/M]: ")));
  $person[$name] = [$name, $age, $gender];
  if ($age > $older[0]) $older = [$age, $name];
  if ($gender === "f" && $age < 20) $womenUnder20++;
  echo str_repeat("-=", 13) . PHP_EOL;
}

function averageAge($arr) {
  $sum = array_reduce($arr, fn($acc, $person) => $acc + $person[1]);
  return $sum / count($arr);
}

$avAge = averageAge($person);
echo "A média de idade do grupo é de {$avAge} anos.\n";
echo "O nome do homem mais velho é {$older[1]}.\n";
echo "Desse grupo, {$womenUnder20} mulheres possuem até 20 anos de idade.\n";
