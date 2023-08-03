<?php

$numbers = [];
$strSeparator = fn($txt = "-=", $n = 15) => str_repeat($txt, $n) . PHP_EOL;
$opt = 4;

function readNumbers() {
  global $numbers;
  if (count($numbers)) $numbers = array_diff($numbers, $numbers);
  for ($i = 1; $i <= 2; $i++) {
    $n = (float) readline("{$i}º número: ");
    array_push($numbers, $n);
  }
}

function readOptions($invalid = false) {
  if ($invalid) echo "\033[0;31mResposta inválida! Tente novamente.\033[0m\n";
  echo "Qual opção você deseja?\n";
  echo <<<OPT
  [1] somar
  [2] multiplicar
  [3] mostrar maior
  [4] novos números
  [5] sair do programa

  OPT;
  $opt = (int) readline("Digite sua escolha: ");
  return $opt ? $opt : readOptions(true);
}

while ($opt !== 5) {
  if ($opt === 4) readNumbers();

  echo $strSeparator();
  $opt = readOptions();

  $res = match($opt) {
    1 => array_sum($numbers),
    2 => array_reduce($numbers, fn($acc, $n) => $acc * $n, 1),
    3 => max($numbers),
    4 => "Ok, digite logo abaixo quais números deseja:",
    5 => "Encerrando aplicação...",
    default => readOptions(true),
  };
  echo "\033[0;32mResposta => {$res}\033[0m\n";
}



