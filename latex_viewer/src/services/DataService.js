function DataService($http, $rootScope, URL, EVENTS) {
    function _on_data_received() {
        $rootScope.$broadcast(EVENTS.DATA_RECEIVED);
    }

    function _on_data_updated() {
        $rootScope.$broadcast(EVENTS.DATA_UPDATED);
    }

    function _on_datas_received() {
        $rootScope.$broadcast(EVENTS.DATAS_RECEIVED);
    }

    function _on_questions_received() {
        $rootScope.$broadcast(EVENTS.QUESTIONS_RECEIVED);
    }

    function _on_search_received() {
        $rootScope.$broadcast(EVENTS.SEARCH_RECEIVED);
    }

    function _update_result(newData) {
        results = newData;
    }

    function _update_datas(newData) {
        datas = newData;
    }

    function _update_questions(newData) {
        questions = newData;
    }

    function _update_data(newData) {
        data = newData;
    }

    function _update_updated_data(newData) {
        updatedData = newData;
    }

    function _on_error(response) {
        if (response.status > 0) {
            console.error(response);
        }
    }

    this.getSearchResults = function() {
        return results;
    }

    this.getQuestions = function() {
        return questions;
    }

    this.getDatas = function() {
        return datas;
    }

    this.getData = function() {
        return data;
    }

    this.getUpdatedData = function() {
        return updatedData;
    }

    let results = null;
    let solutions = null;
    let questions = null;
    let data = null;
    let updatedData = null;
    let datas = null;

    this.retrieveSolution = function(id) {
        return $http.get(URL.GET_SOLUTIONS + id)
            .then(function success(response) {
                _update_data(response.data);
                _on_data_received();
            }, function error(response) {
                _on_error(response)
            });
    }

    this.retrieveQuestion = function(id) {
        return $http.get(URL.GET_QUESTIONS + id)
            .then(function success(response) {
                _update_data(response.data);
                _on_data_received();
            }, function error(response) {
                _on_error(response)
            });
    }

    this.retrieveKeypoint = function(id) {
        return $http.get(URL.GET_KEYPOINTS + id)
            .then(function success(response) {
                _update_data(response.data);
                _on_data_received();
            }, function error(response) {
                _on_error(response)
            });
    }

    this.retrieveSolutions = function() {
        return $http.get(URL.GET_SOLUTIONS)
            .then(function success(response) {
                _update_datas(response.data);
                _on_datas_received();
            }, function error(response) {
                _on_error(response)
            });
    }

    this.retrieveQuestions = function() {
        return $http.get(URL.GET_QUESTIONS)
            .then(function success(response) {
                _update_datas(response.data);
                _on_datas_received();
            }, function error(response) {
                _on_error(response)
            });
    }

    this.retrieveKeypoints = function() {
        return $http.get(URL.GET_KEYPOINTS)
            .then(function success(response) {
                _update_datas(response.data);
                _on_datas_received();
            }, function error(response) {
                _on_error(response)
            });
    }

    this.searchQuestions = function(query) {
        return $http.get(URL.GET_QUESTIONS + query)
            .then(function success(response) {
                _update_questions(response.data);
                _on_questions_received();
            }, function error(response) {
                _on_error(response)
            });
    }

    this.searchFormula = function(query) {
        return $http.get(URL.SEARCH_FORMULA + encodeURIComponent(query))
            .then(function success(response) {
                _update_result(response.data);
                _on_search_received();
            }, function error(response) {
                _on_error(response)
            });
    }

    this.fullTextSearch = function(query) {
        return $http.get(URL.SEARCH_FULL_TEXT + encodeURIComponent(query))
            .then(function success(response) {
                _update_result(response.data);
                _on_search_received();
            }, function error(response) {
                if (response.status > 0) {
                    console.error(response);
                }
            })
    }

    this.exactSearchDb = function(query) {
        return $http.get(URL.SEARCH_DB + encodeURIComponent(query))
            .then(function success(response) {
                _update_result(response.data);
                _on_search_received();
            }, function error(response) {
                if (response.status > 0) {
                    console.error(response);
                }
            })
    }

    this.updateQuestion = function(data, tokenHeader) {
        let questionData = {
            "question": data,
            "username": "admin",
            "password": "123456"
        }

        return $http({
                method: 'PATCH',
                url: URL.UPDATE_QUESTION,
                data: JSON.stringify(questionData),
                headers: tokenHeader
            })
            .then(function success(response) {
                _update_updated_data(response.data);
                console.log("Question is successfully updated");
                _on_data_updated();
            }, function error(response) {
                _on_error(response);
            });
    }

    this.updateSolution = function(data, tokenHeader) {
        let solutionData = {
            "solution": data,
            "username": "admin",
            "password": "123456"
        }

        return $http({
                method: 'PATCH',
                url: URL.UPDATE_SOLUTION,
                data: JSON.stringify(solutionData),
                headers: tokenHeader
            })
            .then(function success(response) {
                _update_updated_data(response.data);
                console.log("Solution is successfully updated");
                _on_data_updated();
            }, function error(response) {
                _on_error(response);
            });
    }

    this.updateKeypoint = function(data, tokenHeader) {
        let keypointData = {
            "keypoint": data,
            "username": "admin",
            "password": "123456"
        }

        return $http({
                method: 'PATCH',
                url: URL.UPDATE_KEYPOINT,
                data: JSON.stringify(keypointData),
                headers: tokenHeader
            })
            .then(function success(response) {
                _update_updated_data(response.data);
                console.log("Keypoint is successfully updated");
                _on_data_updated();
            }, function error(response) {
                _on_error(response);
            });
    }

}

export default ['$http', '$rootScope', 'URL', 'EVENTS', DataService];