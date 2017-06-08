<?php
$string = $_GET["string"];
$func = $_GET["func"];
system("python site_tools.py " . $func . " " . $string);
?>