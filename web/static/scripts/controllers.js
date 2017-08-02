/**
 * Created by iggor on 01/08/2017.
 */
angular.module('inGaiaApp')
    .controller('HomeController', function ($scope, $log, $stateParams, RealtyService) {

        var page = parseInt($stateParams.page);

        $scope.previousPage = page - 1;
        $scope.nextPage = page + 1;

        $scope.showPreviousButton = page > 0;

        loadRealties();

        function loadRealties() {
            RealtyService.getRealties(page).then(function (response) {
                if (response.statusText === 'OK') {
                    $scope.realties = response.data;
                }
            });
        }
    })
    .controller('DetailController', function ($scope, $log, $stateParams, RealtyService) {

        var id = $stateParams.id;

        loadRealty(id);

        function loadRealty() {
            RealtyService.getRealty(id).then(function (response) {
                if (response.statusText === 'OK') {
                    $scope.realty = response.data;
                }
            });
        }
    });