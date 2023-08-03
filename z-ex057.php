<?php

$genero = strtoupper(trim(readline("Sexo [F/M]: ")))[0];
while ($genero !== "F" && $genero !== "M") {
  $genero = strtoupper(trim(readline("Resposta inválida. Digite novamente! Sexo [F/M]: ")))[0];
}
echo "Ok. Resposta válida!";