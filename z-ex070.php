<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$products = [];
$barato = [];

while (true) {
  $name = $read->read_str("Nome do produto: ");
  $price = $read->read_float("Preço: R$ ");
  array_push($products, ["name" => $name, "price" => $price]);

  if (count($products)) $barato = array($name, $price);
  else $barato = $barato < $price ? $barato : array($name, $price);
  echo line();
  $opt = $read->read_str("Quer continuar [S/N]? ", ["n","s"]);
  echo line();
  if ($opt === "n") break;
}

function sumProducts() {
  global $products;
  return array_sum(array_map(fn($p) => $p['price'], $products));
}

function totMil() {
  global $products;
  return count(array_filter($products, fn($p) => $p['price'] > 1000));
}

echo "O total da compra foi R$ " . sumProducts() . PHP_EOL;
echo "Temos " . totMil() . " produtos custando mais de R$ 1000\n";
echo "O produto mais barato foi {$barato[0]} que custa R$ {$barato[1]}";
