$(function(){
	$('button').click(function(){
		var val = $(this).val();
		var display = $("#target").text()
		var btnType = $(this).attr("name");
		console.log(btnType)
		setupData()
		$.ajax({
			url: '/update',
			data: {'buttonValue':val, 'buttonType':btnType, 'display':display},
			type: 'POST',
			success: function(response){
				$("#target").text(response)
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});

