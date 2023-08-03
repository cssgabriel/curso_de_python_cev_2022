<?php 
function arquivoExiste($name) {
  try {
    $a = fopen($name, "rt");
    fclose($a);
    return true;
  }
  catch (Error $e)  {
    return false;
  }
}

function criarArquivo($name) {
  try {
    $a = fopen($name, "wt+");
    fclose($a);
    echo "Arquivo criado com sucesso";
  }
  catch (Error $e) {
    echo "Houve um erro na criação do arquivo.";
  }
}

function lerArquivo($name) {
  try {
    $a = fopen($name, "r");
    echo "Pessoas Cadastradas\n";
    foreach (explode(",", file_get_contents($a)) as $line) {
      $data = str_replace("\n", "", $line);
      var_dump($data);
      // echo "{dado[0] {<21}{dado[1] {>3} anos.";
    }
  }
  catch (Error $e) {
    echo "Erro ao ler o arquivo.";
  }
  finally {
    fclose($a);
  }
}

function cadastrar($arq, $name="desconhecido", $idade = 0) {
  try {
    $a = fopen($arq, "at");
    try {
      fwrite($a,"{$name}, {$idade}\n");
      echo "{$name} adicionado!";
      fclose($a);
    }
    catch (Error $e) {
      echo "Houve um erro na hora de escrever os dados";
    }
  }
  catch (Error $e) {
    echo "houve um erro na criação do arquivo!";
  }
}