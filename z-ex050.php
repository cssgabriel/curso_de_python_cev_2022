<?php

$numbers = [];
$c = 0;
while ($c < 6) {
  $n = intval(readline("Digite um número: "));
  if ($n % 2 === 0) array_push($numbers, $n);
  $c++;
}

echo "A soma dos números pares foi de " . array_sum($numbers);
