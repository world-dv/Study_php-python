<?php
	function sum($a, $b)
	{
		$sum = 0;
		while($a <= $b)
		{
			$sum += $a;
			$a++;
		}
		return $sum;
	}

	$from = 1;
	$to = 100;

	$total = sum($from, $to);
	echo ("$from 에서 $to 까지의 합 : $total");
?>