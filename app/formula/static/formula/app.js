$(document).ready(function(){
	$('.form').submit(function(e){
		e.preventDefault()
		$.post('/magic/', $('.form').serialize(), function(data){
			
			// $('.output').append('<li>' + data['ibm'] + '</li>', OnSubmitCreateForm('.content', data))
		}, 'json')
	})

})