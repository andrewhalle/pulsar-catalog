var catalog;
$(document).ready(setup);

function setup() {
	$.ajax({
		url: "/gen_catalog",
		success: setHTML
	});
	$("#search").keyup(filter);
	$("#ATNF").change(filter);
	$("#RRATalog").change(filter);
	$("#Parallaxes").change(filter);
	$("#GCpsr").change(filter);
	$("#next").click(next);
	$("#prev").click(prev);
}

function setHTML(result) {
	catalog = JSON.parse(result);
	catalog.entries_per_page = 10;
	catalog.pages = Math.ceil(catalog.entries.length / catalog.entries_per_page);
	catalog.curr_page = 1;
	filter();
}

function filter() {
	console.log("here");
	var prestring = $("#search").val();
	var numVisible = 0;
	for (var i = 0; i < catalog.entries.length; i++) {
		var curr = catalog.entries[i];
		var smaller = Math.min(prestring.length, curr.Name.length);
		if (curr.Name.slice(0, smaller) == prestring.slice(0, smaller)) {
			curr.visible = true;
		} else {
			curr.visible = false;
		}
		var sourceNames = [];
		for (source of curr.sources) {
			sourceNames.push(source.Name);
		}
		if ($("#ATNF").is(":checked") && curr.visible) {
			if ($.inArray("ATNF", sourceNames) == -1) {
				curr.visible = false;
			}
		}
		if ($("#RRATalog").is(":checked")) {
			if ($.inArray("RRATalog", sourceNames) == -1) {
				curr.visible = false;
			}
		}
		if ($("#Parallaxes").is(":checked")) {
			if ($.inArray("Parallaxes", sourceNames) == -1) {
				curr.visible = false;
			}
		}
		if ($("#GCpsr").is(":checked")) {
			if ($.inArray("GCpsr", sourceNames) == -1) {
				curr.visible = false;
			}
		}
		if (curr.visible) {
			numVisible += 1;
		}
	}
	if (numVisible === 0) {
		numVisible = 1;
	}
	catalog.pages = Math.ceil(numVisible / catalog.entries_per_page);
	catalog.curr_page = 1;
	render(catalog);
}

function next() {
	if (catalog.curr_page != catalog.pages) {
		catalog.curr_page += 1;
		render(catalog);
	}
}

function prev() {
	if (catalog.curr_page != 1) {
		catalog.curr_page -= 1;
		render(catalog);
	}
}

function render(catalog) {
    var table = '<table style="padding: 0px;margin 2vh 5vw 0px 5vw; width: 90vw; text-align: center"><tr><th>Name</th><th>RA</th><th>DEC</th><th>Sources</th></tr>';
	var start_buffer = (catalog.curr_page - 1) * catalog.entries_per_page;
	var entries_left = catalog.entries_per_page;
	var i = 0;
	var curr;
	while (start_buffer > 0 && i < catalog.entries.length) {
		curr = catalog.entries[i];
		if (curr.visible) {
			start_buffer -= 1;
		}
		i += 1;
	}
	while (entries_left > 0 && i < catalog.entries.length) {
		curr = catalog.entries[i];
		if (curr.visible) {
			var sourceNames = [];
			for (var source of curr.sources) {
				sourceNames.push(source.Name);
			}
			table += "<tr><td><a target=\"_blank\" href=/entries/" + curr.Name.replace("/", "-") + ">" + curr.Name + "</a></td><td>" + curr.RA + "</td><td>" + curr.DEC + "</td><td>" + sourceNames.join() + "</td></tr>";
			entries_left -= 1;
		}
		i += 1;
	}
	table += "</table>";
	$("#table").html(table);
	$("#pageinfo").html(catalog.curr_page.toString() + " of " + catalog.pages.toString());
}
