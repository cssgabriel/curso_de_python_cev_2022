<?php

$n = (float) readline("Quanto dinheiro você tem na carteira (em R$): ");
$dolares = $n / 4.73;
echo "Com R$ {$n} você pode comprar US$ {$dolares}";