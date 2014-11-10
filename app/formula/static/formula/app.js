$(document).ready(function(){
	$('.form').submit(function(e){
		e.preventDefault()
		$.post('/magic/', $('.form').serialize(), function(data){
		}, 'json')
	})
})