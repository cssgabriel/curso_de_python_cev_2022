<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$stack = [];
$par = [
  "(" => "(",
  ")" => ")"
];

$exp = $read->read_str("Digite uma expressão matemática: ");

for ($i = 0; $i < strlen($exp); $i++) {
  $p = $par[$exp[$i]] ?? null;
  if ($p === ")" && !isset($stack[0])) echo "Expressão inválida.";
  if ($p === "(") array_push($stack, $par[$exp[$i]]);
  else if ($p === ")") array_pop($stack);
  else continue;
}

echo count($stack) === 0 ? "Expressão válida!" : "Expressão inválida!";