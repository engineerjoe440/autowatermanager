<!DOCTYPE html>
<html lang="en" class="fore-mute-dark background-mute-light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title><?php echo $pagetitle ?> - <?php echo $sitetitle ?></title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600&subset=cyrillic,greek" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="//maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="../style/reset.css?v=<?php echo md5($imSettings['general']['version']) ?>"/>
    <link rel="stylesheet" type="text/css" href="../style/style.css?v=<?php echo md5($imSettings['general']['version']) ?>"/>
    <link rel="stylesheet" type="text/css" href="../style/print.css?v=<?php echo md5($imSettings['general']['version']) ?>" media="print"/>
    <link rel="stylesheet" type="text/css" href="css/template.css?v=<?php echo md5($imSettings['general']['version']) ?>">
<?php if (isset($stylesheets) && is_array($stylesheets)):?>
<?php     foreach ($stylesheets as $sheet): ?>
    <link rel="stylesheet" type="text/css" href="<?php echo $sheet ?>?v=<?php echo md5($imSettings['general']['version']) ?>">
<?php endforeach; ?>
<?php endif; ?>
    <link rel="stylesheet" type="text/css" href="css/theme-<?php echo strtolower($theme) ?>.css?v=<?php echo md5($imSettings['general']['version']) ?>">
    <link rel="stylesheet" type="text/css" href="css/print.css?v=<?php echo md5($imSettings['general']['version']) ?>" media="print">
    <script src="../res/jquery.js?v=<?php echo md5($imSettings['general']['version']) ?>"></script>
    <script src="../res/modernizr-custom.js?v=<?php echo md5($imSettings['general']['version']) ?>"></script>
    <script src="../res/x5engine.js?v=<?php echo md5($imSettings['general']['version']) ?>"></script>
    <script>x5engine.settings.currentPath = '../';</script>
    <script src="js/Chart.min.js?v=<?php echo md5($imSettings['general']['version']) ?>"></script>
    <script src="js/controlpanel.js?v=<?php echo md5($imSettings['general']['version']) ?>"></script>
</head>
<body class="fore-mute-dark background-mute-light">
    <div class="main-container">
        <div class="sidebar background-mute-dark fore-white border-right-3 border-color-1 noprint">
            <div class="header">
                <?php if (strlen($logo)): ?>
                <img class="logo" src="<?php echo $logo ?>" alt="<?php echo $sitetitle ?>">
                <?php endif; ?>
                <div class="text">
                    <div class="site-title text-extralarge">
                        <a href="<?php echo $imSettings['general']['url'] ?>"<?php echo isset($redirectJs) ? $redirectJs : "" ?> class="fore-color-inherit" target="_blank"><?php echo $sitetitle ?></a>
                    </div>
                    <div class="site-subtitle">
                        <a href="<?php echo $imSettings['general']['url'] ?>"<?php echo isset($redirectJs) ? $redirectJs : "" ?> class="fore-color-inherit" target="_blank"><?php echo str_replace(array("/", "-"), array("/<wbr>", "-<wbr>"), $sitesubtitle) ?></a>
                    </div>
                    <div class="separator fore-color-1"></div>
                    <div class="username semibold"><?php echo $username ?></div>
                    <a href="login.php?logout" class="logout button fore-white background-color-1"><?php echo strtoupper(l10n("admin_logout", "Logout")) ?></a>
                </div>
            </div>
            <ul class="menu">
<?php
    $menu = array();
    $menu[] = array(
        "url" => "index.php",
        "image" => "images/dashboard_white.png",
        "text" => l10n("dashboard_title", "Dashboard"),
        "selected" => isset($_SERVER['PHP_SELF']) && basename($_SERVER['PHP_SELF']) == "index.php"
    );
    if (isset($imSettings['blog']) && $imSettings['blog']['comments_source'] == 'wsx5') {
        $menu[] = array(
            "url" => "blog.php",
            "image" => "images/blog_white.png",
            "text" => l10n("blog_title", "Blog"),
            "selected" => isset($_SERVER['PHP_SELF']) && basename($_SERVER['PHP_SELF']) == "blog.php"
        );
    }
    if (isset($imSettings['guestbooks']) && count($imSettings['guestbooks'])) {
        $menu[] = array(
            "url" => "guestbook.php",
            "image" => "images/guestbook_white.png",
            "text" => l10n("admin_guestbook", "Guestbook"),
            "selected" => isset($_SERVER['PHP_SELF']) && basename($_SERVER['PHP_SELF']) == "guestbook.php"
        );
    }
    $menu[] = array(
        "url" => "sitetest.php",
        "image" => "images/test_white.png",
        "text" => l10n("admin_test", "Website Test"),
        "selected" => isset($_SERVER['PHP_SELF']) && basename($_SERVER['PHP_SELF']) == "sitetest.php"
    );


    $itemT = new Template("templates/common/menu-entry.php");
    foreach ($menu as $entry) {
        $itemT->url = $entry['url'];
        $itemT->image = $entry['image'];
        $itemT->text = $entry['text'];
        $itemT->selected = $entry['selected'];
        echo "\t\t\t\t" . str_replace("\n", "\n\t\t\t\t", $itemT->render()) . "\n";
    }
?>
            </ul>
        </div>
        <div class="content">
            <div class="text-extralarge toolbar background-mute-vary noprint">
                <div class="hamburger">
                    <div class="bar background-mute-dark"></div>
                    <div class="bar background-mute-dark"></div>
                    <div class="bar background-mute-dark"></div>
                </div>
<?php if (strlen($pagetitle)): ?>
                <div class="pagetitle uppercase fore-color-1"><?php echo $pagetitle ?></div>
<?php endif; ?>
<?php if (strlen($logo)): ?>
                <img class="logo" src="<?php echo $logo ?>" alt="<?php echo $sitetitle ?>">
<?php endif; ?>
            </div>
            <?php echo $content ?>
        </div>
    </div>
</body>
</html>

