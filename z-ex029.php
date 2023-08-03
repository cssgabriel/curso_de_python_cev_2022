<?php

$speed = (float) readline("Qual a velocidade do seu carro? ");

if ($speed > 80) {
  echo "Você foi MULTADO!\n";
  $multa = ($speed - 80) * 7;
  echo "Valor da multa: R$ {$multa}.\n";
} else {
  echo "Você está dentro do limite de velocidade.\n";
}

echo "Tenha um boa viagem!";