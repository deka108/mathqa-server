function DataController($scope, EVENTS, DataService, LoginService) {
    $scope.pageTitle = "Data Editor";

    $scope.getObject = function() {
        console.log($scope.objectId);
        switch ($scope.objectType) {
            case "question":
                DataService.retrieveQuestion($scope.objectId);
                break;
            case "solution":
                DataService.retrieveSolution($scope.objectId);
                break;
            case "keypoint":
                DataService.retrieveKeypoint($scope.objectId);
                break;
        }
    }

    $scope.updateObject = function() {
        if (LoginService.getToken()) {
            let tokenHeader = LoginService.getTokenHeader();

            switch ($scope.objectType) {
                case "question":
                    DataService.updateQuestion($scope.data, tokenHeader);
                    break;
                case "solution":
                    DataService.updateSolution($scope.data, tokenHeader);
                    break;
                case "keypoint":
                    DataService.updateKeypoint($scope.data, tokenHeader);
            }
        } else {
            console.error("Need to login first!!");
        }
    }

    $scope.$on(EVENTS.DATA_RECEIVED, function() {
        let data = DataService.getData();
        $scope.formulaData.rawLatex = data.content;
    });

}

export default ['$scope', 'EVENTS', 'DataService', 'LoginService', DataController];