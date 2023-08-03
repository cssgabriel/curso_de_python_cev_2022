<?php

$alunos = [];
$qtdAlunos = (int) readline("Quantos alunos participarão do sorteio? ");

while(count($alunos) < $qtdAlunos) {
    $aluno = readline("Novo aluno: ");
    $alunos[] = $aluno;
}
echo str_repeat("-=", 13) . PHP_EOL;
echo "Sorteando...\n";
echo str_repeat("-=", 13) . PHP_EOL;
$i = array_rand($alunos);
echo "O escolhido foi {$alunos[$i]}";

