/**
 * Created by iggor on 01/08/2017.
 */
angular.module('inGaiaApp')
    .factory('RealtyService', function ($http) {
        var baseUrl = 'http://localhost/api/v1/';

        return {
            getRealties: function (page) {
                return $http.get(baseUrl + 'realties/' + page);
            },

            getRealty: function (realtyId) {
                return $http.get(baseUrl + 'realty/' + realtyId);
            }
        }
    })