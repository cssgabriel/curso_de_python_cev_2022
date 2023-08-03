<?php
class Read {
  /*
  private string $txt;

  public function __construct($txt = "Digite um número: ") {
    $this->txt = $txt;
  }
  */
  public function read_int($txt = "Digite um número: ", $invalid = false) {
    if ($invalid) echo "\033[0;31mResposta inválida! Tente novamente.\033[0m\n";
    $int = readline($txt);
    if (is_numeric($int)) $int = intval($int);
    return is_int($int) ? $int : $this->read_int($txt,true); 
  }

  public function read_float($txt = "Digite um número: ", $invalid = false) {
    if ($invalid) echo "\033[0;31mResposta inválida! Tente novamente.\033[0m\n";
    $float = readline($txt);
    if (is_numeric($float)) $float = (float) $float;
    return is_float($float) ? $float : $this->read_float($txt, true);
  }

  public function read_str($txt = "Digite um texto: ", $invalid = []) {
    $str = strtolower(trim(readline($txt)));
    $res[] = $str;
    if ($invalid && !array_filter($invalid, fn($a) => in_array($a, $res))) {
      echo "\033[0;31mResposta inválida! Tente novamente.\033[0m\n";
      return $this->read_str($txt, $invalid);
    } else {
      return $str;
    }
  }
}
