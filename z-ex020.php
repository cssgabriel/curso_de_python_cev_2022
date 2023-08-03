<?php

$alunos = [];
$qtdAlunos = (int) readline("Quantos alunos participarão do sorteio? ");

while(count($alunos) < $qtdAlunos) {
    $aluno = readline("Novo aluno: ");
    $alunos[] = $aluno;
}
echo str_repeat("-=", 13) . PHP_EOL;
echo "Sorteando a ordem da apresentação...\n";
echo str_repeat("-=", 13) . PHP_EOL;

echo "A nova ordem será: ";
shuffle($alunos);
foreach ($alunos as $aluno) {
    echo "$aluno ";
}

