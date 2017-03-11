function FormulaDataService($http, $rootScope, URL, EVENTS) {
    function _on_login() {
        $rootScope.$broadcast(EVENTS.LOGIN);
    }

    function _on_logout() {
        _set_token(null);
        $rootScope.$broadcast(EVENTS.LOGOUT);
    }

    function _on_error(response) {
        if (response.status > 0) {
            console.error(response);
        }
    }

    function _set_token(newToken) {
        token = newToken;
    }

    function _get_token_header() {
        return "Authorization: Token " + token.auth_token;
    }

    let token = null;

    this.getToken = function() {
        return token;
    }

    this.getTokenHeader = function() {
        return {
            'Authorization': ' Token ' + token.auth_token
        }
    }


    this.logout = function() {
        return $http({
            method: 'POST',
            url: URL.LOGOUT,
            headers: this.getTokenHeader()
        }).then(function success(response) {
            console.log(response);
            _on_logout();
        }, function error(response) {
            console.error(response);
        })
    }

    this.login = function() {
        let userData = {
            "username": "dekauliya",
            "password": "123456"
        }
        return $http.post(URL.LOGIN, JSON.stringify(userData))
            .then(function success(response) {
                _set_token(response.data);
                _on_login();
            }, function error(response) {
                _on_error(response);
            });
    }
}

export default ['$http', '$rootScope', 'URL', 'EVENTS', FormulaDataService];