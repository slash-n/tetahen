<?php

ob_start();
passthru('/usr/bin/env python main.py');
$output = ob_get_clean(); 
echo $output;
?>
