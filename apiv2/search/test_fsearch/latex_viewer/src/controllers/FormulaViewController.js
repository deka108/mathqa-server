function FormulaViewController($scope, FormulaDataService, EVENTS) {
    FormulaDataService.getFormulaCategories();
}

export default ['$scope', 'FormulaDataService', 'EVENTS', FormulaViewController];