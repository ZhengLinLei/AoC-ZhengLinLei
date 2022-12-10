<?php
// Part 1 and Part 2


// ZhengLinLei

define('CRLF',chr(0x0D).chr(0x0A));
define('LF',chr(0x0A));

$ops = explode(LF,trim(file_get_contents(__DIR__.'../input.txt'),LF));

$counter = 1;
$x = 1;

$command = '';
$value = 0;
$values = [];
$values[0]=1;

foreach ($ops as $idx => $op) {
	list($command,$value) = explode(' ',$op.' ');
	$value = intval($value);
	if ($command =='noop') { $values[$counter] = $x; $counter++;}
	if ($command =='addx') {
		$values[$counter] = $x;$counter++;
		$values[$counter] = $x;$counter++;
		$x += $value;
	}
}

$score = 20 * $values[20] + 60 * $values[60] + 100 * $values[100] + 140 * $values[140] + 180 * $values[180] + 220 * $values[220];

echo "Part 1:  $score\n";
$j=0;
for ($i=1;$i<count($values);$i++) {
	
	if (($values[$i]==$j) || ($values[$i]==$j-1) || ($values[$i]==$j+1)) {
		echo '█';
	} else {
		echo '.';
	}$j++;
	if ($j==40) { echo "\n"; $j=0; }
}

?>