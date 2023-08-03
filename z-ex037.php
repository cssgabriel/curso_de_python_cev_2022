<?php

$num = (int) readline("Digite um número: ");
$opt = 0;

echo <<<OPT
Escolha uma opção para conversão:
  [1] - Binário
  [2] - Octal
  [3] - Hexadecimal

OPT;

while ($opt !== "1" && $opt !== "2" && $opt !== "3") {
  $opt = readline("Sua opção: ");
}

switch ($opt) {
  case 1:
    echo "Convertendo para binário: " . base_convert($num, 10, 2);
    break;
  case 2:
    echo "Convertendo para octal: " . base_convert($num, 10, 8);
    break;
  case 3:
    echo "Convertendo para hexadecimal: " . base_convert($num, 10, 16);
    break;
  default:
    break;
}