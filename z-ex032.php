<?php

$year = (int) readline("Ano: ");
if ($year == 0) {
    $year = date("Y");
}
if ($year % 4 == 0 && ($year % 100 != 0 || $year % 400 == 0)) {
    echo "O ano de {$year} É BISSEXTO";
} else {
    echo "O ano de {$year} NÃO É BISSEXTO";
}
