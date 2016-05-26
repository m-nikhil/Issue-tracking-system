<!-- security lock goes here-->


<!DOCTYPE HTML>
<html>
<head>
<title>Edit Profile</title>

<?php
	require('utility/links.php')
?>

</head>
<body>

<div class="header-bg">
	<div class="wrap"> 
		<div class="total-box">
			<div class="total">
				<div class="header_top">
				    <!-- navbar goes here -->
				    <?php 
				    	include('utility/login navbar.php');
				    ?>

				</div>

				<div class="header-bottom">
					<!-- Title and logo goes here-->
					<?php 
				    	include('utility/title and logo.php');
				    ?>

					<div class="clear"></div>
				</div>
			</div>
		</div>
	</div>
</div>

<div class="banner-box">
		<div class="wrap">
			<div class="main-top">
				<div class="main">
					<div>
						<!--secondary navbar goes here-->

					</div>
					<div >
						<!-- Body goes here -->
						<?php
							include('body/client login.php');
						?>
					</div>
				</div>
			</div>
		</div>
</div>

</body>
</html>