function DataEditController($scope, $window, DATA_TYPES, EVENTS, DataService, LoginService) {
    $scope.pageTitle = "Data Editor";

    $scope.getObject = function() {
        switch ($scope.objectType) {
            case DATA_TYPES.QUESTION:
                DataService.retrieveQuestion($scope.objectId);
                break;
            case DATA_TYPES.SOLUTION_BY_QUESTIONID:
                DataService.retrieveSolutionByQuestionId($scope.objectId);
                break;
            case DATA_TYPES.SOLUTION:
                DataService.retrieveSolution($scope.objectId);
                break;
            case DATA_TYPES.KEYPOINT:
                DataService.retrieveKeypoint($scope.objectId);
                break;
        }
    }

    if (!!$window.metaData) {
        $scope.objectType = $window.metaData.objectType;
        $scope.objectId = $window.metaData.objectId;
    }

    $scope.updateObject = function() {
        if (LoginService.getToken()) {
            let tokenHeader = LoginService.getTokenHeader();
            $scope.data.content = $scope.formulaData.rawLatex;
            switch ($scope.objectType) {
                case DATA_TYPES.QUESTION:
                    DataService.updateQuestion($scope.data, tokenHeader);
                    break;
                case DATA_TYPES.SOLUTION:
                case DATA_TYPES.SOLUTION_BY_QUESTIONID:
                    DataService.updateSolution($scope.data, tokenHeader);
                    break;
                case DATA_TYPES.KEYPOINT:
                    DataService.updateKeypoint($scope.data, tokenHeader);
            }
        } else {
            $scope.showLoginAlert();
        }
    }

    $scope.$on(EVENTS.DATA_RECEIVED, function() {
        let data = DataService.getData();
        if (data instanceof Array) {
            data = data[0];
        }
        console.log(data);
        $scope.data = data;
        $scope.formulaData.rawLatex = data.content;
    });

}

export default ['$scope', '$window', 'DATA_TYPES', 'EVENTS', 'DataService', 'LoginService', DataEditController];