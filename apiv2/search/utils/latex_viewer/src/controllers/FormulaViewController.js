function FormulaViewController($scope, $mdDialog, $mdEditDialog, $window, FormulaDataService, LoginService, EVENTS) {
    $scope.pageTitle = "Formula Viewer";
    $scope.promise = FormulaDataService.retrieveFormulas();

    $scope.$on(EVENTS.FORMULA_RECEIVED, function() {
        $scope.formulas = FormulaDataService.getFormulas();
    });


    $scope.$on(EVENTS.FORMULA_UPDATED, function() {
        console.log("Formula updated!");
    });

    $scope.$on(EVENTS.FORMULA_DELETED, function() {
        console.log("Formula deleted!");
        $scope.refreshData();
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
        FormulaDataService.updateFormula(formula);
        console.log(formula);
    }

    $scope.deleteFormula = function(formula) {
        FormulaDataService.deleteFormula(formula);
        console.log(formula);
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

    $scope.reindexFormula = function(someFormulas) {
        if (LoginService.getToken()) {
            let data = {
                headers: LoginService.getTokenHeader(),
            }

            // if (!someFormulas) {
            //     data.formulas = null;
            // } else {
            //     if (someFormulas instanceof Array) {
            //         data.formulas = someFormulas;
            //     } else {
            //         data.formulas = [someFormulas];
            //     }
            // }

            FormulaDataService.reindexFormula(data);
        } else {
            console.error("Need to login first!!");
        }
    }
}

export default ['$scope', '$mdDialog', '$mdEditDialog', '$window', 'FormulaDataService', 'LoginService', 'EVENTS', FormulaViewController];