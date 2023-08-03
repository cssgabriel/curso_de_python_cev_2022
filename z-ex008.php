<?php

$metros = (float) readline("Digite um número (em metros): ");
$km = $metros / 1000;
$hm = $metros / 100;
$dam = $metros / 10;
$dm = $metros * 10;
$cm = $metros * 100;
$mm = $metros * 1000;

echo "{$metros} Metros equivale a: \n";
echo "{$km} Quilômetros\n";
echo "{$hm} Hectômetros\n";
echo "{$dam} Decâmetros\n";
echo "{$dm} Decímetros\n";
echo "{$cm} Centímetros\n";
echo "{$mm} Milímetros\n";