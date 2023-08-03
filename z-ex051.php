<?php

$termo = intval(readline("Digite o primeiro termo: "));
$razao = intval(readline("Digite qual a razão: "));

$decimo = $termo + 10 * $razao;

for ($i = $termo; $i < $decimo; $i += $razao ) {
  echo "$i\n";
}