<?php

$termo = intval(readline("Digite o primeiro termo: "));
$razao = intval(readline("Digite qual a razão: "));

$i = 1;
while ($i <= 10) {
    echo "{$termo} -> ";
    $termo += $razao;
    $i += 1;
}
echo "FIM!";