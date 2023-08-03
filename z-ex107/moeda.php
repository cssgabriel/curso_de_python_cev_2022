<?php 
class Moeda {
  public function aumentar($n, $taxa){
    $res = $n + ($n * $taxa / 100);
    return $res;
  }
  
  public function diminuir($n, $taxa){
    $res = $n - ($n * $taxa / 100);
    return $res;
  }
  
  public function dobro($n){
    $res = $n * 2;
    return $res;
  }
  
  public function metade($n){
    $res = $n / 2;
    return $res;
  }
}

    