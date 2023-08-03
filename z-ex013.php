<?php

$salary = (float) readline("Digite seu salário: ");
$newSalary = $salary + ($salary * 15 / 100);

echo "Parabéns, com o aumento de 15%, voce passará a ganhar " . number_format($newSalary, 2, ",", ".");