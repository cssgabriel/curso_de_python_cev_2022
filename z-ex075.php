<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();

$arr = [];
for ($i = 0; $i < 4; $i++) {
  $n = $read->read_int();
  array_push($arr, $n);
}
echo line();
echo "Você digitou os valores " . implode(", ", $arr) . PHP_EOL;
echo "O número 9 apareceu " . array_count_values($arr)[9] . " vezes" . PHP_EOL;
echo "O número 3 apareceu na ". array_search(3, $arr) + 1 . "º posição." . PHP_EOL;
echo "Os valores pares foram: " . implode(", ", array_filter($arr, fn($n) => $n % 2 === 0));