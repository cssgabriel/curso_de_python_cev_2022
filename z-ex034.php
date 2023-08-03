<?php

$salary = (float) readline("Qual seu salário atual? "); 
$tax = $salary > 1250 ? 10 : 15;
echo "Você ganhou um aumento de {$tax}%. ";
echo "Seu salário agora será de R$ " . $salary + ($salary * $tax / 100);

