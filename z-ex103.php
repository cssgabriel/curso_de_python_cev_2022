<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$nome = $read->read_str("Nome: ");
$gols = $read->read_int("Gols: ");

function ficha($nome = "<desconhecido>", $gols = 0) {
  echo "O jogador {$nome} fez {$gols} gols!";
}

ficha($nome, $gols);