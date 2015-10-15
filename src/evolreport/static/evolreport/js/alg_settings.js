$(document).ready(function(){

	$('input[type=checkbox]').click(function() {
		var $this = $(this);
		if ($this.is(':checked')) {
			addEvalTab($this.attr('id').split("-toggle")[0]);
		} else {
			removeEvalTab($this.attr('id').split("-toggle")[0]);
		}
	});

	$("#run-alg").click(function(){
		runAlgorithm();
	})

});

function addEvalTab(id){
	$tabs = $("#eval-tabs-area");
	$tabs.append("<li id='"+id+"-tab-header' class='tab col s3 disabled'><a href='#"+id+"-content'>"+id+"</a></li>");
	
	$tabsCollectionDiv = $("#eval-container");
	$tabsCollectionDiv.append("<div id='"+id+"-content' class='col s12' style='padding-top:28px;'>"+id+"</div>");
	$tabs.tabs();
}

function removeEvalTab(id){
	$("#"+id+"-tab-header").remove();
	$("#"+id+"-content").remove();
	$tabs.tabs();
}

function runAlgorithm(){
	$("#alg-wrapper").css('height', function(){
		return $("#alg-wrapper").css('height');
	})
}