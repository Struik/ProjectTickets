/**
 * Created by Oleg on 07.08.2014.
 */
(function () {
    var app = angular.module('projectTickets', ['ui.bootstrap']);

    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');//замена стандартных символов '{{' и '}}' для совместимости с django
        $interpolateProvider.endSymbol('}]}');
    });

    app.controller('ItemController', ['$scope','$http','$filter', function ($scope, $http, $filter) {

        function getItems(){
            $http({
                    url: "get_items",
                    method: "GET"
                 }).
            success(function(data, status, headers, config) {
                /*var dataAdjusted = [];
                for (var iter in data) {
                    dataAdjusted[iter]=data[iter]['fields'];
                    dataAdjusted[iter]['pk']=data[iter]['pk']
                }
                $scope.items = dataAdjusted;*/
                $scope.items = data;
                $scope.items.selected={};
                $scope.items.fixed={};
            });
        }
        //Загрузка данных при попадании на страницу
        getItems();

        //Галочка в шапке таблицы, которая включает на гриде все галочки, ответственные за удаление
        $scope.checkAll = function () {
            if ($scope.selectedAll) {
                $scope.selectedAll = true;
            } else {
                $scope.selectedAll = false;
            }
            angular.forEach($scope.items, function (item) {
                item.selected = $scope.selectedAll;
            });
        }

        //Изменение галочки "Выполнено". При установке проставляется дата выполнения равная времени нажатия,
        //при снятии дата выполнения очищается
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

        //Изменение галочки "Выполнено". При установке проставляется дата выполнения равная времени нажатия,
        //при снятии дата выполнения очищается
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

        //Удаление тикетов. Удаляются все тикеты, у которых проставлено selected=true, т.е. установлен галочка перед номером тикета
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

        var comparator = function(actual, expected) {
        if (actual && expected && typeof actual === 'object' && typeof expected === 'object') {
            var res = true;
            for (var key in expected) {
                if (key.charAt(0) !== '$' && hasOwnProperty.call(actual, key)) {
                    res = res && comparator(actual[key], expected[key]);
                }
            }
            return res;
            }
            expected = (''+expected).toLowerCase();
            return (''+actual).toLowerCase().indexOf(expected) > -1;
        };
        $scope.comparator = comparator;
    }]);

    app.controller("AddItemController", ['$scope','$http', function ($scope, $http) {
        $scope.item = {};

        //Инициализация элемента datepicker в форме добавления тикета. Код пока не разбирал, только немного адаптировал
        $scope.dateOptions = {
            formatYear: 'yy',
            startingDay: 1
        };

        $scope.format = 'dd-MMMM-yyyy';
        $scope.minDate = new Date();

        $scope.disabled = function(date, mode) {
            return ( mode === 'day' && ( date.getDay() === 0 || date.getDay() === 6 ) );
        }

        $scope.open = function($event) {
            $event.preventDefault();
            $event.stopPropagation();

            $scope.opened = true;
        };

        //Команда на добавление нового тикета
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

    //Фикс для правильной работы с датой, до его включения, при создании нового тикета в backend уходила вчерашняя дата.
    app.directive('datepickerLocaldate', ['$parse', function ($parse) {
        var directive = {
            restrict: 'A',
            require: ['ngModel'],
            link: link
        };
        return directive;

        function link(scope, element, attr, ctrls) {
            var ngModelController = ctrls[0];

            // called with a JavaScript Date object when picked from the datepicker
            ngModelController.$parsers.push(function (viewValue) {
                // undo the timezone adjustment we did during the formatting
                viewValue.setMinutes(viewValue.getMinutes() - viewValue.getTimezoneOffset());
                // we just want a local date in ISO format
                return viewValue.toISOString().substring(0, 10);
            });

            // called with a 'yyyy-mm-dd' string to format
            ngModelController.$formatters.push(function (modelValue) {
                if (!modelValue) {
                    return undefined;
                }
                // date constructor will apply timezone deviations from UTC (i.e. if locale is behind UTC 'dt' will be one day behind)
                var dt = new Date(modelValue);
                // 'undo' the timezone offset again (so we end up on the original date again)
                dt.setMinutes(dt.getMinutes() + dt.getTimezoneOffset());
                return dt;
            });
        }
    }]);


})();