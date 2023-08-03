<?php 
class Moeda {
  public function aumentar($n, $taxa, $formato = false){
    $res = $n + ($n * $taxa / 100);
    return $formato ? $this->moeda($res) : $res;
  }
  
  public function diminuir($n, $taxa, $formato = false){
    $res = $n - ($n * $taxa / 100);
    return $formato ? $this->moeda($res) : $res;
  }
  
  public function dobro($n, $formato = false){
    $res = $n * 2;
    return $formato ? $this->moeda($res) : $res;
  }
  
  public function metade($n, $formato = false){
    $res = $n / 2;
    return $formato ? $this->moeda($res) : $res;
  }

  public function moeda($preco, $moeda="R$") {
    return "{$moeda} " . number_format($preco, 2, ",", ".");
  }

  public function resumo($preco, $a, $d) {
    echo str_repeat("-", 30) . PHP_EOL;
    echo str_pad("RESUMO", 30, " ", STR_PAD_BOTH) . PHP_EOL;
    echo str_repeat("-", 30) . PHP_EOL;
    echo "Dobro" . PHP_EOL;
    echo "{$this->dobro($preco, true)}" . PHP_EOL;
    echo "Metade" . PHP_EOL;
    echo "{$this->metade($preco, true)}" . PHP_EOL;
    echo "Aumento" . PHP_EOL;
    echo "{$this->aumentar($preco, $a, true)}" . PHP_EOL;
    echo "Decréscimo" . PHP_EOL;
    echo "{$this->diminuir($preco, $d, true)}" . PHP_EOL;
  }
}
    