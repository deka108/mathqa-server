// Load libraries
import angular from 'angular';

import 'angular-cookie';
import 'angular-messages';
import 'angular-animate';
import 'angular-aria';
import 'angular-filter';
import 'katex';
import 'angular-katex';
import 'angular-material';
import 'angular-material-data-table';

import AppController from 'src/controllers/AppController';
import FormulaViewController from 'src/controllers/FormulaViewController';
import LatexFormController from 'src/controllers/LatexFormController';
import LoginController from 'src/controllers/LoginController';
import SearchController from 'src/controllers/SearchController';
import LatexTableController from 'src/controllers/LatexTableController';
import FormulaDataService from 'src/services/FormulaDataService';
import LoginService from 'src/services/LoginService';
import QuestionDataService from 'src/services/QuestionDataService';
import EVENTS from 'src/constants/EVENTS';
import URL from 'src/constants/URL';

export default angular.module('viewer-app', ['ngMaterial', 'katex', 'ngMessages', 'md.data.table'])
    .config(($mdThemingProvider) => {
        $mdThemingProvider.theme('default')
            .primaryPalette('blue')
            .accentPalette('pink');
    })
    .config(($httpProvider) => {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    })
    .constant('URL', URL)
    .constant('EVENTS', EVENTS)
    .controller('AppController', AppController)
    .controller('FormulaViewController', FormulaViewController)
    .controller('LatexFormController', LatexFormController)
    .controller('LoginController', LoginController)
    .controller('LatexTableController', LatexTableController)
    .controller('SearchController', SearchController)
    .service('QuestionDataService', QuestionDataService)
    .service('FormulaDataService', FormulaDataService)
    .service('LoginService', LoginService);