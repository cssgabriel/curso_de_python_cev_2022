<?php

$sum = 0;
$c = 0;
for ($i = 0; $i <= 500 ; $i++) {
  if ($i % 3 === 0) {
    $c++;
    $sum += $i;
  }
}

echo "Foram encontrados {$c} números ímpares que são divisíveis por 3.\n";
echo "A soma de todos eles dá {$sum}.";
