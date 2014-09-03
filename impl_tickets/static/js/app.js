/**
 * Created by Oleg on 07.08.2014.
 */
(function () {
    var app = angular.module('projectTickets', []);

    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    });

    app.controller('ItemController', ['$scope','$http', function ($scope, $http) {
        function getItems(){
            $http({
                    url: "get_items",
                    method: "GET"
                 }).
                success(function(data, status, headers, config) {
                    $scope.items = data;
                });
        }
        getItems();
    }]);

    app.controller("AddItemController", ['$scope','$http', function ($scope, $http) {
        $scope.item = {};

        this.addItem = function() {
            /*for (var key in this.item) {
                alert(key+':'+this.item[key])
            }*/

            $http({
                url: "add_item",
                method: "GET",
                params: this.item
             }).
            success(function(data, status, headers, config) {
                var scope = angular.element($("#body")).scope();
                scope.items = data;
            });
            this.item={};
        }
    }]);

    var tickets = [
        {
            id: 1,
            description: 'В поля src_host_id, dst_host_id надо указывать "mvs" вместо "mws"',
            status_mvs: 'Исправлено',
            status_slv: 'Обнаружено',
            date_found: '06.08.2014',
            date_fixed: '06.08.2014',
            date_fix_confirmed: '1288323623006',
        },
        {
            id: 2,
            description: 'Значения атрибута action должны быть в нижнем регистре, сейчас они идут с большой буквы.',
            status_mvs: 'Исправлено',
            status_slv: 'Обнаружено',
            date_found: '06.08.2014',
            date_fixed: '06.08.2014',
            date_fix_confirmed: '06.08.2014',
        }
    ];


})();