function LatexTableController($scope, $mdDialog, $mdEditDialog, $window, FormulaDataService, EVENTS) {
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

    $scope.$on(EVENTS.FORMULA_UPDATED, function() {
        console.log("Formula updated!");
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

    $scope.showMathmlDialog = function(evt, formula) {
        _setLatexStr(formula.content);
        _setDialogEvent(evt);
        FormulaDataService.retrieveMathml(formula.content);
    }

    $scope.filterByCategory = function(formula) {
        if (!$scope.selectedCategories || $scope.selectedCategories.indexOf("all") != -1) {
            return true;
        } else {
            for (let i = 0; i < formula.categories.length; i++) {
                if ($scope.selectedCategories.indexOf(formula.categories[i]) != -1) return true;
            }
        }
        return false;
    }

    $scope.changePage = function(page, limit) {
        console.log(page, limit);
    }

    $scope.updateResults = function() {
        $scope.limitOptions = [50, 100, $scope.results.length];
    }

}

export default ['$scope', '$mdDialog', '$mdEditDialog', '$window', 'FormulaDataService', 'EVENTS', LatexTableController];