function AppController($scope, EVENTS, QuestionDataService) {
    QuestionDataService.retrieveData();

    $scope.$on(EVENTS.DATA_RECEIVED, function(evt, data) {
        $scope.questions = data;
        console.log($scope.questions);
        renderMathInElement(document.body);
    });
}

export default ['$scope', 'EVENTS', 'QuestionDataService', AppController];