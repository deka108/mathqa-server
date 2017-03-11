function AppController($scope, EVENTS, LoginService) {
    $scope.isLogin = false;
    $scope.userData = {
        'username': 'dekauliya',
        'password': '123456'
    };

    $scope.$on(EVENTS.LOGIN, function() {
        $scope.isLogin = true;
    });

    $scope.$on(EVENTS.LOGOUT, function() {
        $scope.isLogin = false;
    });

    $scope.login = function() {
        LoginService.login();
    };

    $scope.logout = function() {
        LoginService.logout();
        $scope.isLogin = false;
    };


}

export default ['$scope', 'EVENTS', 'LoginService', AppController];