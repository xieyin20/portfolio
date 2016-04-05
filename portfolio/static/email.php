<!-- <html>
<head></head>
<body> -->
<?php
if($_POST["submit"]) {
    mail("xieyin@umich.edu", "Form to email message", $_POST["first name"],  $_POST["last name"], $_POST["email"],  $_POST["phone number"], $_POST["message"], "From: an@email.address");
}
?>
<!-- </body>
</html> -->