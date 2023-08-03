<?php

$lines = [];
$c = 1;
while ($c <= 3) {
  $line = (float) readline("Reta {$c}: ");
  array_push($lines, $line);
  $c++;
}

function isTriangle($arr) {
  [$l1, $l2, $l3] = $arr;
  return $l1 + $l2 > $l3 && $l1 + $l3 > $l2 && $l2 + $l3 > $l1;
}

function typeTriangle($arr) {
  [$l1, $l2, $l3] = $arr;
  if ($l1 == $l2 && $l2 == $l3) return "EQUILÁTERO";
  else if ($l1 == $l2 && $l2 !== $l3) return "ISÓCELES";
  else return "ESCALENO";
}

if (isTriangle($lines)) {
  echo "Com essas três retas, é possível formar um triângulo\n";
  echo "Este é um triângulo: " . typeTriangle($lines);
} else {
  echo "Com essas três retas, não é possível formar um triângulo";
}
