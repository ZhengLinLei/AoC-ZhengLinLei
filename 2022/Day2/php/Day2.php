<?php
// Read File ../input.txt

// Part 1 and Part 2


// ZhengLinLei

$gestor = @fopen("../input.txt", "r");
for(;$l=fgets($gestor);){
    $a=ord($l[0])-65;$b=ord($l[2])-88;
    $x+=$b+[4,7,1][($b+3-$a)%3];
    $y+=($a+[2,0,1][$b])%3+[1,4,7][$b];
}
echo"$x $y";