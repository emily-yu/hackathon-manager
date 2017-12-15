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
function deleteByValue(val, inputs) {
    for(var f in inputs) {
        if(inputs[f] == val) {
            delete inputs[f];
        }
    }
}

function same(n, csv) {
    let temp = new Array();
    temp = csv.split('\n');
    temp = temp.toString().split(',');
    deleteByValue('""', temp)
    for (i = 0; i < temp.length; i += 1) { 
        console.log(temp[i])
        if (temp[i] == undefined) {
            temp.splice(i, 2);
        }
    }
    let fullArray = []
    let avgArray = []
    for(i = 0; i < temp.length; i+=1){ 
        if (avgArray.length == n) {
            fullArray.push(avgArray)
            avgArray = []
            avgArray.push(temp[i])
        }
        else {
            avgArray.push(temp[i])
        }
    }

    createNTable(fullArray)

    // generate some page specific elements
    switch ((location.pathname.substring(location.pathname.lastIndexOf("/") + 1))) {
        case 'sponsors.html':
            replaceInvoices()
            break;
        case 'milestones.html':
            let x = document.getElementsByTagName("td");
            for (var i=0; i<x.length; i++) {
                const initial_text = x[i].textContent
                const row_number = Math.ceil(i/5)
                if ((i+1) % 3 == 0) { // add invoices
                    x[i].innerHTML = '<div class="dropdown">\
                                        <button class="dropbtn" style = "background-color: ' + get_status_color(initial_text) + '">' + initial_text + '</button>\
                                        <div id="myDropdown" class="dropdown-content">\
                                            <a class = "option">Completed</a>\
                                            <a class = "option">In Progress</a>\
                                            <a class = "option">N/A</a>\
                                        </div>\
                                    </div>'
                }
            }
            let buttons = document.getElementsByClassName('dropbtn')
            for (let button of buttons) {
                button.addEventListener('click', function() {
                    document.getElementById("myDropdown").classList.toggle("show");
                })
            }

            // dropdown menu functions
            let open_button;
            window.onclick = function(event) {

                console.log("CLICKED" + event.target)
                console.log("CONTENT " + event.target.textContent)

                const testClass = event.target.className;
                if (testClass == 'option'){
                    let buttonNode = open_button
                    buttonNode.innerHTML = event.target.textContent
                    buttonNode.style.backgroundColor = get_status_color(event.target.textContent)
                }
                else if (event.target.matches('.dropbtn')) {
                    console.log("BAJSDLFDS")
                    console.log(event.target)
                    open_button = event.target
                }
                else if (!event.target.matches('.dropbtn')) {
                    var dropdowns = document.getElementsByClassName("dropdown-content");
                    var i;
                    for (i = 0; i < dropdowns.length; i++) {
                        var openDropdown = dropdowns[i];
                        if (openDropdown.classList.contains('show')) {
                            openDropdown.classList.remove('show');
                        }
                    }
                }
            }

            break;
        default:
            console.log("nah")
    }
}

function get_status_color(status) {
    console.log(status)
    switch (status) {
        case 'In Progress':
            return 'orange'
        case 'N/A':
            return 'red'
        case 'Completed':
            return 'green'
        default:
            return 'black'
    }
}

function replaceInvoices() {
    let x = document.getElementsByTagName("td");
    for (var i=0; i<x.length; i++) {
        const initial_text = x[i].textContent
        const row_number = Math.ceil(i/5)

        if ((i+1) % 5 == 0) { // add invoices
            get_image_names(row_number, i)
        }
    }
}

function setImage(fileNames, elemNumber) {
    let x = document.getElementsByTagName("td");
    const row_number = Math.ceil(elemNumber/5)
    x[elemNumber].innerHTML = '<form action = "' + getNgrok() + 'uploader" method = "POST"\
                        enctype = "multipart/form-data">\
                            <input type = "file" name = "file" />\
                            <input type = "text" name = "row" value = ' + row_number + ' style = "display: none">\
                            <input type = "submit"/>\
                        </form>'

    // check if there was bad response from server
    if (fileNames[0] !== "<!DOCTYPE") {
        for (const file of fileNames) {
            x[elemNumber].innerHTML += '<img src = "application/invoices/' + row_number + '/' + file + '" height = 50><br>'
        }
    }

}

function get_image_names(folder, elemNumber) {
    var myUrl = getNgrok() + 'get_files?folder=' + folder;
    var proxy = 'https://cors-anywhere.herokuapp.com/';

    $.ajax({
        url: proxy + myUrl,
        complete: function(data) {
            console.log(data.responseText.split(/[ ,]+/).filter(Boolean), elemNumber)
            setImage(data.responseText.split(/[ ,]+/).filter(Boolean), elemNumber)
        }
    });
}