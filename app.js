function loadData() {
	function csvToArray (csv) {
	    rows  = csv.split("\n");
	    return rows.map(function (row) {
	    	return row.split(",");
	    });
	};

	// Hard-coded for brevity, but you can set this variable with FileReader
	var csv = CSVParse("data.csv")

	var array = csvToArray(csv);
	return array;
}

function createTable() {
    var array = [["god bless",2,3,4],[4,5,6,4],[7,8,9,4]];
    // var array = loadData();
    var content = "";
    array.forEach(function(row) {
        content += "<tr>";
        row.forEach(function(cell) {
            content += "<td>" + cell + "</td>" ;
        });
        content += "</tr>";
    });
    document.getElementById("1").innerHTML = content;
}

function createTable2() {
    var array = [["god bless",2,3,4],[4,5,6,4],[7,8,9,4]];
    // var array = loadData();
    var content = "";
    array.forEach(function(row) {
        content += "<tr>";
        row.forEach(function(cell) {
            content += "<td>" + cell + "</td>" ;
        });
        content += "</tr>";
    });
    document.getElementById("1").innerHTML = content;
    document.getElementById("2").innerHTML = content;
}