<?php

$x = (float) readline("Cateto oposto: ");
$y = (float) readline("Cateto adjacente: ");
$hip = hypot($x, $y);
echo "A hipotenusa vale {$hip}!";