/**
 * Created by iggor on 01/08/2017.
 */
angular.module('inGaiaApp')
    .controller('IndexController', function ($scope, $state, $log, $stateParams, RealtyService) {
        // $scope.cities = [];

        $scope.searchTitle = function (query) {
            $state.go('search', {'query': query, 'page': 0, 'asc': 0});
        }

        // RealtyService.getRealtiesByCities().then(function (response) {
        //     if (response.statusText === 'OK') {
        //         $scope.cities = response.data.data;
        //     }
        // })
    })
    .controller('SearchController', function ($scope, $state, $log, $stateParams, RealtyService) {
        var page = parseInt($stateParams.page);
        var asc = parseInt($stateParams.asc);
        $scope.query = $stateParams.query;

        $scope.previousPage = page - 1;
        $scope.nextPage = page + 1;

        $scope.showPreviousButton = page > 0;
        $scope.showNextButton = false;

        $scope.asc = asc === 1;
        $scope.desc = !$scope.asc;

        $scope.toggleOrderBy = function () {
            $scope.asc = !$scope.asc;
            $scope.desc = !$scope.asc;

            $state.go('search', {'page': 0, 'asc': $scope.asc ? 1 : 0, 'query': $scope.query});
        }

        RealtyService.searchTitle($scope.query).then(function (response) {
            if (response.statusText === 'OK') {
                $scope.realties = response.data.data;
                $scope.showNextButton = page < response.data.count;
            }
        })
    })
    .controller('HomeController', function ($scope, $state, $log, $stateParams, RealtyService) {

        var page = parseInt($stateParams.page);
        var asc = parseInt($stateParams.asc);

        $scope.previousPage = page - 1;
        $scope.nextPage = page + 1;

        $scope.showPreviousButton = page > 0;
        $scope.showNextButton = false;

        $scope.asc = asc === 1;
        $scope.desc = !$scope.asc;

        $scope.toggleOrderBy = function () {
            $scope.asc = !$scope.asc;
            $scope.desc = !$scope.asc;

            $state.go('home', {'page': 0, 'asc': $scope.asc ? 1 : 0});
        }

        loadRealties();

        function loadRealties() {
            if ($scope.asc) {
                RealtyService.getRealtiesAsc(page).then(function (response) {
                    if (response.statusText === 'OK') {
                        $scope.realties = response.data.data;
                        $scope.showNextButton = page < response.data.count;
                    }
                });
            } else {
                RealtyService.getRealtiesDesc(page).then(function (response) {
                    if (response.statusText === 'OK') {
                        $scope.realties = response.data.data;
                        $scope.showNextButton = page < response.data.count;
                    }
                });
            }
        }
    })
    .controller('LogController', function ($scope, $state, $log, $stateParams, RealtyService) {

        var page = parseInt($stateParams.page);
        var id = $stateParams.id;
        var asc = parseInt($stateParams.asc);

        $scope.id = id;

        $scope.previousPage = page - 1;
        $scope.nextPage = page + 1;

        $scope.showPreviousButton = page > 0;
        $scope.showNextButton = false;

        $scope.asc = asc === 1;
        $scope.desc = !$scope.asc;

        $scope.toggleOrderBy = function () {
            $scope.asc = !$scope.asc;
            $scope.desc = !$scope.asc;

            $state.go('log', {'id': id, 'page': 0, 'asc': $scope.asc ? 1 : 0});
        }

        loadRealties();

        function loadRealties() {
            if (asc === 0) {
                RealtyService.getRealtyLogDesc(id, page).then(function (response) {
                    if (response.statusText === 'OK') {
                        $scope.realties = response.data.data;
                        $scope.showNextButton = page < response.data.count;
                    }
                });
            } else {
                RealtyService.getRealtyLogAsc(id, page).then(function (response) {
                    if (response.statusText === 'OK') {
                        $scope.realties = response.data.data;
                        $scope.showNextButton = page < response.data.count;
                    }
                });
            }
        }
    })
    .controller('DetailController', function ($scope, $log, $stateParams, RealtyService) {

        var id = $stateParams.id;

        loadRealty(id);

        function loadRealty() {
            RealtyService.getRealtyInfo(id).then(function (response) {
                if (response.statusText === 'OK') {
                    $scope.realty = response.data;
                }
            });
        }
    });