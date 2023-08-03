<?php

require_once("z-line.php");
require_once("z-Read.php");

echo line();
echo "Sequência de Fibonacci\n";
echo line();

$read = new Read();
$n = $read->read_int("Quantos termos você quer mostrar? ");

$fib = [1, 1];
$i = 2;
while (count($fib) < $n) {
  if (isset($fib[$i - 2])) {
     $t = $fib[$i - 2] + $fib[$i - 1];
     array_push($fib, $t);
     $i++;
  }
}
echo implode(" -> ", $fib);
//print_r($fib);



