<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$jogador = [];
cadastroJogador();
function cadastroJogador() {
  global $read;
  global $jogador;
  $nome = $read->read_str("Nome do jogador: ");
  $jogador['nome'] = $nome;
  $partidas = $read->read_int("Quantas partidas {$nome} jogou? ");
  foreach (range(1, $partidas) as $i) {
    $gol = $read->read_int("Quantos gols na partida {$i}: ");
    if (isset($jogador['gols'])) $jogador['gols'] = [...$jogador['gols'], $gol];
    else $jogador['gols'] = [$gol];
  }
}
echo line();
var_dump($jogador);
echo line();
foreach ($jogador as $k => $v) {
  echo "O campo {$k} tem valor: ";
  var_dump($v);
}
echo line();
foreach ($jogador['gols'] as $k => $v) {
  echo ">>> Na partida " . $k + 1 . ", fez {$v} gols.\n";
}