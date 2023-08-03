<?php

$randomNumber = rand(0,5);
echo str_repeat("-=", 13) . PHP_EOL;
echo "Vou pensar em um número entre 0 e 5. Tente advinhar..." . PHP_EOL;
echo str_repeat("-=", 13) . PHP_EOL;
sleep(1);

$n = (int) readline("Em qual número estou pensando? ");
$palpites = 1;

while ($n !== $randomNumber) {
  if ($n > $randomNumber) $n = (int) readline("Pensei em um número MENOR. Tente novamente: ");
  else if ($n < $randomNumber) $n = (int) readline("Pensei em um número MAIOR. Tente novamente: "); 
  $palpites++;
}
echo "Parabéns, você acertou!\n";
echo "Você precisou de {$palpites} tentativas.\n";
echo "=-=-=-=Jogo encerrado!=-=-=-=";