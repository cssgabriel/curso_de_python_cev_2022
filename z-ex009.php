<?php

$n = intval(readline("Digite um número: "));

for ($i = 1; $i <= 10 ; $i++) {
    $value = $n * $i;
    echo "{$n} X {$i} = {$value}\n";
}
