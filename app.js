var csv = "city,state,population,land area, seattle,WA,652405,83.9, new york,NY,8405837,302.6, boston,MA,645966,48.3, kansas city,MO,467007,315.0"

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




function createNTable(array) {
    // var array = [["god bless",2,3,4],[4,5,6,4],[7,8,9,4]];
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



// array with n strings inside each array
// if n = 3, then [[a, b, c], [a , b, c]]
function same(n){
    var temp = new Array();
    // this will return an array with strings "1", "2", etc.
    temp = csv.split(",");
    var fullArray = []
    var avgArray = []
    for(i = 0; i < temp.length; i+=1) { 
        console.log(i)
        if (avgArray.length == n) {
            fullArray.push(avgArray)
            avgArray = []
        }
        else {
            avgArray.push(temp[i])
        }
    }
    console.log(fullArray)
    createNTable(fullArray)
}