<?php

include "includes.php";

// Redirect to a specific section
$redirect = Configuration::getControlPanel()->getRedirectFromArray($_GET);
if ($redirect) {
    header("Location: " . $redirect);
    exit(0);
}
// Otherwise attempt the login
Configuration::getControlPanel()->accessOrRedirect();

$main = Configuration::getControlPanel()->getMainTemplate();
$main->pagetitle = l10n("admin_dashboard", "Dashboard");
$main->stylesheets = array("css/dashboard.css");
$main->content = "";






// -----------------
// Tests
// -----------------

// Results list
$results = imTest::testWsx5Configuration();
$list = "";
$count = 0;
$testT = new Template("templates/dashboard/test-row.php");
foreach ($results as $result) {
    if (!$result['success']) {
        $count++;
        $testT->name = $result['name'];
        $list .= $testT->render();
    }
}

if ($count > 0) {
    $boxT = new Template("templates/dashboard/box.php");
    $boxT->title = l10n("admin_test_title", "Website Test");
    $boxT->content = "";
    $boxT->image = "images/test_black.png";

    // Summary
    $rowT = new Template("templates/dashboard/summary-row.php");
    $rowT->icon = "fa-exclamation-triangle";
    $rowT->iconColoredClass = "background-color-3";
    $rowT->iconEmptyClass = "background-mute";
    $rowT->value = $count;
    $rowT->caption = ucfirst(l10n("admin_test_notpassed", "Not passed"));
    $boxT->content .= $rowT->render();

    // Errors list
    $boxT->content .= $list;

    $main->content .= $boxT->render();
}


echo $main->render();

