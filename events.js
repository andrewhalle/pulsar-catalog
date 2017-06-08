var catalog;
$(document).ready(setup);

function setup() {
	$.ajax({
		url: "/catalog",
		success: setHTML
	});
	$("#search").keyup(filter);
	$("#next").click(next);
	$("#prev").click(prev);
}

function setHTML(result) {
	catalog = JSON.parse(result);
	render(catalog);
}

function filter() {
	var prestring = $("#search").val();
	for (var i = 0; i < catalog.entries.length; i++) {
		var curr = catalog.entries[i];
		var smaller = Math.min(prestring.length, curr.PSRJ[0].length);
		if (curr.PSRJ[0].slice(0, smaller) == prestring.slice(0, smaller)) {
			curr.visible = true;
		} else {
			curr.visible = false;
		}
	}
	render(catalog);
}

function next() {
	catalog.curr_page += 1;
	render(catalog);
}

function prev() {
	catalog.curr_page -= 1;
	render(catalog);
}

function render(catalog) {
	var table = "<table><tr><th>JName</th><th>RAJ</th><th>DECJ</th></tr>";
	var start_buffer = (catalog.curr_page - 1) * catalog.entries_per_page;
	var entries_left = catalog.entries_per_page;
	var i = 0;
	while (start_buffer > 0 && i < catalog.entries.length) {
		var curr = catalog.entries[i];
		if (curr.visible) {
			start_buffer -= 1;
		}
		i += 1;
	}
	while (entries_left > 0 && i < catalog.entries.length) {
		var curr = catalog.entries[i];
		if (curr.visible) {
			table += "<tr><td>" + curr.PSRJ[0] + "</td><td>" + curr.RAJ[0] + "</td><td>" + curr.DECJ[0] + "</td></tr>";
			entries_left -= 1;
		}
		i += 1;
	}
	table += "</table>";
	$("#table").html(table);
}