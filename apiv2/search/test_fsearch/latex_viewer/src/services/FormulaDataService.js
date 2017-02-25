function FormulaDataService($http, $rootScope, URL, EVENTS) {
    function _on_mathml_received(data) {
        $rootScope.$broadcast(EVENTS.MATHML_RECEIVED, data);
    }

    function _on_formula_categories_received(data) {
        $rootScope.$broadcast(EVENTS.FORMULA_CATEGORIES_RECEIVED, data);
    }

    function _update_formula_categories(newData) {
        formulaCategories = newData;
    }

    function _on_formula_posted() {
        $rootScope.$broadcast(EVENTS.ON_FORMULA_POSTED);
    }

    function _on_error(response) {
        if (response.status > 0) {
            console.error(response);
        }
    }

    var formulaCategories = null;

    this.getFormulaCategories = function() {
        if (formulaCategories) return formulaCategories;
        return $http.get(URL.GET_FORMULA_CATEGORIES).then(
            function success(response) {
                _on_formula_categories_received(response.data);
            },
            function error(response) {
                _on_error(response);
            });
    }

    this.retrieveMathml = function(data) {
        let formulaData = {
            "formula": data
        }
        return $http.post(URL.CHECK_MATHML, JSON.stringify(formulaData))
            .then(
                function success(response) {
                    _on_mathml_received(response.data);
                },
                function error(response) {
                    _on_error(response);
                });
    }

    this.getFormulas = function() {
        return $http.get(URL.GET_FORMULAS).then(
            function success(response) {
                _on_formula_received(response.data);
            },
            function error(response) {
                _on_error(response);
            });
    }

    this.postFormula = function(data) {
        let formulaData = {
            "formula": data,
            "username": "admin",
            "password": "123456"
        }
        console.log(formulaData);
        return $http.post(URL.POST_NEW_FORMULA, JSON.stringify(formulaData))
            .then(function success(response) {
                _on_formula_posted();
            }, function error(response) {
                _on_error(response);
            });
    }

}

export default ['$http', '$rootScope', 'URL', 'EVENTS', FormulaDataService];