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
            case "formula_category":
                $scope.promise = DataService.searchQuestions("?formula_categories=" + encodeURIComponent(query.toLowerCase()));
                break;
            case "db":
                $scope.promise = DataService.exactSearchDb(query);
                break;
            case "fulltext":
                $scope.promise = DataService.fullTextSearch(query);
                break;
            case "formula":
                $scope.promise = DataService.searchFormula(query);
                break;
        }
    }

    $scope.$on(EVENTS.SEARCH_RECEIVED, function() {
        let results = DataService.getSearchResults();
        if (results instanceof Array) {
            $scope.results = results;
        } else {
            $scope.results = [results];
        }
        $scope.questions = "";
        if (!results || (results.length == 1 && results[0] == "")) {
            $scope.results = [];
        }
        $scope.resultCount = $scope.results.length;
        console.log($scope.results);
    });


    $scope.$on(EVENTS.QUESTIONS_RECEIVED, function() {
        let questions = DataService.getQuestions();
        if (questions instanceof Array) {
            $scope.questions = questions;
        } else {
            $scope.questions = [questions];
        }
        $scope.results = "";
        if (!questions || (questions.length == 1 && questions[0] == "")) {
            $scope.questions = [];
        }
        $scope.resultCount = $scope.questions.length;
        console.log($scope.questions);
    });
}

export default ['$scope', 'EVENTS', 'DataService', SearchController];