/**
 * Created by iggor on 01/08/2017.
 */
angular.module('inGaiaApp', ['ngMaterial', 'ui.router'])
    .config(function ($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise('/home/0');

        $stateProvider
            .state('home', {
                url: '/home/{page}',
                templateUrl: 'static/views/partial-home.html',
                controller: 'HomeController'
            })
            .state('log', {
                url: '/log/{id}/{page}',
                templateUrl: 'static/views/partial-realty-log.html',
                controller: 'LogController'
            })
            .state('detail', {
                url: '/detail/{id}',
                templateUrl: 'static/views/partial-detail.html',
                controller: 'DetailController'
            })
    });