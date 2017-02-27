function LatexFormController($scope, $mdDialog, FormulaDataService, EVENTS) {
    $scope.pageTitle = "Formula Editor";
    FormulaDataService.retrieveFormulaCategories();

    function DialogController($scope, $mdDialog) {
        $scope.hide = function() {
            $mdDialog.hide();
        };

        $scope.cancel = function() {
            $mdDialog.cancel();
        };

        $scope.confirm = function() {
            $mdDialog.hide();
            FormulaDataService.createFormula({
                'content': $scope.formulaData.rawLatex,
                'categories': $scope.formulaData.selectedCategories,
                'questions': $scope.formulaData.questionId
            });
            $scope.resetForm();
        };
    }

    $scope.$on(EVENTS.MATHML_RECEIVED, function() {
        $scope.formulaData.mathmlStr = FormulaDataService.getMathmlFormula();
        console.log($scope.formulaData.mathmlStr);
        $scope.showDialog($scope.event);
    });

    $scope.$on(EVENTS.FORMULA_CATEGORIES_RECEIVED, function() {
        $scope.formulaCategories = FormulaDataService.getFormulaCategories();
    });

    $scope.formulaData = {};

    $scope.checkMathml = function(evt) {
        FormulaDataService.retrieveMathml($scope.formulaData.rawLatex);
        $scope.formulaData.latexStr = '$$' + $scope.formulaData.rawLatex + '$$';
        $scope.event = evt;
    }

    $scope.showDialog = function(evt) {
        $mdDialog.show({
                controller: DialogController,
                templateUrl: 'latex_preview_dialog.html',
                parent: angular.element(document.body),
                scope: $scope,
                targetEvent: evt,
                preserveScope: true,
                clickOutsideToClose: true,
                fullscreen: true
            })
            .then(function() {
                console.log("Submitted post request");
            }, function() {
                console.log("Cancelled post request");
            });
    };

    $scope.resetForm = function() {
        $scope.formulaEditor.$setPristine();
        $scope.formulaEditor.$setUntouched();
        $scope.formulaData = {};
    }
}

export default ['$scope', '$mdDialog', 'FormulaDataService', 'EVENTS', LatexFormController];