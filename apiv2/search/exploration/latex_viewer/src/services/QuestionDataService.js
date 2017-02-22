function QuestionDataService($http, $rootScope, URL, EVENTS) {
    function _on_data_received(data) {
        $rootScope.$broadcast(EVENTS.DATA_RECEIVED, data);
    }

    this.retrieveData = function(path) {
        return $http.get(URL.TEST_QUESTION)
            .then(function success(response) {
                _on_data_received(response.data);
                // _update_data();
            }, function error(response) {
                if (response.status > 0) {
                    console.error(response);
                }
            })
    }

}

export default ['$http', '$rootScope', 'URL', 'EVENTS', QuestionDataService];