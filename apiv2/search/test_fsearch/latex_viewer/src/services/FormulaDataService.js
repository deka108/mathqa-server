function FormulaDataService($http, $rootScope, LoginService, URL, EVENTS) {
    function _on_mathml_received() {
        $rootScope.$broadcast(EVENTS.MATHML_RECEIVED);
    }

    function _on_formula_categories_received() {
        $rootScope.$broadcast(EVENTS.FORMULA_CATEGORIES_RECEIVED);
    }

    function _on_formula_received() {
        $rootScope.$broadcast(EVENTS.FORMULA_RECEIVED);
    }

    function _on_formula_created() {
        $rootScope.$broadcast(EVENTS.FORMULA_CREATED);
    }

    function _on_formula_updated() {
        $rootScope.$broadcast(EVENTS.FORMULA_UPDATED);
    }

    function _on_formula_deleted() {
        $rootScope.$broadcast(EVENTS.FORMULA_DELETED);
    }

    function _on_error(response) {
        if (response.status > 0) {
            console.error(response);
        }
    }

    function _update_formula_categories(newData) {
        formulaCategories = newData;
    }

    function _update_formulas(newData) {
        formulas = newData;
    }

    function _update_mathml_formula(newData) {
        formulaMathml = newData;
    }

    let formulaMathml = null;
    let formulaCategories = null;
    let formulas = null;

    this.getFormulaCategories = function() {
        return formulaCategories;
    }

    this.getMathmlFormula = function() {
        return formulaMathml;
    }

    this.getFormulas = function() {
        return formulas;
    }

    this.retrieveFormulaCategories = function() {
        if (formulaCategories) { _on_formula_categories_received(); }
        return $http.get(URL.GET_FORMULA_CATEGORIES).then(
            function success(response) {
                _update_formula_categories(response.data);
                _on_formula_categories_received();
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
                    _update_mathml_formula(response.data);
                    _on_mathml_received();
                },
                function error(response) {
                    _on_error(response);
                });
    }

    this.retrieveFormulas = function() {
        return $http.get(URL.GET_TEST_FORMULAS).then(
            function success(response) {
                _update_formulas(response.data);
                _on_formula_received();
            },
            function error(response) {
                _on_error(response);
            });
    }

    this.createFormula = function(data) {
        let formulaData = {
            "formula": data,
            "username": "admin",
            "password": "123456"
        }
        return $http.post(URL.CUD_TEST_FORMULA, JSON.stringify(formulaData))
            .then(function success(response) {
                console.log(response);
                _on_formula_created();
            }, function error(response) {
                _on_error(response);
            });
    }

    this.updateFormula = function(data) {
        let formulaData = {
            "formula": data,
            "username": "admin",
            "password": "123456"
        }
        return $http.patch(URL.CUD_TEST_FORMULA, JSON.stringify(formulaData))
            .then(function success(response) {
                console.log(response);
                _on_formula_updated();
            }, function error(response) {
                _on_error(response);
            });
    }

    this.deleteFormula = function(data) {
        let formulaData = {
            "formula": data,
            "username": "admin",
            "password": "123456"
        }
        return $http.delete(URL.CUD_TEST_FORMULA, JSON.stringify(formulaData))
            .then(function success(response) {
                console.log(response);
                _on_formula_deleted();
            }, function error(response) {
                _on_error(response);
            });
    }

    this.reindexFormula = function(data) {
        let postData = {
            "username": "admin",
            "password": "123456",
            "formulas": data.formulas,
            "reset": true
        }
        return $http({
            method: 'POST',
            url: URL.REINDEX_TEST_FORMULA,
            data: JSON.stringify(postData),
            headers: data.headers
        }).then(function success(response) {
                console.log(response)
            },
            function error(response) {
                _on_error(response);
            });
    }
}

export default ['$http', '$rootScope', 'LoginService', 'URL', 'EVENTS', FormulaDataService];