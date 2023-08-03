<?php

$km = (float) readline("Quantos quilômetros tem a viagem que você pretende fazer? ");
echo $km <= 200 ? "O preço da viagem é R$ ". $km * 0.50 : "Desconto aplicado. O preço da viagem é R$ " . $km * 0.45;