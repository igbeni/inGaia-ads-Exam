/**
 * Created by iggor on 01/08/2017.
 */
angular.module('inGaiaApp')
    .factory('RealtyService', function ($http) {
        var baseUrl = 'http://localhost/api/v1/';

        return {
            getRealties: function (page, asc) {
                return $http.get(baseUrl + 'realties/' + page + "/" + asc);
            },

            getRealty: function (realtyId, page, asc) {
                return $http.get(baseUrl + 'realty/' + realtyId + "/" + page + "/" + asc);
            },

            getRealtyInfo: function (realtyId) {
                return $http.get(baseUrl + 'realty-info/' + realtyId);
            }
        }
    })