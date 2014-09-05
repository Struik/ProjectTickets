/**
 * Created by Oleg on 07.08.2014.
 */
(function () {
    var app = angular.module('projectTickets', []);

    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    });

    app.controller('ItemController', ['$scope','$http','$filter', function ($scope, $http, $filter) {

        function getItems(){
            $http({
                    url: "get_items",
                    method: "GET"
                 }).
                success(function(data, status, headers, config) {
                    $scope.items = data;
                    $scope.items.selected={};
                    $scope.items.fixed={};
                });
        }
        getItems();

        this.fix = function(pk,value) {
            $http({
                url: "change_item",
                method: "GET",
                params: {pks: pk, action: 'fixed', value: value, date_field: 'date_fixed'}
             }).
            success(function(data, status, headers, config) {
                $scope.items = data;
            });
        }

        this.confirm = function(pk,value) {
            $http({
                url: "change_item",
                method: "GET",
                params: {pks: pk, action: 'confirmed', value: value, date_field: 'date_fix_confirmed'}
             }).
            success(function(data, status, headers, config) {
                $scope.items = data;
            });
        }


        this.deleteItems = function() {
            var trues = $filter("filter")( $scope.items , {selected:true} );
            var pks = [];

            for (var iter in trues) {
                pks.push(trues[iter].pk);
            }

            $http({
                url: "delete_item",
                method: "GET",
                params: {pks: pks}
             }).
            success(function(data, status, headers, config) {
                $scope.items = data;
            });
        }
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
                var table = angular.element($("#body")).scope();
                $scope.$$prevSibling.items = data;
                $scope.addItemCtrl.item={};
            });
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