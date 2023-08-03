<?php

$temperatura = (float) readline("Qual temperatura em ºC você quer converter para ºF? ");
$conversao = ($temperatura * 9 / 5) + 32;

echo "A temperatura de {$temperatura}ºC corresponde a {$conversao}ºF";