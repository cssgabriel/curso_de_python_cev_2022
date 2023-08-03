<?php

$termo = intval(readline("Digite o primeiro termo: "));
$razao = intval(readline("Digite qual a razão: "));

$i = 0;
$enesimo = 10;
while ($enesimo !== 0) {
  echo "\033[0;32m";
  while ($i < $enesimo) {
    echo "{$termo} -> ";
    $termo += $razao;
    $i += 1;
  }
  echo "FIM!\033[0m\n";
  $enesimo = (int) readline("Quer mostrar mais termos? Digite quantos: ");
  $i = 0;
}

