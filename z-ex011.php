<?php

$height = (float) readline("Digite a altura a parede: ");
$width = (float) readline("Digite a largura a parede: ");

$area = $height * $width;
$paint = $area / 2;
echo "Sua parede possui {$area}m². Para pintar esta área você precisará de {$paint} litros de tinta.";
