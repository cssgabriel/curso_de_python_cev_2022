<?php

$people = [];
$c = 0;
while ($c < 7) {
  $year = (int) readline("Digite o ano de nascimento: ");
  $age = date("Y") - $year;
  if ($age < 21) array_push($people, $age);
  $c++;
}

$menor = count($people);
$maior = 7 - $menor;

echo "{$maior} são maiores.\n{$menor} são menores.";
