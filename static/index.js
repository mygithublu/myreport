"use strict";

new Vue({
    el: '#app',
    data: function data() {
        return {
            list: ['','',1,2,3,'','','','',4,5,6,'','',7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,'','',28,29,30,'','','','','.','.','.','',''],
            calendar: {}
        };
    },
    methods: {
        init: function init() {
            this.year = new Date().getFullYear();
            this.dateIndex = this.dateIndexInYear();
        },
        showCalendar: function showCalendar(month) {
            //根据年月生成日历
			
            var date = new Date(this.year, month-1, 1); //month月的第一天

            var day = date.getDay(); //第一天是星期几
					
            var days = new Date(this.year, month, 0).getDate(); //month月的总天数

            var temp = Math.floor((days + day) / 7);
            var rows = (days + day) % 7 == 0 ? temp : temp + 1; //每个月几行

            var d = 1;
            var mounthArr = [];

            for (var i = 0; i < rows; i++) {
                //循环行
                mounthArr[i] = [];

                for (var j = 1; j <= 7; j++) {
                    //循环列
                    if (d > days) {
                        //超过最大天数赋空
                        mounthArr[i].push('');
                        continue;
                    }

                    if (i == 0) {
                        //第一行判断month月第一天是星期几，例如星期二前面空两个周日、周一
                        if (j >= day + 1) {
                            mounthArr[i].push(d < 10 ? "0" + d : d);
                            d++;
                        } else {
                            mounthArr[i].push('');
                        }
                    } else {
                        mounthArr[i].push(d < 10 ? "0" + d : d);
                        d++;
                    }
                }
            }

            this.calendar[month] = mounthArr;
        },
        dateIndexInYear: function dateIndexInYear() {
            //计算今天是今年的第几天
            var nowDate = new Date();
            var initTime = new Date();
            initTime.setMonth(0); // 本年初始月份

            initTime.setDate(1); // 本年初始时间

            var differenceVal = nowDate - initTime; // 今天的时间减去本年开始时间，获得相差的时间

            console.log(nowDate, initTime, differenceVal, Math.ceil(differenceVal / (24 * 60 * 60 * 1000)));
            return Math.ceil(differenceVal / (24 * 60 * 60 * 1000));
        }
    },
    created: function created() {
        var _this = this;

        this.init();
        this.list.forEach(function (item) {
            if (item) {
                _this.showCalendar(item);
            }
        });
        console.log(this.calendar);
    }
});