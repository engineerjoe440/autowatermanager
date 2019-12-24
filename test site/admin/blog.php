<?php

include "includes.php";

Configuration::getControlPanel()->accessOrRedirect();

// Load the main template
$mainT = Configuration::getControlPanel()->getMainTemplate();
$mainT->pagetitle = l10n("blog_title", "Blog");
//$mainT->stylesheets = array("css/comments.css");
$mainT->content = "";
$contentT = new Template("templates/common/box.php");
$contentT->cssClass = "blog";
$contentT->content = "";

// Show the category and post selectors
$selectorsT = new Template("templates/blog/selectors.php");
$selectorsT->categories = $imSettings['blog']['posts_cat'];
$selectorsT->selectedCategory = @$_GET['category'];
$selectorsT->posts = $imSettings['blog']['posts'];
if (isset($_GET['category'])) {
	$selectorsT->categoryPosts = $imSettings['blog']['posts_cat'][$_GET['category']];
	$selectorsT->selectedPost = @$_GET['post'];
}
$contentT->content .= $selectorsT->render();

$topic = false;
if (isset($_GET['category']) && isset($_GET['post'])) {
}

$mainT->content = $contentT->render();
echo $mainT->render();
