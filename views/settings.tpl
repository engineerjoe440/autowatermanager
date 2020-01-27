<!DOCTYPE html><!-- HTML5 -->
<html lang="en-GB" dir="ltr">
	<head>
    <style>
/* The switch - the box around the slider */
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
    </style>
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
							<form action="/autowater_update" method="get">
                            <table style="width:100%">
                                <tr>
                                    <th>Stall Index</th>
                                    <th>In/Out of Service</th>
                                    <th>Manual Turn On</th>
                                    <th>Manual Turn Off</th>
                                    <th>Heater Power</th>
                                    <th>Trough Size</th>
                                    <th>Animal Name</th>
                                </tr>
                                <tr>
                                    <th colspan="5"> &nbsp &nbsp &nbsp </th>
                                </tr>
                                <tr>
                                    <th>Pole 1 - Side A</th>
                                    <td>
                                        <label class="switch">
                                          <input type="checkbox" name="pole1aservice" value="checked" {{PAGE['p1acheck']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </td>
                                    <td><input type="submit" name="pole1aon" value="Turn On"></td>
                                    <td><input type="submit" name="pole1aoff" value="Turn Off"></td>
                                    <td><input type="text" maxlength="4" name="power1a" value="{{PAGE['1apower']}}" size="4">&nbsp Watts</td>
                                    <td><input type="text" maxlength="4" name="size1a" value="{{PAGE['size1a']}}" size="4">&nbsp Gallons</td>
                                    <td><input type="text" name="animal1a" value="{{PAGE['animal1a']}}"></td>
                                </tr>
                                <tr>
                                    <th>Pole 1 - Side B</th>
                                    <td>
                                        <label class="switch">
                                          <input type="checkbox" name="pole1bservice" value="checked" {{PAGE['p1bcheck']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </td>
                                    <td><input type="submit" name="pole1bon" value="Turn On"></td>
                                    <td><input type="submit" name="pole1boff" value="Turn Off"></td>
                                    <td><input type="text" maxlength="4" name="power1b" value="{{PAGE['1bpower']}}" size="4">&nbsp Watts</td>
                                    <td><input type="text" maxlength="4" name="size1b" value="{{PAGE['size1b']}}" size="4">&nbsp Gallons</td>
                                    <td><input type="text" name="animal1b" value="{{PAGE['animal1b']}}"></td>
                                </tr>
                                <tr>
                                    <th>Pole 2 - Side A</th>
                                    <td>
                                        <label class="switch">
                                          <input type="checkbox" name="pole2aservice" value="checked" {{PAGE['p2acheck']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </td>
                                    <td><input type="submit" name="pole2aon" value="Turn On"></td>
                                    <td><input type="submit" name="pole2aoff" value="Turn Off"></td>
                                    <td><input type="text" maxlength="4" name="power2a" value="{{PAGE['2apower']}}" size="4">&nbsp Watts</td>
                                    <td><input type="text" maxlength="4" name="size2a" value="{{PAGE['size2a']}}" size="4">&nbsp Gallons</td>
                                    <td><input type="text" name="animal2a" value="{{PAGE['animal2a']}}"></td>
                                </tr>
                                <tr>
                                    <th>Pole 2 - Side B</th>
                                    <td>
                                        <label class="switch">
                                          <input type="checkbox" name="pole2bservice" value="checked" {{PAGE['p2bcheck']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </td>
                                    <td><input type="submit" name="pole2bon" value="Turn On"></td>
                                    <td><input type="submit" name="pole2boff" value="Turn Off"></td>
                                    <td><input type="text" maxlength="4" name="power2b" value="{{PAGE['2bpower']}}" size="4">&nbsp Watts</td>
                                    <td><input type="text" maxlength="4" name="size2b" value="{{PAGE['size2b']}}" size="4">&nbsp Gallons</td>
                                    <td><input type="text" name="animal2b" value="{{PAGE['animal2b']}}"></td>
                                </tr>
                                <tr>
                                    <th>Pole 3 - Side A</th>
                                    <td>
                                        <label class="switch">
                                          <input type="checkbox" name="pole3aservice" value="checked" {{PAGE['p3acheck']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </td>
                                    <td><input type="submit" name="pole3aon" value="Turn On"></td>
                                    <td><input type="submit" name="pole3aoff" value="Turn Off"></td>
                                    <td><input type="text" maxlength="4" name="power3a" value="{{PAGE['3apower']}}" size="4">&nbsp Watts</td>
                                    <td><input type="text" maxlength="4" name="size3a" value="{{PAGE['size3a']}}" size="4">&nbsp Gallons</td>
                                    <td><input type="text" name="animal3a" value="{{PAGE['animal3a']}}"></td>
                                </tr>
                                <tr>
                                    <th>Pole 3 - Side B</th>
                                    <td>
                                        <label class="switch">
                                          <input type="checkbox" name="pole3bservice" value="checked" {{PAGE['p3bcheck']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </td>
                                    <td><input type="submit" name="pole3bon" value="Turn On"></td>
                                    <td><input type="submit" name="pole3boff" value="Turn Off"></td>
                                    <td><input type="text" maxlength="4" name="power3b" value="{{PAGE['3bpower']}}" size="4">&nbsp Watts</td>
                                    <td><input type="text" maxlength="4" name="size3b" value="{{PAGE['size3b']}}" size="4">&nbsp Gallons</td>
                                    <td><input type="text" name="animal3b" value="{{PAGE['animal3b']}}"></td>
                                </tr>
                                <tr>
                                    <th>Pole 4 - Side A</th>
                                    <td>
                                        <label class="switch">
                                          <input type="checkbox" name="pole4aservice" value="checked" {{PAGE['p4acheck']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </td>
                                    <td><input type="submit" name="pole4aon" value="Turn On"></td>
                                    <td><input type="submit" name="pole4aoff" value="Turn Off"></td>
                                    <td><input type="text" maxlength="4" name="power4a" value="{{PAGE['4apower']}}" size="4">&nbsp Watts</td>
                                    <td><input type="text" maxlength="4" name="size4a" value="{{PAGE['size4a']}}" size="4">&nbsp Gallons</td>
                                    <td><input type="text" name="animal4a" value="{{PAGE['animal4a']}}"></td>
                                </tr>
                                <tr>
                                    <th>Pole 4 - Side B</th>
                                    <td>
                                        <label class="switch">
                                          <input type="checkbox" name="pole4bservice" value="checked" {{PAGE['p4bcheck']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </td>
                                    <td><input type="submit" name="pole4bon" value="Turn On"></td>
                                    <td><input type="submit" name="pole4boff" value="Turn Off"></td>
                                    <td><input type="text" maxlength="4" name="power4b" value="{{PAGE['4bpower']}}" size="4">&nbsp Watts</td>
                                    <td><input type="text" maxlength="4" name="size4b" value="{{PAGE['size4b']}}" size="4">&nbsp Gallons</td>
                                    <td><input type="text" name="animal4b" value="{{PAGE['animal4b']}}"></td>
                                </tr>
                                <tr>
                                    <th>Pole 5 - Side A</th>
                                    <td>
                                        <label class="switch">
                                          <input type="checkbox" name="pole5aservice" value="checked" {{PAGE['p5acheck']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </td>
                                    <td><input type="submit" name="pole5aon" value="Turn On"></td>
                                    <td><input type="submit" name="pole5aoff" value="Turn Off"></td>
                                    <td><input type="text" maxlength="4" name="power5a" value="{{PAGE['5apower']}}" size="4">&nbsp Watts</td>
                                    <td><input type="text" maxlength="4" name="size5a" value="{{PAGE['size5a']}}" size="4">&nbsp Gallons</td>
                                    <td><input type="text" name="animal5a" value="{{PAGE['animal5a']}}"></td>
                                </tr>
                                <tr>
                                    <th>Pole 5 - Side B</th>
                                    <td>
                                        <label class="switch">
                                          <input type="checkbox" name="pole5bservice" value="checked" {{PAGE['p5bcheck']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </td>
                                    <td><input type="submit" name="pole5bon" value="Turn On"></td>
                                    <td><input type="submit" name="pole5boff" value="Turn Off"></td>
                                    <td><input type="text" maxlength="4" name="power5b" value="{{PAGE['5bpower']}}" size="4">&nbsp Watts</td>
                                    <td><input type="text" maxlength="4" name="size5b" value="{{PAGE['size5b']}}" size="4">&nbsp Gallons</td>
                                    <td><input type="text" name="animal5b" value="{{PAGE['animal5b']}}"></td>
                                </tr>
                                <tr>
                                    <th>Pole 6 - Side A</th>
                                    <td>
                                        <label class="switch">
                                          <input type="checkbox" name="pole6aservice" value="checked" {{PAGE['p6acheck']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </td>
                                    <td><input type="submit" name="pole6aon" value="Turn On"></td>
                                    <td><input type="submit" name="pole6aoff" value="Turn Off"></td>
                                    <td><input type="text" maxlength="4" name="power6a" value="{{PAGE['6apower']}}" size="4">&nbsp Watts</td>
                                    <td><input type="text" maxlength="4" name="size6a" value="{{PAGE['size6a']}}" size="4">&nbsp Gallons</td>
                                    <td><input type="text" name="animal6a" value="{{PAGE['animal6a']}}"></td>
                                </tr>
                                <tr>
                                    <th>Pole 6 - Side B</th>
                                    <td>
                                        <label class="switch">
                                          <input type="checkbox" name="pole6bservice" value="checked" {{PAGE['p6bcheck']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </td>
                                    <td><input type="submit" name="pole6bon" value="Turn On"></td>
                                    <td><input type="submit" name="pole6boff" value="Turn Off"></td>
                                    <td><input type="text" maxlength="4" name="power6b" value="{{PAGE['6bpower']}}" size="4">&nbsp Watts</td>
                                    <td><input type="text" maxlength="4" name="size6b" value="{{PAGE['size6b']}}" size="4">&nbsp Gallons</td>
                                    <td><input type="text" name="animal6b" value="{{PAGE['animal6b']}}"></td>
                                </tr>
                                <tr>
                                    <th colspan="5"> &nbsp &nbsp &nbsp </th>
                                </tr>
                                <tr>
                                    <th>Stock Pole</th>
                                    <td>
                                        <label class="switch">
                                          <input type="checkbox" name="stockpoleservice" value="checked"  {{PAGE['stockcheck']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </td>
                                    <td><input type="submit" name="stockpoleon" value="Turn On"></td>
                                    <td><input type="submit" name="stockpoleoff" value="Turn Off"></td>
                                    <td><input type="text" maxlength="4" name="stockpolepower" value="{{PAGE['stockpower']}}" size="4">&nbsp Watts</td>
                                    <td><input type="text" maxlength="4" name="sizestock" value="{{PAGE['sizestock']}}" size="4">&nbsp Gallons</td>
                                    <td><input type="text" name="animalstock" value="{{PAGE['animalstock']}}"></td>
                                </tr>
                                <tr>
                                    <th colspan="5"> &nbsp &nbsp &nbsp </th>
                                </tr>
                                <tr>
                                    <th colspan="5"> <input type="submit" value="Submit"> </th>
                                </tr>
                            </table>
                            </form>
                            
                            </br>
                            </br>
                            </br>
                            
                            <form action="/email_update" method="get">
                            <table style="width:100%">
                                <tr>
                                    <th>Email Address 1: &nbsp <input type="text" name="emailadd1" size="75" value="{{PAGE['emailadd1']}}"></th>
                                    <th>Error Messages
                                        <label class="switch">
                                          <input type="checkbox" name="enerrmsg" value="checked"  {{PAGE['enerrmsg']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </th>
                                </tr>
                                <tr>
                                    <th>Email Address 2: &nbsp <input type="text" name="emailadd2" size="75" value="{{PAGE['emailadd2']}}"></th>
                                    <th>New Log Messages
                                        <label class="switch">
                                          <input type="checkbox" name="enlogmsg" value="checked"  {{PAGE['enlogmsg']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </th>
                                </tr>
                                <tr>
                                    <th>Email Address 3: &nbsp <input type="text" name="emailadd3" size="75" value="{{PAGE['emailadd3']}}"></th>
                                    <th>Settings Change Messages
                                        <label class="switch">
                                          <input type="checkbox" name="ensetmsg" value="checked"  {{PAGE['ensetmsg']}}>
                                          <span class="slider round"></span>
                                        </label>
                                    </th>
                                </tr>
                                <tr>
                                    <th> &nbsp &nbsp &nbsp </th>
                                </tr>
                                <tr>
                                    <th align="left"> <input type="submit" value="Update Email Settings"> </th>
                                </tr>
                            </table>
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
