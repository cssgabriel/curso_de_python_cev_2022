<?php

$lines = [];
$c = 1;
while ($c <= 3) {
  $line = (float) readline("Reta {$c}: ");
  array_push($lines, $line);
  $c++;
}

function check($l1, $l2, $l3) {
  return $l1 + $l2 > $l3;
}

if (check($lines[0], $lines[1], $lines[2]) && check($lines[0], $lines[2], $lines[1]) && check($lines[2], $lines[1], $lines[0])) {
  echo "Com essas três retas, é possível formar um triângulo";
} else {
  echo "Com essas três retas, não é possível formar um triângulo";
}
