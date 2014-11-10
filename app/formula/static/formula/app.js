$(document).ready(function(){
	$(document).on('submit', '.form', function(e){
		e.preventDefault()
		$.post('/magic/', $('.form').serialize(), function(data){
			console.log(data)
		})
		})
})
