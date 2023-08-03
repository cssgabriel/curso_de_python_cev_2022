<?php

$name = strtolower(trim(readline("Digite seu nome completo: ")));
echo "Seu nome possui Silva? ";
echo str_contains($name, "silva") ? "Sim, possui." : "Não possui";