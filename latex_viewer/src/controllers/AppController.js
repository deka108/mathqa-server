function AppController($scope, $mdSidenav, $window, EVENTS, LoginService) {
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

    $scope.toggleNav = function() {
        $mdSidenav("leftNav").toggle();
    }

    $scope.pages = {
        "Data Editor": "data_editor.html",
        "Data Viewer": "data_viewer.html",
        "Formula Viewer": "formula_viewer.html",
        "Formula Search": "index.html",
        "Create New Formula": "insert_formula.html",
        "Question Search": "question_search_viewer.html",
    }

    $scope.goToPage = function(page) {
        $window.location.href = "/" + page;
    }


}

export default ['$scope', '$mdSidenav', '$window', 'EVENTS', 'LoginService', AppController];