<?php

$types = ["pedra", "papel", "tesoura"];
$computerChoice = $types[rand(0,2)];

echo <<<CHOICE
Vamos jogar JOKENPÔ!
Escolhas:
[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura

CHOICE;

$userChoice = intval(readline("Qual sua escolha? ") - 1);
if (isset($types[$userChoice])) $userChoice = $types[$userChoice];

$isWinner = [
  "pedra" => fn($v) => $v === "tesoura",
  "papel" => fn($v) => $v === "pedra",
  "tesoura" => fn($v) => $v === "papel",
];

echo str_repeat("-=", 13) . PHP_EOL;
if ($computerChoice !== $userChoice) {
  echo $isWinner[$computerChoice]($userChoice)
    ? "Você perdeu! Computador: {$computerChoice} | Você: {$userChoice}.\n"
    : "Você venceu! Computador: {$computerChoice} | Você: {$userChoice}.\n";
} else {
  echo "Empate! Computador: {$computerChoice} | Você: {$userChoice}.\n";
}
echo str_repeat("-=", 13);
