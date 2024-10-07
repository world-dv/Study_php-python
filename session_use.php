<?php
	session_start();

	$user_id = $_SESSION["userid"];
	$user_name = $_SESSION["username"];
?>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
	<h3>
		등록된 세션의 사용
	</h3>
	<ul>
		<li>등록된 세션(userid) : <?= $user_id?></li>
		<li>등록된 세션(username) : <?=$user_name?></li>
	</ul>
</body>
</html>