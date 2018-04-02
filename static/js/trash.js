
function refreshCurrentFolder(){
        $.ajax({
            type: "GET",
            url: "/get_location",
            success: response => {
                $("#currentPath").html(response.current_location);
            }
        });
}


























function displayFolders(){
$.ajax({
    type: "GET",
    url: "/get_folders",
    success: function(data){
        $.each(data.list_of_folders, function(index, value){
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
    $.each(list_of_files, function(index, value){
        value.href="/download_file/" + value.innerHTML;
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