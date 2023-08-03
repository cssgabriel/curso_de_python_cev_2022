<?php

require_once("z-line.php");
// require_once("z-Read.php");
require_once("z-Numbers.php");

// $read = new Read();
$numbers = new Numbers();
$assoc = [];

function notas($s = false, ...$n) {
  global $numbers;
  global $assoc;
  $numbers->setPushArr(...$n);
  $assoc['total'] = $numbers->getCount();
  $assoc['maior'] = $numbers->getHighNumber();
  $assoc['menor'] = $numbers->getSmallNumber();
  $assoc['media'] = number_format($numbers->getAverage(), 2);
  if ($s) {
    if ($assoc['media'] >= 7) {
      $assoc["situacao"] = "ÓTIMO";
    }
    else if ($assoc['media'] >= 5) {
      $assoc["situacao"] = "REGULAR";
    }
    else {
      $assoc["situacao"] = "RUIM";
    }
  }
  return $assoc;
}

print_r(notas(true, 10, 8, 6, 4));
print_r(notas(true, 6, 8, 6, 3));
print_r(notas(true, 6, 8, 6, 5, 9, 10));
print_r(notas(false, 4, 6, 1));