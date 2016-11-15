
var fila='<div class="row embed-responsive embed-responsive-16by9 cust">'+
'			 	<iframe class="embed-responsive-item" src="https://www.youtube.com/embed/<videoid>"></iframe>'+
'			</div>';

var url = '/test?';
var qry='';

function busqueda(){
	$("#resultados").html('');
	qry=$("#filtro").val();
    $.getJSON(url,
		{
		'q':qry
		},
		 function(result){
        $.each(result.items, function(i, field){
            $("#resultados").append(fila.replace('<videoid>',field.id.videoId));
        });
    });	
}
