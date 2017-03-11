function DataViewController($scope, EVENTS, DataService) {
    $scope.pageTitle = "Data Viewer";

    $scope.getObjects = function(dataType) {
        switch (dataType) {
            case "question":
                $scope.dataType = "Question";
                $scope.hideContent = true;
                DataService.retrieveQuestions();
                break;
            case "solution":
                $scope.dataType = "Solution";
                $scope.hideContent = true;
                DataService.retrieveSolutions();
                break;
            case "keypoint":
                $scope.dataType = "Keypoint";
                $scope.hideContent = true;
                DataService.retrieveKeypoints();
                break;
        }
    }

    $scope.$on(EVENTS.DATAS_RECEIVED, function() {
        $scope.datas = DataService.getDatas();
        $scope.datasCount = $scope.datas.length;
        $scope.maxPage = Math.round($scope.datasCount / $scope.pageLimit) + 1

        $scope.contents = [];
        $scope.datas.forEach(function(data) {
            $scope.contents.push(data.content.replace(/;/g, '</br>'));
        });
    });

    $scope.pageLimit = 100;
    $scope.curPage = 1;

    $scope.nextPage = function() {
        if ($scope.curPage < $scope.maxPage) {
            $scope.curPage++;
        }
    }

    $scope.previousPage = function() {
        if ($scope.curPage > 1) {
            $scope.curPage--;
        }
    }

    $scope.$on('cfpLoadingBar:completed', function() {
        $scope.hideContent = false;
    });

}

export default ['$scope', 'EVENTS', 'DataService', DataViewController];