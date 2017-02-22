function LatexInputController($scope) {
    $scope.updateLatex = function() {
        $scope.latex_str = '$$' + $scope.raw_str + '$$';
    };

}

export default ['$scope', LatexInputController];