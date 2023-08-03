<?php

$randomNumber = rand(0,5);
echo str_repeat("-=", 13) . PHP_EOL;
echo "Vou pensar em um número entre 0 e 5. Tente advinhar..." . PHP_EOL;
echo str_repeat("-=", 13) . PHP_EOL;
sleep(1);
$n = (int) readline("Em qual número estou pensando? ");

echo $n === $randomNumber ? "Parabéns, você acertou\n" : "Não foi dessa vez. Pensei no número {$randomNumber}\n";
echo "Jogo encerrado!";