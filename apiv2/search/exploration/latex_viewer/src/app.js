// Load libraries
import angular from 'angular';

import 'angular-animate';
import 'angular-aria';
import 'angular-material';
import 'angular-katex';

import AppController from 'src/controllers/AppController';
import LatexInputController from 'src/controllers/LatexInputController';
import QuestionDataService from 'src/services/QuestionDataService';
import EVENTS from 'src/constants/EVENTS';
import URL from 'src/constants/URL';

export default angular.module('viewer-app', ['ngMaterial', 'katex'])
    .config(($mdThemingProvider) => {
        $mdThemingProvider.theme('default')
            .primaryPalette('blue')
            .accentPalette('pink');
    })
    .directive("mathjaxBind", function() {
        return {
            restrict: "A",
            controller: ["$scope", "$element", "$attrs",
                function($scope, $element, $attrs) {
                    $scope.$watch($attrs.mathjaxBind, function(texExpression) {
                        $element.html(texExpression);
                        MathJax.Hub.Queue(["Typeset", MathJax.Hub, $element[0]]);
                    });
                }
            ]
        };
    })
    .constant('URL', URL)
    .constant('EVENTS', EVENTS)
    .controller('LatexInputController', LatexInputController)
    .controller('AppController', AppController)
    .service('QuestionDataService', QuestionDataService);