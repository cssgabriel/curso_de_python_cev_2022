<?php

$weight = (float) readline("Digite seu peso (kg): ");
$height = (float) readline("Digite sua altura (m): ");
$imc = $weight / $height ** 2;

switch ($imc) {
  case $imc < 18.5:
    echo "ABAIXO DO PESO";
    break;
  case $imc <= 25:
    echo "PESO IDEAL";
    break;
  case $imc <= 30:
    echo "SOBREPESO";
    break;
  case $imc <= 40:
    echo "OBESIDADE";
    break;
  case $imc > 40:
    echo "OBESIDADE MÓRBIDA";
    break;
  default:
    echo "Valor inválido.";
    break;
}


