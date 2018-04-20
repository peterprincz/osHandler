var app = angular.module('myApp', []);
app.controller('headerCtrl', function($scope, $http) {

    $http({
        url: "/get_ip",
        method: "GET"
    }).then(function successCallback(response) {
        $scope.ipAddress = response.data.ip_address;
    }, function errorCallback(response) {
        $scope.ipAddress = "error";
    });
});


app.controller("fileCtrl", function($scope, $http){
    $scope.lastLocations = [];

    $scope.propertyName = 'age';
    $scope.reverse = true;

    $scope.sortBy = function(propertyName) {
        $scope.reverse = ($scope.propertyName === propertyName) ? !$scope.reverse : false;
        $scope.propertyName = propertyName;
    };

    $http({
        url: "/get_root_path",
        method: "GET"
    }).then(function successCallback(response) {
        $scope.currentLocation = response.data.root_location;
        $scope.formattedLocation = response.data.root_location.replace(/\//g,'!');
        refreshWindow();
        getLocationForNavbar();
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
            url: "/get_files_with_size",
            method: "POST",
            data: dataToSend
        }).then(function successCallback(response) {
            $scope.fileList = response.data;
        }, function errorCallback(response) {
            console.log(response);
        })
    }

    $scope.moveIntoFolder = function(folder){
        console.log("hello")
        $scope.lastLocations = [];
        $scope.currentLocation =  $scope.currentLocation + "/" + folder;
        refreshFormattedLocation();
        refreshWindow();
    };

    $scope.moveToFolder = function(path){
        $scope.lastLocations.push($scope.currentLocation);
        $scope.currentLocation = path;
        refreshFormattedLocation();
        refreshWindow();
    };


    $scope.moveOutOfFolder = function(){
        $scope.lastLocations.push($scope.currentLocation);
        var currentLocation = $scope.currentLocation;
        if(currentLocation == "/"){
            return;
        }
        for(let i = currentLocation.length - 1;i > -1;i--){
            if(currentLocation[i] == "/"){
                if(i == 0){
                    $scope.currentLocation = "/";
                    $scope.formattedLocation = "";
                    refreshWindow();
                    return;
                }
                $scope.currentLocation = currentLocation.substring(0, i);
                refreshFormattedLocation();
                refreshWindow();
                return;
            }
        }
    };

    $scope.moveBackAFolder = function moveBackAFolder(){
        if($scope.lastLocations.length > 0) {
            $scope.currentLocation = $scope.lastLocations.pop();
            refreshFormattedLocation();
            refreshWindow();
        }
    };

    $scope.refreshWindow = function(){
        refreshWindow();
    }

    function refreshWindow() {
        getFolders();
        getFiles();
        getLocationForNavbar();
    }

    function refreshFormattedLocation(){
        $scope.formattedLocation = $scope.currentLocation.replace(/\//g,'!');
    }

    $scope.uploadFile = function(){
        var file = $("#uploadFile")[0].files[0];
        var upload = new Upload(file);
        upload.doUpload($scope.formattedLocation);
    }

    function getLocationForNavbar(){
        let listOfFolders = $scope.currentLocation.split("/");
        $scope.foldersForNavbar = [];
        if(listOfFolders.toString() === ["", ""].toString()){
            console.log("true")
            folderNameWPath = {};
            folderNameWPath["folderName"] = "/";
            folderNameWPath["folderPath"] = "/";
            $scope.foldersForNavbar.push(folderNameWPath);
            console.log(folderNameWPath)
            return;
        }
        listOfFolders.forEach(function (folderName, number) {
            let folderNameWPath = {};
            folderNameWPath["folderName"] = folderName + "/";
            folderNameWPath["folderPath"] = "/" + $scope.currentLocation.split("/").slice(0, number +  1).join('/').substring(1);
            $scope.foldersForNavbar.push(folderNameWPath)
        });
    }

});
