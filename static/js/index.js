var current_location;

$(document).ready(function() {
     $.ajax({
        type: "GET",
        url: "/get_location",
        success: response => {
            current_location = response.current_location;
                displayFolders();
                displayFiles();
        }
    });

});


function displayFiles(){
        $.ajax({
            type: "POST",
            url: "/get_files",
            data: {'currentLocation': current_location},
            success: function(response){
				$.each(response.list_of_files, function(index, value){
					var div = $("<div class='fileDiv'></div>")
					var a = $("<a data-type = 'file' href='#'>" + value + "</a>")
					div.append(a)
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
    data: {'currentLocation': current_location},
    success: function(response){
        $.each(response.list_of_folders, function(index, value){
            var div = $("<div class='folderDiv'></div>")
            var p = $("<p style='color:red;cursor:pointer;' data-type = 'folder' style='display: inline;'>" + value + "</p>")
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
        var formattedLocation = current_location
        for(let i = 0;i < formattedLocation.length; i ++){
            formattedLocation = formattedLocation.replace(char, '!')
        }
        value.href="/download_file/" + formattedLocation + '!' + value.innerHTML;
    })
    }



function addLinksToFolders(){
    folderDivs = $($("#folders").children())
    console.log(folderDivs);
    $.each(folderDivs, function(index, value){
        $(value).click(function(){
            current_location = current_location + "/" + $(value).children()[0].innerHTML
            refreshTable();
        })
    })
}


function moveBack(){
    if(current_location == "/home"){
        return
    }
    for(let i = current_location.length - 1;i > 0;i--){
    	if(current_location[i] == "/"){
	    	current_location = current_location.substring(0, i);
	    	refreshTable();
		    break;
        }
    }
}


    function addCompress(){
        var char = "/"
        var formattedLocation = current_location.substring(1, current_location.length)
        for(let i = 0;i < formattedLocation.length; i ++){
            formattedLocation = formattedLocation.replace(char, '!')
        }
        $("#compresser").attr("href", "/compress_folder/" + '!' + formattedLocation);
}

function refreshTable(){
    $("#files").html(" ")
    $("#folders").html(" ")
    displayFolders();
    displayFiles();
    addCompress()
}

