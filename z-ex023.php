<?php

$n = intval(readline("Digite um número entre 0000 e 9999: "));
$un = intdiv($n, 1) % 10;
$dz = intdiv($n, 10) % 10;
$ct = intdiv($n, 100) % 10;
$ml = intdiv($n, 1000);
echo <<<"OUT"
  Unidade: {$un}
  Dezena: {$dz}
  Centena: {$ct}
  Milhar: {$ml}
OUT;