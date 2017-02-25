function LatexFormController($scope, $mdDialog, FormulaDataService, EVENTS) {
    FormulaDataService.getFormulaCategories();
    let formElement = document.getElementById('formulaEditor');

    $scope.formulaData = {};

    $scope.checkMathml = function() {
        FormulaDataService.retrieveMathml($scope.formulaData.rawLatex);
        $scope.formulaData.latexStr = '$$' + $scope.formulaData.rawLatex + '$$';
    }

    $scope.$on(EVENTS.MATHML_RECEIVED, function(evt, data) {
        $scope.formulaData.mathmlStr = data;
        console.log(data);
        $scope.showDialog();
    });

    $scope.$on(EVENTS.FORMULA_CATEGORIES_RECEIVED, function(evt, data) {
        $scope.formulaCategories = data;
    });

    $scope.showDialog = function() {
        $mdDialog.show({
                controller: DialogController,
                templateUrl: 'latex_preview_dialog.html',
                parent: angular.element(formElement),
                scope: $scope,
                preserveScope: true,
                clickOutsideToClose: true,
                fullscreen: true
            })
            .then(function() {
                console.log("Submitted");
            });
    };

    function DialogController($scope, $mdDialog) {
        $scope.cancel = function() {
            $mdDialog.cancel();
        };

        $scope.confirm = function() {
            $mdDialog.hide();
            FormulaDataService.postFormula({
                'content': $scope.formulaData.rawLatex,
                'categories': $scope.formulaData.selectedCategories,
                'questions': $scope.formulaData.questions
            });
            $scope.resetForm();
        };
    }

    $scope.resetForm = function() {
        $scope.formulaEditor.$setPristine();
        $scope.formulaEditor.$setUntouched();
        $scope.formulaData = {};
    }
}

export default ['$scope', '$mdDialog', 'FormulaDataService', 'EVENTS', LatexFormController];