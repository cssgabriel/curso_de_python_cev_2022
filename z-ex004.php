<?php

$variable = readline("Digite algo: ");

echo "is_array: " . (is_array($variable) ? "Sim" : "Não") . "\n"; // Encontra se a variável é um array :bool
echo "is_bool: " . (is_bool($variable) ? "Sim" : "Não") . "\n"; // Diz se a variável é booleana :bool
echo "is_callable: " . (is_callable($variable) ? "Sim" : "Não") . "\n"; // Verifique se um valor pode ser chamado como uma função do escopo atual :bool
echo "is_countable: " . (is_countable($variable) ? "Sim" : "Não") . "\n"; // Verifique se o conteúdo de uma variável é um valor contável
echo "is_double: " . (is_double($variable) ? "Sim" : "Não") . "\n"; // Alias de is_float()
echo "is_float: " . (is_float($variable) ? "Sim" : "Não") . "\n"; // Encontra se o tipo de uma variável é float
echo "is_int: " . (is_int($variable) ? "Sim" : "Não") . "\n"; // Descubra se o tipo de uma variável é inteiro
echo "is_integer: " . (is_integer($variable) ? "Sim" : "Não") . "\n"; // Alias ​​de is_int()
echo "is_iterable: " . (is_iterable($variable) ? "Sim" : "Não") . "\n"; // Verifique se o conteúdo de uma variável é um valor iterável
echo "is_long: " . (is_long($variable) ? "Sim" : "Não") . "\n"; // Alias ​​de is_int()
echo "is_null: " . (is_null($variable) ? "Sim" : "Não") . "\n"; // Encontra se uma variável é null
echo "is_numeric: " . (is_numeric($variable) ? "Sim" : "Não") . "\n"; // Encontra se uma variável é um número ou uma string numérica
echo "is_object: " . (is_object($variable) ? "Sim" : "Não") . "\n"; // Encontra se uma variável é um objeto
// echo "is_real: " . (is_real($variable) ? "Sim" : "Não") . "\n"; // Alias ​​de is_float() **DEPRECATED**
echo "is_resource: " . (is_resource($variable) ? "Sim" : "Não") . "\n"; // Encontra se uma variável é um recurso
echo "is_scalar: " . (is_scalar($variable) ? "Sim" : "Não") . "\n"; // Encontra se uma variável é um escalar
echo "is_string: " . (is_string($variable) ? "Sim" : "Não") . "\n"; // Descubra se o tipo de uma variável é string
echo "isset: " . (isset($variable) ? "Sim" : "Não") . "\n"; // Determina se uma variável é declarada e é diferente de null
