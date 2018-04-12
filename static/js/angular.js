var app = angular.module('myApp', []);
app.controller('headerCtrl', function($scope, $http) {
    $http({
        url: "/get_ip",
        method: "GET",
    }).then(function successCallback(response) {
        $scope.ipAddress = response.data.ip_address;
    }, function errorCallback(response) {
        $scope.ipAddress = "error";
    });
});

app.controller("fileCtrl", function($scope, $http){
    $http({
        url: "/get_root_path",
        method: "GET",
    }).then(function successCallback(response) {
        $scope.currentLocation = response.data.root_location;
        $scope.formattedLocation = response.data.root_location.replace(/\//g,'!');
        getFolders();
        getFiles();
    });

    function getFolders() {
        let dataToSend = {"currentLocation": $scope.currentLocation};
        $http({
            url: "/get_folders",
            method: "POST",
            data: dataToSend
        }).then(function successCallback(response) {
            $scope.directoryList = response.data.list_of_folders;
        }, function errorCallback(response) {
        })
    }

    function getFiles() {
        let dataToSend = {"currentLocation": $scope.currentLocation};
        $http({
            url: "/get_files",
            method: "POST",
            data: dataToSend
        }).then(function successCallback(response) {
            console.log(response.data.list_of_files);
            $scope.fileList = response.data.list_of_files;
        }, function errorCallback(response) {
            console.log(response)
        })
    }
});



/*
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
}
 */