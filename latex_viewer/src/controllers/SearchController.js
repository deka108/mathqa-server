function SearchController($scope, EVENTS, DataService) {
    $scope.pageTitle = "Search View";

    $scope.search = function(query) {
        switch ($scope.searchType) {
            case "questionId":
                $scope.promise = DataService.searchQuestions(parseInt(query));
                break;
            case "conceptId":
                $scope.promise = DataService.searchQuestions("?concept=" + parseInt(query));
                break;
            case "subconceptId":
                $scope.promise = DataService.searchQuestions("?subconcept=" + parseInt(query));
                break;
            case "fulltext":
                $scope.promise = DataService.fullTextSearch(query);
                break;
            case "db":
                $scope.promise = DataService.exactSearchDb(query);
                break;
            case "formula":
                $scope.promise = DataService.searchFormula(query);
                break;
        }
    }

    $scope.$on(EVENTS.SEARCH_RECEIVED, function() {
        $scope.results = DataService.getSearchResults();
        $scope.questions = "";
        $scope.resultCount = $scope.results.length;
        console.log($scope.results);
    });


    $scope.$on(EVENTS.QUESTIONS_RECEIVED, function() {
        let result = DataService.getSearchResults();
        if (result instanceof Array) {
            $scope.questions = result;
        } else {
            $scope.questions = [result];
        }
        $scope.results = "";
        $scope.resultCount = $scope.questions.length;
        console.log($scope.questions);
    });
}

export default ['$scope', 'EVENTS', 'DataService', SearchController];