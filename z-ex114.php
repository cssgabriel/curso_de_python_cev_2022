<?php

// require_once("z-line.php");
// require_once("z-Read.php");
// require_once("z-ex112/utilidades/moeda.php");
// require_once("z-Numbers.php");


$URL  =  'https://www.codexworld.com' ;
// $URL  =  'http://pudim.com.br' ;

if ( isSiteAvailible ( $URL )){ 
  echo  'O site está disponível.' ;     
} else { 
  echo  'Opa, o site não foi encontrado.';
}

function  isSiteAvailible ( $url ){ 
  // Verifica se um url válido foi fornecido 
  if(! filter_var ( $url ,  FILTER_VALIDATE_URL )){ 
      return  false ; 
  } 

  // Inicializar cURL 
  $curlInit = curl_init($url);
  
  // Definir opções 
  curl_setopt ( $curlInit , CURLOPT_CONNECTTIMEOUT , 10 ); 
  curl_setopt ( $curlInit , CURLOPT_HEADER , true ); 
  curl_setopt ($curlInit , CURLOPT_NOBODY , true ); 
  curl_setopt ( $curlInit , CURLOPT_RETURNTRANSFER , true ); 

  // Obter resposta 
  $response  =  curl_exec ( $curlInit ); 
  
  // Fechar uma sessão cURL 
  curl_close ( $curlInit ); 

  return  $response ? true : false ;
}