$(document).ready(setup);

function setup() {
	$.ajax({
		url: "/catalog",
		data: {
			string: "",
			func: "search_bar_change"
		},
		success: setHTML
	});
	$("#update").click(get_new_catalog);
	$("#next").click(next);
	$("#prev").click(prev);
}

function setHTML(result) {
	$("#table").html(result)
}

function get_new_catalog() {
	$.ajax({
		url: "/catalog",
		data: {
			string: $("#search").val(),
			func: "search_bar_change"
		},
		success: setHTML
	});
}

function next() {
	$.ajax({
		url: "/catalog",
		data: {
			string: $("#search").val(),
			func: "page_next"
		},
		success: setHTML
	});
}

function prev() {
	$.ajax({
		url: "/catalog",
		data: {
			string: $("#search").val(),
			func: "page_prev"
		},
		success: setHTML
	});
}