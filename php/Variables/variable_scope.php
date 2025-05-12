<?php

$nome = "Richas";

function teste(){

	global $nome;
	echo $nome;

}

function teste2(){

	$nome = "Rafinha";
	echo $nome."no teste2";
}

teste();
teste2();


?>