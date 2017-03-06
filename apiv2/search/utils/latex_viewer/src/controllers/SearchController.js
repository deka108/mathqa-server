function SearchController($scope, EVENTS, FormulaDataService) {
    $scope.pageTitle = "Search View";

    $scope.searchFormula = function(query) {
        FormulaDataService.searchFormula(query);
    }

    $scope.$on(EVENTS.SEARCH_RECEIVED, function() {
        $scope.formulas = FormulaDataService.getFormulaResults();
    });
}

export default ['$scope', 'EVENTS', 'FormulaDataService', SearchController];