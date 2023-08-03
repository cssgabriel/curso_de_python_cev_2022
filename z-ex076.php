<?php

require_once("z-line.php");
//require_once("z-Read.php");
//require_once("z-Numbers.php");

$list = [
  "Lápis", 2.50,
  "Borracha", 1.00,
  "Caderno", 19.90,
  "Folha sulfite", 12.00,
  "Apontador", 0.50,
  "Caixa com clipes", 1.20,
  "Régua", 0.70,
  "Estojo", 9.50
];

echo line();
echo center("Listagem de Preços");
echo line();

foreach ($list as $k => $v) {
  if (is_numeric($v)) $v = number_format($v, 2);
  echo $k % 2 !== 0 ? "R$" . str_pad($v, 7, " ", STR_PAD_LEFT) . PHP_EOL : str_pad("{$v}", 21, ".");
}
