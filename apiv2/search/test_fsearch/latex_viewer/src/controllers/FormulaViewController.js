function FormulaViewController($scope, $mdDialog, $mdEditDialog, FormulaDataService, EVENTS) {
    function _setLatexStr(newLatex) {
        $scope.latexStr = "$$" + newLatex + "$$";
    }

    function _setMathmlStr(newMathml) {
        $scope.mathmlStr = newMathml;
    }

    function _setDialogEvent(newEvent) {
        $scope.dialogEvent = newEvent;
    }

    FormulaDataService.retrieveFormulaCategories();
    $scope.promise = FormulaDataService.retrieveFormulas();
    $scope.latexStr = null;
    $scope.mathmlStr = null;
    $scope.dialogEvent = null;

    $scope.$on(EVENTS.FORMULA_RECEIVED, function() {
        $scope.formulas = FormulaDataService.getFormulas();
    });

    $scope.$on(EVENTS.FORMULA_CATEGORIES_RECEIVED, function() {
        $scope.formulaCategories = FormulaDataService.getFormulaCategories();
    });

    $scope.$on(EVENTS.FORMULA_UPDATED, function() {
        console.log("Formula updated!");
    });

    $scope.$on(EVENTS.MATHML_RECEIVED, function() {
        _setMathmlStr(FormulaDataService.getMathmlFormula());
        $mdDialog.show({
            contentElement: '#mathmlDialog',
            parent: angular.element(document.body),
            targetEvent: $scope.dialogEvent,
            clickOutsideToClose: true
        });
    });

    $scope.query = {
        order: 'questions'
    };

    $scope.editContent = function(evt, formula) {
        evt.stopPropagation();
        $mdEditDialog.small({
            modelValue: formula.content,
            placeholder: 'Add a content',
            save: function(input) {
                formula.content = input.$modelValue;
            },
            title: 'Add/Edit content',
            targetEvent: evt,
        });
    }

    $scope.editQuestions = function(evt, formula) {
        evt.stopPropagation();

        $mdEditDialog.small({
            modelValue: formula.questions,
            placeholder: 'Add a question',
            save: function(input) {
                formula.questions = input.$modelValue;
            },
            title: 'Add/Edit questions',
            targetEvent: evt,
        });
    }

    $scope.updateFormula = function(formula) {
        FormulaDataService.updateFormula(formula);
        console.log(formula);
    }

    $scope.deleteFormula = function(formula) {
        FormulaDataService.deleteFormula(formula);
        console.log(formula);
    }

    $scope.refreshData = function() {
        $scope.promise = FormulaDataService.retrieveFormulas();
    }

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

}

export default ['$scope', '$mdDialog', '$mdEditDialog', 'FormulaDataService', 'EVENTS', FormulaViewController];