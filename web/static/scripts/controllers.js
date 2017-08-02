/**
 * Created by iggor on 01/08/2017.
 */
angular.module('inGaiaApp')
    .controller('HomeController', function ($scope, $log, $stateParams, RealtyService) {

        var page = parseInt($stateParams.page);

        $scope.previousPage = page - 1;
        $scope.nextPage = page + 1;

        $scope.showPreviousButton = page > 0;
        $scope.showNextButton = false;

        $scope.asc = false;
        $scope.desc = !$scope.asc;

        $scope.toggleOrderBy = function () {
            $scope.asc = !$scope.asc ;
            $scope.desc = !$scope.asc;
        }

        loadRealties();

        function loadRealties() {
            RealtyService.getRealties(page, $scope.asc).then(function (response) {
                if (response.statusText === 'OK') {
                    $scope.realties = response.data.data;
                    $scope.showNextButton = page < response.data.count;
                }
            });
        }
    })
    .controller('LogController', function ($scope, $log, $stateParams, RealtyService) {

        var page = parseInt($stateParams.page);
        var id = $stateParams.id;

        $scope.id = id;

        $scope.previousPage = page - 1;
        $scope.nextPage = page + 1;

        $scope.showPreviousButton = page > 0;
        $scope.showNextButton = false;

        $scope.asc = false;
        $scope.desc = !$scope.asc;

        $scope.toggleOrderBy = function () {
            $scope.asc = !$scope.asc ;
            $scope.desc = !$scope.asc;
        }

        loadRealties();

        function loadRealties() {
            RealtyService.getRealty(id, page, $scope.asc).then(function (response) {
                if (response.statusText === 'OK') {
                    $scope.realties = response.data.data;
                    $scope.showNextButton = page < response.data.count;
                }
            });
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