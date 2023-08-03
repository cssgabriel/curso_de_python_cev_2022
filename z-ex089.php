<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$students = [];

while (true) {
  $name = $read->read_str("Nome: ");
  $grade = [];
  foreach (range(1, 2) as $i) {
    $g = $read->read_float("Nota {$i}: ");
    $grade[] = $g;
  }
  $students[] = ["name" => $name, "grade" => $grade];
  $opt = $read->read_str("Quer continuar? [S/N] ", ["s", "n"]);
  if ($opt === "n")  break;
}

printTableStudents();

function printTableStudents() {
  global $students;
  echo line("-", 30);
  echo str_pad("Nº", 5, " ") . str_pad("NOME", 15, " ") . str_pad("MÉDIA", 10, " ") . PHP_EOL;
  echo line("-", 30);
  foreach ($students as $i => $student) {
    $average = array_sum($student['grade']) / 2;
    $average = str_pad(number_format($average, 2), 4);
    echo str_pad($i, 4, " ") . str_pad($student['name'], 15, " ") . str_pad($average, 10, " ") . PHP_EOL;
  }
  echo line();
}

while (true) {
  $opt = $read->read_int("Mostrar notas de qual aluno? \33[1;34m[999 interrompe]\33[m ");
  if ($opt == 999) break;
  else if (!isset($students[$opt])) echo "Código não encontrado. Tente novamente!\n";
  else printDataStudent($students[$opt]);
}

function printDataStudent($student) {
  echo $student['name'] . " obteve as seguintes notas: " . implode(", ", $student['grade']) . PHP_EOL;
}