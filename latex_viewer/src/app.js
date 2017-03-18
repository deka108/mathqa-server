// Load libraries
import angular from 'angular';

import 'angular-cookie';
import 'angular-messages';
import 'angular-animate';
import 'angular-aria';
import 'angular-filter';
import 'angular-loading-bar';
import 'katex';
import 'angular-katex';
import 'angular-material';
import 'angular-material-data-table';

import AppController from 'src/controllers/AppController';
import DataEditController from 'src/controllers/DataEditController';
import DataViewController from 'src/controllers/DataViewController';
import FormulaViewController from 'src/controllers/FormulaViewController';
import LatexFormController from 'src/controllers/LatexFormController';
import LatexTableController from 'src/controllers/LatexTableController';
import LoginController from 'src/controllers/LoginController';
import QuestionViewController from 'src/controllers/QuestionViewController';
import SearchController from 'src/controllers/SearchController';

import FormulaDataService from 'src/services/FormulaDataService';
import LoginService from 'src/services/LoginService';
import DataService from 'src/services/DataService';

import FORMULAS from 'src/constants/FORMULAS';
import EVENTS from 'src/constants/EVENTS';
import URL from 'src/constants/URL';

export default angular.module('viewer-app', ['ngMaterial', 'katex', 'ngMessages', 'md.data.table', 'angular-loading-bar', 'ngAnimate'])
    .config(($mdThemingProvider) => {
        $mdThemingProvider.theme('default')
            .primaryPalette('blue')
            .accentPalette('pink');
    })
    .config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
        cfpLoadingBarProvider.parentSelector = '#loading-bar-container';
        cfpLoadingBarProvider.spinnerTemplate = '<div><span class="fa fa-spinner">Loading...</div>';
    }])
    .config(($httpProvider) => {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    })
    .config((katexConfigProvider) => {
        console.log(katexConfigProvider);
        katexConfigProvider.defaultOptions = {
            delimiters: [
                { left: "$$", right: "$$", display: false },
                { left: "\\[", right: "\\]", display: true },
                { left: "\\(", right: "\\)", display: false }
            ]
        }
    })
    .constant('URL', URL)
    .constant('EVENTS', EVENTS)
    .constant('FORMULAS', FORMULAS)
    .controller('AppController', AppController)
    .controller('DataEditController', DataEditController)
    .controller('DataViewController', DataViewController)
    .controller('FormulaViewController', FormulaViewController)
    .controller('LatexFormController', LatexFormController)
    .controller('LatexTableController', LatexTableController)
    .controller('LoginController', LoginController)
    .controller('QuestionViewController', QuestionViewController)
    .controller('SearchController', SearchController)
    .service('DataService', DataService)
    .service('FormulaDataService', FormulaDataService)
    .service('LoginService', LoginService);