<?php
	$grade = 5;

	switch ($grade)
	{
		case 1:
			echo "$grade 학년 급식비 : 3만원"; break;
		case 2:
			echo "$grade 학년 급식비 : 3만 5천원"; break;
		case 3:
			echo "$grade 학년 급식비 : 4만원"; break;
		case 4:
			echo "$grade 학년 급식비 : 4만 오천원"; break;
		case 5:
			echo "$grade 학년 급식비 : 5만원"; break;
		case 6:
			echo "$grade 학년 급식비 : 5만 오천원"; break;
		default:
			echo "학년이 잘못 입력되었어요!"; break;
	}
?>