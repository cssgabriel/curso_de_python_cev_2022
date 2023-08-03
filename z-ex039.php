<?php

$birthYear = (int) readline("Informe sua data de nascimento: ");
$age = date("Y") - $birthYear;
$diff = abs($age - 18);
if ($age < 18) echo "Você irá se alistar daqui a {$diff} anos.";
else if ($age === 18) echo "Chegou a hora de se alistar";
else echo "Você já deveria ter se alistado há {$diff} anos.";