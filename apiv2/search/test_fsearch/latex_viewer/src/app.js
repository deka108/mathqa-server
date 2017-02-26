// Load libraries
import angular from 'angular';

import 'angular-messages';
import 'angular-animate';
import 'angular-aria';
import 'angular-filter';
import 'angular-katex';
import 'angular-material';
import 'angular-material-data-table';

import AppController from 'src/controllers/AppController';
import LatexFormController from 'src/controllers/LatexFormController';
import FormulaViewController from 'src/controllers/FormulaViewController';
import QuestionDataService from 'src/services/QuestionDataService';
import FormulaDataService from 'src/services/FormulaDataService';
import EVENTS from 'src/constants/EVENTS';
import URL from 'src/constants/URL';

export default angular.module('viewer-app', ['ngMaterial', 'katex', 'ngMessages', 'md.data.table', 'angular.filter'])
    .config(($mdThemingProvider) => {
        $mdThemingProvider.theme('default')
            .primaryPalette('blue')
            .accentPalette('pink');
    })
    .constant('URL', URL)
    .constant('EVENTS', EVENTS)
    .controller('FormulaViewController', FormulaViewController)
    .controller('LatexFormController', LatexFormController)
    .controller('AppController', AppController)
    .service('QuestionDataService', QuestionDataService)
    .service('FormulaDataService', FormulaDataService);