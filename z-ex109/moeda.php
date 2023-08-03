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
}

    