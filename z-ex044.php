<?php

$price = (float) readline("Preço das compras (R$): ");
echo <<<PAYMENT
FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão

PAYMENT;
$opt = fn($msg = "Sua opção: ") => (int) readline($msg);

function installments() {
  $i = (int) readline("Quantas parcelas? ");
  return "{$i}x de R$ {} com juros de 20%. TOTAL: R$ {}";
};

$value = null;

while (!$value) {

  $value = match($opt()) {
    1 => [$price * 0.9, "Com 10% de desconto, você irá pagar R$ {}"],
    2 => [$price * 0.95, "Com 5% de desconto, você irá pagar R$ {}"],
    3 => [$price, "2x de R$ {} sem juros: R$ {}"],
    4 => [$price * 1.2, installments()],
    default => null,
  };

};

$t = implode($value[0], explode("{}", $value[1]));

echo "$t";