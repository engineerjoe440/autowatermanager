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
		<script type="text/javascript" src="/static/scripts.js"></script>
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
	<li class="imMnMnFirst imPage" data-link-paths="index,/">
<div class="label-wrapper">
<div class="label-inner-wrapper">
		<a class="label" href="index.html">
Overview		</a>
</div>
</div>
	</li><li class="imMnMnLast imPage" data-link-paths="settings">
<div class="label-wrapper">
<div class="label-inner-wrapper">
		<a class="label" href="settings.html">
Settings		</a>
</div>
</div>
	</li></ul></div>
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
	<li class="imMnMnFirst imPage" data-link-paths="index,/">
<div class="label-wrapper">
<div class="label-inner-wrapper">
		<a class="label" href="index.html">
Overview		</a>
</div>
</div>
	</li><li class="imMnMnLast imPage" data-link-paths="settings">
<div class="label-wrapper">
<div class="label-inner-wrapper">
		<a class="label" href="settings.html">
Settings		</a>
</div>
</div>
	</li></ul></div>
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
                                    <th colspan="2">Ambient Air Temperature: &nbsp &nbsp {{PAGE['temp']}}&#176F <br> Daylight: &nbsp {{PAGE['daylight']}} </th>
                                    <th> &nbsp </th>
                                    <th style="text-align:left;">Battery: &nbsp {{PAGE['batlevel']}} % <br>Voltage: {{PAGE['batvolt']}} VDC</th>
                                    <th> &nbsp </th>
                                    <th>Power Input OK: &nbsp &nbsp {{PAGE['activesrc']}} <br> Control Errors: &nbsp &nbsp {{PAGE['hosterrors']}}</th>
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
                                    <th style="vertical-align: bottom;">
                                        <form action='/set_light'>
                                            <p><input type="submit" value="Barn Light"> &nbsp &nbsp ({{PAGE['light']}})</p>
                                        </form>
                                    </th>
                                    <th> &nbsp </th>
                                    <th colspan="2" style="text-align:center"><img src="/static/{{PAGE['modelSta']}}.png" alt="Front Panel"><br/>Front Panel Indicator<br/>(Temperature Model Status)</th>
                                    <th> &nbsp </th>
                                    <td><img src="/static/{{PAGE['stockpole']}}.png" alt="Stall Status"><br/>Stock Pole - {{PAGE['stockpole']}} - {{PAGE['namstock']}}</td>
                                </tr>
                            </table>
                            
                            </br>
                            
                            <a href="/static/historiclog.csv" download="log.csv">
                              <p><img src="/static/log.png" alt="Download" width="50"></p>
                              <p>Log File</p>
                            </a>
                            
                            &nbsp; &nbsp; &nbsp;
                            
                            {{PAGE['oldlog']}}
                            
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
