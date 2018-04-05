var currentLocation;
var lastLocations = []

$(document).ready(function() {
     $.ajax({
        type: "GET",
        url: "/get_location",
        success: response => {
            currentLocation = response.current_location;
            displayFolders();
            displayFiles();
            displayIpAddress()
            displayLocation()
        }
    });
});

function displayIpAddress(){
    $.ajax({
        type:"GET",
        url : "/get_ip",
        success : response => $("#ipAdress").html('(' + response.ip_address + ')')
    })
}



function displayFiles(){
        $.ajax({
            type: "POST",
            url: "/get_files_with_size",
            data: {'currentLocation': currentLocation},
            success: function(response){
				$.each(response, function(index, value){
					var div = $("<div class='fileDiv'></div>")
					var a = $("<a class='file' data-type='file' href='#'>" + value.name + "</a>")
					if((value.size / 1024) / 1024 > 1){
					    var p = $("<p data-type = 'fileSize' >" + (((value.size + 0.0) / 1024) / 1024).toFixed(2) + " Mb" +"</p>")
					} else {
					    if(value.size / 1024 > 1){
					        var p = $("<p data-type = 'fileSize' >" + ((value.size + 0.0) / 1024).toFixed(2) + " Kb" +"</p>")
					    } else {
					        var p = $("<p data-type = 'fileSize' >" + (value.size) + " Bytes </p>")
					    }
					}
					div.append(a)
					div.append(p)
					$("#files").append(div);
				})
				addLinksToFiles();
			}
            })
        };



function displayFolders(){
$.ajax({
    type: "POST",
    url: "/get_folders",
    data: {'currentLocation': currentLocation},
    success: function(response){
        $.each(response.list_of_folders, function(index, value){
            var div = $("<div class='folderDiv'></div>")
            var p = $("<p class='folder' data-type='folder'>" + value+ "</p>")
            div.append(p)
            $("#folders").append(div)
        })
        addLinksToFolders();
    }
    })
};


function addLinksToFiles(){
    let list_of_files = $("[data-type='file']")
    let char = '/'
    $.each(list_of_files, function(index, value){
        var formattedLocation = currentLocation
        for(let i = 0;i < formattedLocation.length; i ++){
            formattedLocation = formattedLocation.replace(char, '!')
        }
        value.href="/download_file/" + formattedLocation + '!' + value.innerHTML;
    })
    }



function addLinksToFolders(){
    folderDivs = $($("#folders").children())
    $.each(folderDivs, function(index, value){
        $(value).click(function(){
            currentLocation = currentLocation + "/" + $(value).children()[0].innerHTML
            lastLocations = []
            refreshTable();
        })
    })
}


function moveBack(){
    let a = lastLocations.pop();
    if(a != null){
        currentLocation = a
    }
    refreshTable();
}

function displayLocation(){
    $("#currentLocation").html("")
    var listOfFolders = currentLocation.split("/")
    listOfFolders[0] = "/"
    var fullroute = $("<div></div>")
    let folder = $("<p class='path'>" + listOfFolders[0] + "</p>")
    fullroute.append(folder)
    for(let i = 1;i < listOfFolders.length;i++){
        let folder = $("<p class='path'>" + listOfFolders[i] + "/</p>")
        $(folder).click(function(){
            lastLocations = []
            lastLocations.push(currentLocation)
            let b = "/"
            b += currentLocation.split("/").slice(0, i +  1).join('/').substring(1)
            currentLocation = b;
            refreshTable();
        })
        fullroute.append(folder)
    }
    $("#currentLocation").append(fullroute)
}


function moveUp(){
    if(currentLocation == "/"){
        return;
    }
    lastLocations.push(currentLocation)
    for(let i = currentLocation.length - 1;i > -1;i--){
    	if(currentLocation[i] == "/"){
    	    if(i == 0){
    	        currentLocation = "/"
    	        refreshTable();
    	        return;
    	    }
	    	currentLocation = currentLocation.substring(0, i);
	    	refreshTable();
		    return;
        }
    }
}


function addCompress(){
    var formattedLocation = currentLocation.substring(1, currentLocation.length)
    for(let i = 0;i < formattedLocation.length; i ++){
        formattedLocation = formattedLocation.replace("/", '!')
    }
    $("#compresser").attr("href", "/compress_folder/" + '!' + formattedLocation);
}

function refreshTable(){
    $("#files").html(" ")
    $("#folders").html(" ")
    displayFolders();
    displayFiles();
    addCompress()
    displayLocation()
}

