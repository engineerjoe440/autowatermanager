<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script type="text/javascript" src="/static/scripts.js"></script>
<link rel="icon" href="/static/favicon.ico" type="image/vnd.microsoft.icon" />
<style>
body{
    background-color: #4c0099;
    color: #ffffff;
}

a{ color: #99ffff; }

img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
</head>
<body>

<h2>AutoWaterManager Update</h2>
<p>The AutoWaterManager has successfully issued a GIT Pull Request, the results are:</p>
<p>{{PAGE['response']}}</p>
<br>
<br>
<p>This page will refresh to reload and reconnect to the AutoWaterManager in 
<span onload="countdown_redirect('counter', uri='index.html');" id="counter">200</span> seconds.</p>
<br>
<br>
<p>If the page does not reload, you can manually return <a href="/index.html">home</a>.</p>

</body>
</html>