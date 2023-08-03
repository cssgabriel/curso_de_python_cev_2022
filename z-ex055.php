<?php

$pesos = [];
for ($i = 0; $i < 5; $i++) {
  $peso = (float) readline("Peso (kg): ");
  array_push($pesos, $peso);
}
$pesoMax = max($pesos);
$pesoMin = min($pesos);
echo "O maior peso lido foi de {$pesoMax} Kg.\nO menor peso lido foi de {$pesoMin} Kg";
