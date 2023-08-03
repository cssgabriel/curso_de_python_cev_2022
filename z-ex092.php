<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$worker = [];

readDataWorker();
foreach ($worker as $k => $v) {
  echo ">>> {$k}: {$v}.\n";
}

function readDataWorker() {
  global $read;
  global $worker;
  $nome = $read->read_str("Digite seu nome: ");
  $worker['nome'] = $nome;
  $nascimento = $read->read_int("Ano de nascimento: ");
  $worker['nascimento'] = $nascimento;
  $worker['idade'] = date("Y") - $worker["nascimento"];
  $ctps = $read->read_int("Carteira de trabalho: [0 - Não Tem] ");
  $worker['ctps'] = $ctps ? $ctps: "Não possui";
  if (!is_int($ctps)) return;
  $contratacao = $read->read_int("Ano de contratação: ");
  $worker['contratacao'] = $contratacao;
  $salario = $read->read_float("Salário: ");
  $worker['salario'] = $salario;
  $worker["aposentadoria"] = $worker["idade"] + (($worker["contratacao"] + 35) - date("Y"));
}