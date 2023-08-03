<?php

function line($style = "-=", $n = 15) {
  if (!$style) $style = "-=";
  return str_repeat($style, $n) . PHP_EOL;
}

function center($txt, $n = 30) {
  return str_pad($txt, $n, " ", STR_PAD_BOTH) . PHP_EOL;
}

function textBox($txt, $style = "-") {
  if (!$style) $style = "-";
  $len = intval(strlen($txt) * 1.25);
  echo line($style, $len);
  echo center($txt, $len);
  echo line($style, $len);
}