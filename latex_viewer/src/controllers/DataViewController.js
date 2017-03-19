function DataViewController($scope, $window, DATA_TYPES, EVENTS, DataService) {
    $scope.pageTitle = "Data Viewer";

    $scope.getObjects = function(dataType) {
        $scope.dataType = dataType;

        switch ($scope.dataType) {
            case DATA_TYPES.QUESTION:
                $scope.dataTypeTitle = "Question";
                $scope.hideContent = true;
                DataService.retrieveQuestions();
                break;
            case DATA_TYPES.SOLUTION:
                $scope.dataTypeTitle = "Solution";
                $scope.hideContent = true;
                DataService.retrieveSolutions();
                break;
            case DATA_TYPES.KEYPOINT:
                $scope.dataTypeTitle = "Keypoint";
                $scope.hideContent = true;
                DataService.retrieveKeypoints();
                break;
        }
    }

    $scope.$on(EVENTS.DATAS_RECEIVED, function() {
        $scope.datas = DataService.getDatas();
        $scope.datasCount = $scope.datas.length;
        $scope.maxPage = Math.ceil($scope.datasCount / $scope.pageLimit);

        $scope.contents = [];
        $scope.datas.forEach(function(data) {
            $scope.contents.push(data.content.replace(/;/g, '</br>'));
        });
        $scope.curPage = 1;
    });

    $scope.pageLimit = 100;

    $scope.$on('cfpLoadingBar:completed', function() {
        $scope.hideContent = false;
    });

    $scope.openDataEditor = function(objectId) {
        $window.open('data_editor.html', '_blank').metaData = {
            objectType: $scope.dataType,
            objectId: objectId
        };
    }
}

export default ['$scope', '$window', 'DATA_TYPES', 'EVENTS', 'DataService', DataViewController];