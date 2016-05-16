<?php
session_start();

if (isset($_COOKIE['NODE'])) {
  echo "NODE-> ".$_COOKIE['NODE']."<br>";
}

if (isset($_GET['user'])) {
  $user = $_GET['user'];
  $_SESSION[$user] = $_SESSION[$user] + 1;
}

echo "HOST-> ".gethostname()."<br> ";

if (isset($_SESSION[$user])) {
  echo "USER-> ".$user."<br> ";
  echo "VECES-> ".$_SESSION[$user];
}



 ?>
