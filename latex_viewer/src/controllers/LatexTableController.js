function LatexTableController($scope, $mdDialog, $mdEditDialog, $window, FormulaDataService, EVENTS) {
    $scope.pageTitle = "Formula Search";

    function _setLatexStr(newLatex) {
        $scope.latexStr = "$$" + newLatex + "$$";
    }

    function _setMathmlStr(newMathml) {
        $scope.mathmlStr = newMathml;
    }

    function _setDialogEvent(newEvent) {
        $scope.dialogEvent = newEvent;
    }

    $scope.latexStr = null;
    $scope.mathmlStr = null;
    $scope.dialogEvent = null;
    FormulaDataService.retrieveFormulaCategories();

    $scope.$on(EVENTS.FORMULA_CATEGORIES_RECEIVED, function() {
        $scope.formulaCategories = FormulaDataService.getFormulaCategories();
    });

    $scope.$on(EVENTS.MATHML_RECEIVED, function() {
        _setMathmlStr(FormulaDataService.getMathmlFormula());
        let parentEl = document.getElementById("body");
        $mdDialog.show({
            contentElement: '#mathmlDialog',
            parent: angular.element(document.body),
            targetEvent: $scope.dialogEvent,
            clickOutsideToClose: true
        });
    });

    $scope.query = {
        order: 'questions',
        limit: 100,
        page: 1
    };

    $scope.limitOptions = [50, 100];

    $scope.updateResults = function() {
        $scope.limitOptions = [50, 100, $scope.results.length];
        console.log($scope.selectedCategories);
    }

    $scope.filterByCategory = function(formula) {
        if (!$scope.selectedCategories || $scope.selectedCategories.indexOf("all") != -1) {
            return true;
        } else {
            for (let i = 0; i < $scope.selectedCategories.length; i++) {
                if (formula.categories.indexOf($scope.selectedCategories[i]) == -1) {
                    return false;
                }
            }
        }
        return true;
    }

    $scope.showMathmlDialog = function(evt, formula) {
        _setLatexStr(formula.content);
        _setDialogEvent(evt);
        FormulaDataService.retrieveMathml(formula.content);
    }

    $scope.changePage = function(page, limit) {
        console.log(page, limit);
    }

    $scope.searchFormula = function(query) {
        $scope.promise = FormulaDataService.searchFormula(query);
    }

    $scope.scores = {
        p5: 0.8,
        p10: 0.4,
        ap5: 1,
        ap10: 1
    }

    $scope.$on(EVENTS.FORMULA_SEARCH_RECEIVED, function() {
        let results = FormulaDataService.getFormulaResults();
        let formulas = [];
        let rel_labels = [1, 1, 1, 1, "0", "0", "0", "0", "0", "0"];
        let ap_scores = [1, 1, 1, 1, 0.8, 0.67, 0.57, 0.5, 0.44, 0.4];
        for (let i = 0; i < results.length; i++) {
            formulas.push(results[i].rel_formula);
            formulas[i].rel_label = rel_labels[i];
            formulas[i].ap_score = ap_scores[i];
        }
        $scope.formulas = formulas;
        console.log($scope.formulas);
    });


    $scope.reactClick = function(evt) {
        console.log("CLICK");
        // evt.stopPropagation();
    }

    $scope.editRelevance = function(evt, formula) {
        evt.stopPropagation();
        console.log("edit relevance!");
        $mdEditDialog.small({
            modelValue: formula.rel_label,
            placeholder: 'Add a relevance',
            save: function(input) {
                formula.rel_label = input.$modelValue;
            },
            title: 'Add/Edit content',
            targetEvent: evt,
        });
    }

    $scope.editApScore = function(evt, formula) {
        evt.stopPropagation();
        console.log("edit ap score!");
        $mdEditDialog.small({
            modelValue: formula.ap_score,
            placeholder: 'Add a AP score',
            save: function(input) {
                formula.ap_score = input.$modelValue;
            },
            title: 'Add/Edit questions',
            targetEvent: evt,
        });
    }


}

export default ['$scope', '$mdDialog', '$mdEditDialog', '$window', 'FormulaDataService', 'EVENTS', LatexTableController];