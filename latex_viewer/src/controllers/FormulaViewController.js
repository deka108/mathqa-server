function FormulaViewController($scope, $mdDialog, $mdEditDialog, $window, FormulaDataService, LoginService,
    EVENTS) {
    $scope.pageTitle = "Formula Viewer";
    $scope.promise = FormulaDataService.retrieveFormulas();

    $scope.$on(EVENTS.FORMULA_RECEIVED, function() {
        $scope.formulas = FormulaDataService.getFormulas();
    });

    $scope.$on(EVENTS.FORMULA_CREATED, function() {
        console.log("Formula created!");
        $scope.promise = $scope.refreshData();
    })


    $scope.$on(EVENTS.FORMULA_UPDATED, function() {
        console.log("Formula updated!");
        if ($scope.currentUpdatedIdx > -1) {
            $scope.formulas[$scope.currentUpdatedIdx] = FormulaDataService.getUpdatedFormula();
            $scope.currentUpdatedIdx = -1;
        }
    });

    $scope.$on(EVENTS.FORMULA_DELETED, function() {
        console.log("Formula deleted!");
        $scope.promise = $scope.refreshData();
    });

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
        $scope.currentUpdatedIdx = $scope.formulas.indexOf(formula);
        FormulaDataService.updateFormula(formula);
    }

    $scope.deleteFormula = function(formula) {
        $scope.currentDeletedIdx = $scope.formulas.indexOf(formula);
        FormulaDataService.deleteFormula(formula);
    }

    $scope.refreshData = function() {
        $scope.promise = FormulaDataService.retrieveFormulas();
        FormulaDataService.retrieveFormulaCategories();
    }

    $scope.updateResults = function() {
        $scope.limitOptions = [50, 100, $scope.results.length];
    }

    $scope.openFormulaEditor = function() {
        $window.open('insert_formula.html', '_blank');
    }

    $scope.reindexFormula = function() {
        if (LoginService.getToken()) {
            let data = {
                headers: LoginService.getTokenHeader(),
            }

            FormulaDataService.reindexFormula(data);
        } else {
            console.error("Need to login first!!");
        }
    }
}

export default ['$scope', '$mdDialog', '$mdEditDialog', '$window', 'FormulaDataService', 'LoginService', 'EVENTS', FormulaViewController];