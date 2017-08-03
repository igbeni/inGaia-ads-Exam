/**
 * Created by iggor on 01/08/2017.
 */
angular.module('inGaiaApp')
    .factory('RealtyService', function ($http) {
        var baseUrl = 'http://localhost/api/v1/';

        return {
            getRealtiesAsc: function (page) {
                return $http.get(baseUrl + 'realties_asc/' + page);
            },

            getRealtiesDesc: function (page) {
                return $http.get(baseUrl + 'realties_desc/' + page);
            },

            getRealtyLogAsc: function (realtyId, page) {
                return $http.get(baseUrl + 'realty_log_asc/' + realtyId + "/" + page);
            },

            getRealtyLogDesc: function (realtyId, page) {
                return $http.get(baseUrl + 'realty_log_desc/' + realtyId + "/" + page);
            },

            getRealtyInfo: function (realtyId) {
                return $http.get(baseUrl + 'realty-info/' + realtyId);
            },

            searchTitle: function (query) {
                return $http.post(baseUrl + 'search', query);
            },

            getRealtiesByCities: function() {
                return $http.get(baseUrl + 'realties_by_cities');
            }
        }
    })