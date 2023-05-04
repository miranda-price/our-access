<?php

$emailTo = "miranda27price@gmail.com";
$name = Trim(stripslashes($_POST['reporter-name'])); 
$email = Trim(stripslashes($_POST['reporter-email'])); 
$phone = Trim(stripslashes($_POST['reporter-phone']));
$building = $_POST['repair-builidng'];
$floor = $_POST['repair-floor'];
$room = $_POST['repair-room'];
$feature = $_POST['report-details'];

$body = "";

$body .= "Reported ";
$body .= $feature;
$body .= " located in ";
$body .= "\n";
$body .= "Building: ";
$body .= $building;
$body .= "\n";
$body .= "Floor: ";
$body .= $floor;
$body .= "\n";
$body .= "Room: ";
$body .= $room;
$body .= "\n";

$body .= "Reporter Contact Info: ";
$body .= "\n";
$body .= "Name: ";
$body .= $name;
$body .= "\n";
$body .= "Email: ";
$body .= $email;
$body .= "\n";
$body .= "Phone: ";
$body .= $phone;
$body .= "\n";

$body .= "Email automatically generated using Our Access at ouraccess.digitalscholar.rochester.edu/service-request.php";
$body .= "\n";

mail($emailTo, "Service Request", $body, "From: <$email>");
mail($email, "Copy: Service Request", $body, "From: <$email>");

?>