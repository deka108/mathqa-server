function LatexFormController($scope, $mdDialog, FormulaDataService, EVENTS, FORMULAS) {
    $scope.pageTitle = "Formula Editor";
    $scope.formulaData = {};
    FormulaDataService.retrieveFormulaCategories();

    $scope.$on(EVENTS.MATHML_RECEIVED, function() {
        $scope.formulaData.mathmlStr = FormulaDataService.getMathmlFormula();
        console.log($scope.formulaData.mathmlStr);
        $scope.showDialog($scope.event);
    });

    $scope.$on(EVENTS.FORMULA_CATEGORIES_RECEIVED, function() {
        $scope.formulaCategories = FormulaDataService.getFormulaCategories();
    });

    $scope.resetForm = function() {
        $scope.formulaEditor.$setPristine();
        $scope.formulaEditor.$setUntouched();
        $scope.formulaData = {};
    }

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

    $scope.resetSymbolDialog = function() {
        $scope.symbolData = {};
    }

    function _get_all_title() {
        let all_titles = {};
        FORMULAS.STRINGS_MAP['FORMULA_TITLE'].forEach(
            function(text) {
                all_titles[text] = FORMULAS.STRINGS[text];
            }
        );
        $scope.all_titles = all_titles;
    }

    $scope.updateSymbols = function() {
        let symbols = [];
        FORMULAS.STRINGS_MAP[$scope.symbolData.selectedTitle].forEach(
            function(text) {
                symbols.push({
                    "text": text,
                    "symbol": FORMULAS.STRINGS[text]
                });
            }
        )
        $scope.symbolData.symbols = symbols;
        console.log($scope.symbolData.symbols);
    }

    $scope.updateLatex = function(idx) {
        let regex = /^STR_(.*)_TITLE/;
        let selected = regex.exec($scope.symbolData.selectedTitle)[1];
        let latexKey = FORMULAS.STRINGS_MAP['FORMULA_' + selected][idx];
        $scope.symbolData.selectedSymbolLatex = FORMULAS.LATEX_SYMBOLS[latexKey];
    }

    function LatexSymbolDialogController($scope, $mdDialog) {
        $scope.hide = function() {
            $mdDialog.hide();
        };

        $scope.cancel = function() {
            $mdDialog.cancel();
        };

        $scope.confirm = function() {
            $mdDialog.hide();
            if (!$scope.formulaData.rawLatex) {
                $scope.formulaData.rawLatex = $scope.symbolData.selectedSymbolLatex;
            } else {
                let firstString = $scope.formulaData.rawLatex.substring(0, $scope.cursorPosition);
                let secondString = $scope.formulaData.rawLatex.substring($scope.cursorPosition);
                $scope.formulaData.rawLatex = firstString + $scope.symbolData.selectedSymbolLatex + secondString;
            }
            console.log($scope.formulaData.rawLatex);
        };
    }

    $scope.displayLatexDialog = function(evt) {
        if (!$scope.all_titles) {
            _get_all_title();
        }
        $scope.cursorPosition = document.getElementById("rawLatex").selectionEnd;
        $mdDialog.show({
                controller: LatexSymbolDialogController,
                templateUrl: 'latex_symbol_dialog.html',
                parent: angular.element(document.body),
                scope: $scope,
                targetEvent: evt,
                preserveScope: true,
                clickOutsideToClose: true,
                fullscreen: true
            })
            .then(function() {
                console.log("Entered a symbol");
                $scope.resetSymbolDialog();
            }, function() {
                console.log("Cancelled choosing a symbol");
            });
    }
}

export default ['$scope', '$mdDialog', 'FormulaDataService', 'EVENTS', 'FORMULAS', LatexFormController];