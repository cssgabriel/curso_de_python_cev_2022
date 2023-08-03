<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$nasc = $read->read_int("Em que ano você nasceu? ");

function voto($nasc) {
  $idade = date("Y") - $nasc;
  echo "Com {$idade} anos, o voto é: ";
  switch ($idade) {
    case $idade >= 18 && $idade <= 65 :
      echo "Obrigatório";
      break;
    case $idade >= 16 || $idade >= 65:
      echo "Opcional";
      break;
    default:
      echo "Negado";
      break;
  } 
}

voto($nasc);