// Load libraries
import angular from 'angular';

import 'angular-messages';
import 'angular-animate';
import 'angular-aria';
import 'angular-material';
import 'angular-katex';

import AppController from 'src/controllers/AppController';
import LatexFormController from 'src/controllers/LatexFormController';
import QuestionDataService from 'src/services/QuestionDataService';
import FormulaDataService from 'src/services/FormulaDataService';
import EVENTS from 'src/constants/EVENTS';
import URL from 'src/constants/URL';

export default angular.module('viewer-app', ['ngMaterial', 'katex', 'ngMessages'])
    .config(($mdThemingProvider) => {
        $mdThemingProvider.theme('default')
            .primaryPalette('blue')
            .accentPalette('pink');
    })
    .constant('URL', URL)
    .constant('EVENTS', EVENTS)
    .controller('LatexFormController', LatexFormController)
    .controller('AppController', AppController)
    .service('QuestionDataService', QuestionDataService)
    .service('FormulaDataService', FormulaDataService);