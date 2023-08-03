<?php

$n = intval(readline("Digite um número: "));
$divisores = [];

for ($i = 1; $i <= $n; $i++) {
  if ($n % $i === 0) array_push($divisores, $i);
}

echo "Esse número é divisível por: " . implode(", ", $divisores);
echo ".\n";
$count = count($divisores);
if ($divisores[0] === 1 && $divisores[1] === $n) {
  echo "Foi dividido apenas {$count} vezes (por 1 e por ele mesmo).\nPor isso ele é um número PRIMO.";
} else {
  echo "Esse número foi divido {$count} vezes. Não é PRIMO.";
}