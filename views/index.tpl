<!DOCTYPE html><!-- HTML5 -->
<html lang="en-GB" dir="ltr">
	<head>
		<title>AutoWaterManager</title>
		<meta charset="utf-8" />
		<meta name="author" content="JoeStanley" />
		<meta name="viewport" content="width=1150" />
		
		<link rel="stylesheet" type="text/css" href="/static/reset.css"/>
		<link rel="stylesheet" type="text/css" href="/static/style.css"/>
		<link rel="stylesheet" type="text/css" href="/static/template.css"/>
		<link rel="stylesheet" type="text/css" href="/static/index.css"/>
		<script type="text/javascript">
			window.onload = function(){ checkBrowserCompatibility('Your browser does not support the features necessary to display this website.','Your browser may not support the features necessary to display this website.','[1]Update your browser[/1] or [2]continue without updating[/2].','http://outdatedbrowser.com/'); };
			x5engine.utils.currentPagePath = 'index.html';
			x5engine.boot.push(function () { x5engine.imPageToTop.initializeButton({}); });
		</script>
		<link rel="icon" href="/static/favicon.ico" type="image/vnd.microsoft.icon" />
	</head>
	<body>
		<div id="imPageExtContainer">
			<div id="imPageIntContainer">
				<div id="imHeaderBg"></div>
				<div id="imFooterBg"></div>
				<div id="imPage">
					<div id="imHeader">
						<h1 class="imHidden">AutoWaterManager</h1>
						<div id="imHeaderObjects"><div id="imHeader_imObjectImage_04_wrapper" class="template-object-wrapper"><div id="imHeader_imCell_4" class="" > <div id="imHeader_imCellStyleGraphics_4"></div><div id="imHeader_imCellStyle_4" ><img id="imHeader_imObjectImage_04" src="/static/horselogo_txp_neg.png" title="" alt="" /></div></div></div><div id="imHeader_imObjectTitle_03_wrapper" class="template-object-wrapper"><div id="imHeader_imCell_3" class="" > <div id="imHeader_imCellStyleGraphics_3"></div><div id="imHeader_imCellStyle_3" ><div id="imHeader_imObjectTitle_03"><span id ="imHeader_imObjectTitle_03_text" >AutoWaterManager</span > </div></div></div></div><div id="imHeader_imMenuObject_01_wrapper" class="template-object-wrapper"><div id="imHeader_imCell_1" class="" > <div id="imHeader_imCellStyleGraphics_1"></div><div id="imHeader_imCellStyle_1" ><div id="imHeader_imMenuObject_01"><div class="hamburger-menu-background-container hamburger-component">
	<div class="hamburger-menu-background menu-mobile menu-mobile-animated hidden">
		<div class="hamburger-menu-close-button"><span>&times;</span></div>
	</div>
</div>
<ul class="menu-mobile-animated hidden">
	<li class="imMnMnFirst imPage" data-link-paths="/index.html,/">
<div class="label-wrapper">
<div class="label-inner-wrapper">
		<a class="label" href="index.html">
Overview		</a>
</div>
</div>
	</li><li class="imMnMnLast imPage" data-link-paths="/settings.html">
<div class="label-wrapper">
<div class="label-inner-wrapper">
		<a class="label" href="settings.html">
Settings		</a>
</div>
</div>
	</li></ul></div><script type="text/javascript">
x5engine.boot.push(function(){x5engine.initMenu('imHeader_imMenuObject_01',1000)});
$(function () {$('#imHeader_imMenuObject_01 ul li').each(function () {    var $this = $(this), timeout = 0, subtimeout = 0, width = 'none', height = 'none';        var submenu = $this.children('ul').add($this.find('.multiple-column > ul'));    $this.on('mouseenter', function () {        if($(this).parents('#imHeader_imMenuObject_01-menu-opened').length > 0) return;         clearTimeout(timeout);        clearTimeout(subtimeout);        $this.children('.multiple-column').show(0);        submenu.stop(false, false);        if (width == 'none') {             width = submenu.width();        }        if (height == 'none') {            height = submenu.height();            submenu.css({ overflow : 'hidden', height: 0});        }        setTimeout(function () {         submenu.css({ overflow : 'hidden'}).fadeIn(1).animate({ height: height }, 300, null, function() {$(this).css('overflow', 'visible'); });        }, 250);    }).on('mouseleave', function () {        if($(this).parents('#imHeader_imMenuObject_01-menu-opened').length > 0) return;         timeout = setTimeout(function () {         submenu.stop(false, false);            submenu.css('overflow', 'hidden').animate({ height: 0 }, 300, null, function() {$(this).fadeOut(0); });            subtimeout = setTimeout(function () { $this.children('.multiple-column').hide(0); }, 300);        }, 250);    });});});

</script>
</div></div></div></div>
					</div>
					<div id="imStickyBarContainer">
						<div id="imStickyBarGraphics"></div>
						<div id="imStickyBar">
							<div id="imStickyBarObjects"><div id="imStickyBar_imObjectTitle_02_wrapper" class="template-object-wrapper"><div id="imStickyBar_imCell_2" class="" > <div id="imStickyBar_imCellStyleGraphics_2"></div><div id="imStickyBar_imCellStyle_2" ><div id="imStickyBar_imObjectTitle_02"><span id ="imStickyBar_imObjectTitle_02_text" >Title</span > </div></div></div></div><div id="imStickyBar_imMenuObject_03_wrapper" class="template-object-wrapper"><div id="imStickyBar_imCell_3" class="" > <div id="imStickyBar_imCellStyleGraphics_3"></div><div id="imStickyBar_imCellStyle_3" ><div id="imStickyBar_imMenuObject_03"><div class="hamburger-menu-background-container hamburger-component">
	<div class="hamburger-menu-background menu-mobile menu-mobile-animated hidden">
		<div class="hamburger-menu-close-button"><span>&times;</span></div>
	</div>
</div>
<ul class="menu-mobile-animated hidden">
	<li class="imMnMnFirst imPage" data-link-paths="/index.html,/">
<div class="label-wrapper">
<div class="label-inner-wrapper">
		<a class="label" href="index.html">
Overview		</a>
</div>
</div>
	</li><li class="imMnMnLast imPage" data-link-paths="/settings.html">
<div class="label-wrapper">
<div class="label-inner-wrapper">
		<a class="label" href="settings.html">
Settings		</a>
</div>
</div>
	</li></ul></div><script type="text/javascript">
x5engine.boot.push(function(){x5engine.initMenu('imStickyBar_imMenuObject_03',1000)});
$(function () {$('#imStickyBar_imMenuObject_03 ul li').each(function () {    var $this = $(this), timeout = 0, subtimeout = 0, width = 'none', height = 'none';        var submenu = $this.children('ul').add($this.find('.multiple-column > ul'));    $this.on('mouseenter', function () {        if($(this).parents('#imStickyBar_imMenuObject_03-menu-opened').length > 0) return;         clearTimeout(timeout);        clearTimeout(subtimeout);        $this.children('.multiple-column').show(0);        submenu.stop(false, false);        if (width == 'none') {             width = submenu.width();        }        if (height == 'none') {            height = submenu.height();            submenu.css({ overflow : 'hidden', height: 0});        }        setTimeout(function () {         submenu.css({ overflow : 'hidden'}).fadeIn(1).animate({ height: height }, 300, null, function() {$(this).css('overflow', 'visible'); });        }, 250);    }).on('mouseleave', function () {        if($(this).parents('#imStickyBar_imMenuObject_03-menu-opened').length > 0) return;         timeout = setTimeout(function () {         submenu.stop(false, false);            submenu.css('overflow', 'hidden').animate({ height: 0 }, 300, null, function() {$(this).fadeOut(0); });            subtimeout = setTimeout(function () { $this.children('.multiple-column').hide(0); }, 300);        }, 250);    });});});

</script>
</div></div></div></div>
						</div>
					</div>
					<a class="imHidden" href="#imGoToCont" title="Skip the main menu">Go to content</a>
					<div id="imContentContainer">
						<div id="imContentGraphics"></div>
						<div id="imContent">
							<a id="imGoToCont"></a>
				<div id="imPageRow_1" class="imPageRow">
				
				<div id="imPageRowContent_1" class="imContentDataContainer">
				<div id="imCell_1" class="" > <div id="imCellStyleGraphics_1"></div><div id="imCellStyle_1" ><div id="imTextObject_01">
					<div class="text-tab-content"  id="imTextObject_01_tab0" style="">
						<div class="text-inner">
							
                            <table style="width:100%">
                                <tr>
                                    <th colspan="2">Current Outside Air Temperature:</th>
                                    <th style="text-align:left;">&nbsp {{PAGE['temp']}}ºF</th>
                                    <th>System Battery:</th>
                                    <th style="text-align:left;">&nbsp {{PAGE['bat']}}</th>
                                </tr>
                                <tr>
                                    <th colspan="6"> &nbsp &nbsp &nbsp </th>
                                </tr>
                                <tr>
                                    <td align="right"><img src="/static/{{PAGE['pole1a']}}.png" alt="Stall Status"><br/>Stall 1A - {{PAGE['pole1a']}} - {{PAGE['nam1a']}}</td>
                                    <td align="left" ><img src="/static/{{PAGE['pole1b']}}.png" alt="Stall Status"><br/>Stall 1B - {{PAGE['pole1b']}} - {{PAGE['nam1b']}}</td>
                                    <td align="right"><img src="/static/{{PAGE['pole2a']}}.png" alt="Stall Status"><br/>Stall 2A - {{PAGE['pole2a']}} - {{PAGE['nam2a']}}</td>
                                    <td align="left" ><img src="/static/{{PAGE['pole2b']}}.png" alt="Stall Status"><br/>Stall 2B - {{PAGE['pole2b']}} - {{PAGE['nam2b']}}</td>
                                    <td align="right"><img src="/static/{{PAGE['pole3a']}}.png" alt="Stall Status"><br/>Stall 3A - {{PAGE['pole3a']}} - {{PAGE['nam3a']}}</td>
                                    <td align="left" ><img src="/static/{{PAGE['pole3b']}}.png" alt="Stall Status"><br/>Stall 3B - {{PAGE['pole3b']}} - {{PAGE['nam3b']}}</td>
                                </tr>
                                <tr>
                                    <th colspan="6"> &nbsp &nbsp &nbsp </th>
                                </tr>
                                <tr>
                                    <td align="right"><img src="/static/{{PAGE['pole4a']}}.png" alt="Stall Status"><br/>Stall 4A - {{PAGE['pole4a']}} - {{PAGE['nam4a']}}</td>
                                    <td align="left" ><img src="/static/{{PAGE['pole4b']}}.png" alt="Stall Status"><br/>Stall 4B - {{PAGE['pole4b']}} - {{PAGE['nam4b']}}</td>
                                    <td align="right"><img src="/static/{{PAGE['pole5a']}}.png" alt="Stall Status"><br/>Stall 5A - {{PAGE['pole5a']}} - {{PAGE['nam5a']}}</td>
                                    <td align="left" ><img src="/static/{{PAGE['pole5b']}}.png" alt="Stall Status"><br/>Stall 5B - {{PAGE['pole5b']}} - {{PAGE['nam5b']}}</td>
                                    <td align="right"><img src="/static/{{PAGE['pole6a']}}.png" alt="Stall Status"><br/>Stall 6A - {{PAGE['pole6a']}} - {{PAGE['nam6a']}}</td>
                                    <td align="left" ><img src="/static/{{PAGE['pole6b']}}.png" alt="Stall Status"><br/>Stall 6B - {{PAGE['pole6b']}} - {{PAGE['nam6b']}}</td>
                                </tr>
                                <tr>
                                    <th colspan="6"> &nbsp &nbsp &nbsp </th>
                                </tr>
                                <tr>
                                    <th colspan="6"> &nbsp &nbsp &nbsp </th>
                                </tr>
                                <tr>
                                    <th colspan="6"> &nbsp &nbsp &nbsp </th>
                                </tr>
                                <tr>
                                    <th colspan="5"> &nbsp </th>
                                    <td><img src="/static/{{PAGE['stockpole']}}.png" alt="Stall Status"><br/>Stock Pole - {{PAGE['stockpole']}} - {{PAGE['namstock']}}</td>
                                </tr>
                            </table>
                            
                            </br>
                            </br>
                            </br>
                            
                            <form action='/set_light'>
                                <input type="submit" value="Barn Light &nbsp &nbsp ({{PAGE['light']}})">
                            </form>
                            
						</div>
					</div>
				
				</div>
				</div></div></div>
				</div>
				
							<div class="imClear"></div>
						</div>
					</div>
					<div id="imFooter">
						<div id="imFooterObjects"><div id="imFooter_imObjectTitle_04_wrapper" class="template-object-wrapper"><div id="imFooter_imCell_4" class="" > <div id="imFooter_imCellStyleGraphics_4"></div><div id="imFooter_imCellStyle_4" ><div id="imFooter_imObjectTitle_04"><span id ="imFooter_imObjectTitle_04_text" >AutoWaterManager</span > </div></div></div></div><div id="imFooter_imTextObject_02_wrapper" class="template-object-wrapper"><div id="imFooter_imCell_2" class="" > <div id="imFooter_imCellStyleGraphics_2"></div><div id="imFooter_imCellStyle_2" ><div id="imFooter_imTextObject_02">
	<div class="text-tab-content"  id="imFooter_imTextObject_02_tab0" style="">
		<div class="text-inner">
			<div><div style="text-align: center;"><span class="fs12 cf1">Automatic Water Heater Control System</span></div></div><div style="text-align: center;"><span class="fs12 cf1">by Stanley Solutions</span></div>
		</div>
	</div>

</div>
</div></div></div></div>
					</div>
				</div>
				<span class="imHidden"><a href="#imGoToCont" title="Read this page again">Back to content</a></span>
			</div>
		</div>
		
		<noscript class="imNoScript"><div class="alert alert-red">To use this website you must enable JavaScript.</div></noscript>
	</body>
</html>
