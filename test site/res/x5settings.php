<?php

/*
|-------------------------------
|	GENERAL SETTINGS
|-------------------------------
*/

$imSettings['general'] = array(
	'url' => 'http://dummy.com/',
	'homepage_url' => 'http://dummy.com/index.html',
	'icon' => 'http://dummy.com/favImage.png',
	'version' => '14.0.6.2',
	'sitename' => 'HorseTest',
	'public_folder' => '',
	'salt' => 't24aafojhtdwzo0n4x1flip57xcybrmwz0tg695z',
);


$imSettings['admin'] = array(
	'icon' => 'admin/images/logo_hv06rbpu.png',
	'theme' => 'orange'
);
ImTopic::$captcha_code = "		<div class=\"x5captcha-wrap\">
			<label>Check word:</label><br />
			<input type=\"text\" class=\"imCpt\" name=\"imCpt\" maxlength=\"5\" />
		</div>
";

// End of file x5settings.php