<?php

$n = intval(readline("Qual tabuada você deseja? "));

for ($i = 1; $i <= 10 ; $i++) {
    $value = $n * $i;
    echo "{$n} X {$i} = {$value}\n";
}
