<?php

$age = (int) readline("Digite sua idade: ");
echo "Categoria: ";
if ($age <= 9) echo "MIRIM";
else if ($age <= 14) echo "INFANTIL";
else if ($age <= 19) echo "JUNIOR";
else if ($age <= 20) echo "SENIOR";
else echo "MASTER";

