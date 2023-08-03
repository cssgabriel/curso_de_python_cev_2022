<?php

$value = (float) readline("Preço (R$): ");

$discountedValue = $value - ($value * 5 / 100);

echo number_format($discountedValue, 2, ",", ".");