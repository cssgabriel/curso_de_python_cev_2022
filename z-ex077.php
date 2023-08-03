<?php

require_once("z-line.php");
//require_once("z-Read.php");
//require_once("z-Numbers.php");

$list = [
  "cobra",
  "macaco",
  "baleia",
  "golfinho",
  "galinha",
  "coala",
  "cachorro",
  "gato",
  "cavalo",
  "pato"
];

echo line();
echo center("Analisando palavras");
echo line();

foreach ($list as $word) {
  echo "Na palavra {$word}, temos: ";
  $len = strlen($word);
  for ($i = 0; $i < $len; $i++) {
    if (preg_match_all('/[aeiou]/i', $word[$i])) echo "{$word[$i]} ";
  }
  echo "\n";
}
