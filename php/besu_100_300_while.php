<?php
	$sum = 0;
	$i = 100;

	while($i <= 300)
	{
		if($i % 3 == 0)
		{
			$sum = $sum + $i;
		}
		$i++;
	}
	echo "100 ~ 300까지의 정수 중 3의 배수의 합 : $sum";
?>