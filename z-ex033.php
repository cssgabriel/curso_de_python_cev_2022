<?php

$numbers = [];
while (count($numbers) < 3) {
    $n = (int) readline("Digite um número: ");
    array_push($numbers, $n);
}

$higher;
$smaller;
foreach ($numbers as $i => $n) {
    if ($i === 0) {
        $higher = $n;
        $smaller = $n;
    }
    if ($n > $higher) $higher = $n;
    else if ($n < $smaller) $smaller = $n;
    else continue;
}
echo "Maior: {$higher} | Menor: {$smaller}\n";

// outra solução

$higher = max($numbers);
$smaller = min($numbers);
echo "Maior: {$higher} | Menor: {$smaller}\n";

