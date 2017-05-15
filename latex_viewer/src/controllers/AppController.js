function AppController($scope, $mdSidenav, $window, $mdDialog, EVENTS, LoginService) {
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
        "Formula Search": "index.html",
        "Question Search": "question_search_viewer.html",
        "Data Editor": "data_editor.html",
        "Data Viewer": "data_viewer.html",
        "Formula Viewer": "formula_viewer.html",
        "Create New Formula": "insert_formula.html",
        "Formula Result Viewer": "formula_result_viewer.html"
    }

    $scope.goToPage = function(page) {
        $window.location.href = "/" + page;
    }

    $scope.showLoginPrompt = function() {
        $mdDialog.show({
                controller: LoginDialogController,
                templateUrl: 'login_dialog.html',
                parent: angular.element(document.body),
                scope: $scope, // use parent scope in template
                preserveScope: true,
                clickOutsideToClose: true,
            })
            .then(function() {
                $scope.login();
            }, function() {
                console.log("Login cancelled");
            });

        function LoginDialogController($scope, $mdDialog) {
            $scope.hide = function() {
                $mdDialog.hide();
            };

            $scope.cancel = function() {
                $mdDialog.cancel();
            };

            $scope.submitLogin = function() {
                $mdDialog.hide();
            };
        }
    }

    $scope.showLoginAlert = function() {
        $mdDialog.show(
            $mdDialog.alert()
            .parent(angular.element(document.body))
            .clickOutsideToClose(true)
            .title('Authentication Error')
            .textContent('Please login first before performing any database manipulation!')
            .ok('Okay')
        );
    };


}

export default ['$scope', '$mdSidenav', '$window', '$mdDialog', 'EVENTS', 'LoginService', AppController];