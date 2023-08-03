<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$jogadores = [];

while (true) {
  cadastroJogador();
  $opt = $read->read_str("Quer continuar? [s/n] ", ["s", "n"]);
  echo line();
  if ($opt === "n") break;
}

mostrarTaelaJogadores();

while (true) {
  $opt = $read->read_int("Mostrar dados de qual jogador? \33[1;34m[999 interrompe]\33[m ");
  if ($opt === 999) break;
  else if (!isset($jogadores[$opt])) echo "Opção inválida. Digite um número entre 0 e " . count($jogadores) - 1 . PHP_EOL;
  else mostrarDadosJogador($jogadores[$opt]);
  echo line();
}

function mostrarTaelaJogadores() {
  global $jogadores;
  echo line("-", 40);
  echo str_pad("Cod.", 5, " ") . str_pad("NOME", 10, " ") . str_pad("GOLS", 15, " ") . str_pad("TOTAL", 10, " ") . PHP_EOL;
  echo line("-", 40);
  foreach ($jogadores as $i => $jogador) {
    $totGols = array_sum($jogador["gols"]);
    echo str_pad($i, 5, " ") . str_pad($jogador["nome"], 10, " ") . str_pad(implode(", ", $jogador["gols"]), 15, " ") . str_pad("{$totGols}", 10, " ") . PHP_EOL;
  }
  echo line(null, 20);
}

function cadastroJogador() {
  global $read;
  global $jogadores;
  $nome = $read->read_str("Nome do jogador: ");
  $jogador['nome'] = $nome;
  $partidas = $read->read_int("Quantas partidas {$nome} jogou? ");
  foreach (range(1, $partidas) as $i) {
    $gol = $read->read_int("Quantos gols na partida {$i}: ");
    if (isset($jogador['gols'])) $jogador['gols'] = [...$jogador['gols'], $gol];
    else $jogador['gols'] = [$gol];
  }
  $jogadores[] = $jogador;
}

function mostrarDadosJogador($jogador) {
  echo "O jogador {$jogador['nome']} jogou " . count($jogador['gols']) . " partidas.\n";
  foreach ($jogador['gols'] as $k => $v) {
    echo ">>> Na partida " . $k + 1 . ", fez {$v} gols.\n";
  }
  echo "Total de " . array_sum($jogador["gols"]) . " gols.\n";
}
