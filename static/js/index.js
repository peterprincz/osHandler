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
            var a = $("<a href=compress_folder/" + value +" style='display: inline;'>ZIP</a>")
            div.append(p)
            div.append(a)
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
    folders = $("#folders").children()
    console.log(folders);
    $.each(folders, function(index, value){
        $(value).click(function(){
            $.ajax({
            type: "GET",
            url: "/move_to/" + $(this).children()[0].innerHTML,
            success :function(data){
                $("#current_folder").html(data.current_location)
                refreshTable()
            }
            })
        })
    })
}


function refreshTable(){
    $("#files").html(" ")
    $("#folders").html(" ")
    displayFolders();
    displayFiles();
}


function moveBack(){
        $.ajax({
        type: "GET",
        url: "/move_back",
        success : function(data){
            $("#current_folder").html(data.current_location)
            refreshTable();
        }
        })
}