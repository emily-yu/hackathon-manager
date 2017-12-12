// var request = new XMLHttpRequest();
// var cors = require('cors')

// request.onreadystatechange = function() {
//     if (request.readyState === 4) {
//         if (request.status === 200) {
//             document.body.className = 'ok';
//             console.log(request.responseText);
//         } else {
//             document.body.className = 'error';
//         }
//     }
// };


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
    var content = "";
    array.forEach(function(row) {
        content += "<tr>";
        row.forEach(function(cell) {
            content += "<td>" + cell + "</td>" ;
        });
        content += "</tr>";
    });
    document.getElementById("1").innerHTML += content;
}

function clean(obj) {
  for (var propName in obj) { 
    if (obj[propName] === null || obj[propName] === undefined) {
      delete obj[propName];
    }
  }
}
function deleteByValue(val, fruits) {
    for(var f in fruits) {
        if(fruits[f] == val) {
            delete fruits[f];
        }
    }
}

function same(n, csv) {
    var temp = new Array();
    console.log("START")
    temp = csv.split('\n');
    console.log(temp)
    temp = temp.toString().split(',');
    console.log(temp)
    // temp = temp.toString().split(/[ ,]+/);
    console.log(temp)
    // temp = list(filter(lambda x: x!= ('""'), temp))
    console.log(temp)
    deleteByValue('""', temp)
    console.log(temp)
    for (i = 0; i < temp.length; i += 1) { 
        // temp[i] = temp[i].replace("***", " ")
        // console.log(temp[i])
        // temp[i] = temp[i].replace(/\W/g, '')
        console.log(temp[i])
        if (temp[i] == undefined) {
            temp.splice(i, 2);
        }
    }
    var fullArray = []
    var avgArray = []
    for(i = 0; i < temp.length; i+=1){ 
        console.log(i)
        if (avgArray.length == n) {
            fullArray.push(avgArray)
            avgArray = []
            avgArray.push(temp[i])
        }
        else {
            avgArray.push(temp[i])
        }
    }

    // judging
    if (n == 12) {
        for (i = 0; i < fullArray.length; i+=1) { 
            console.log(temp[i])
        }
    }

    console.log(fullArray)
    createNTable(fullArray)
}