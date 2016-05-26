<br><br><br><br><br><br><br>
<div class="row">
	<div class="col-xs-offset-1 col-xs-10 col-sm-offset-3 col-sm-6 col-md-offset-3 col-md-6">
		<p style="font-size: 20px;padding-left: 30%;">Submit Issue</p> 
		<br>
		<form action = "function/client login.php action="function/student-academicchange.php" method="POST" enctype="multipart/form-data"" method="POST">                                                                        
			<div class="form-group">
				<select class="form-control" name="project name" autofocus>
					<option value="bug">Bug</option>
					<option value="feature">feature</option>
				</select>
			</div>
			<div class="form-group">
				<input type="password" class="form-control" placeholder="Subject of the issue" name="subject" autofocus required>
			</div>
			<div class="form-group">
				<textarea class="form-control" placeholder="Description of the issue"  name="description" autofocus></textarea>
			</div>
			<div class="row">	
				<br>		
				<div class="col-xs-offset-5">
					<input type="Submit" class="btn btn-default" value="Login">
				</div>
			</div>
		</form>
	</div>
</div>