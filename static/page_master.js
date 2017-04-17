
Vue.component('data-item', {
	props: ['raw_data'],
	template: '<li>{{ raw_data.page_seq }}</li>'
})

var app8 = new Vue({
    el: '#app8',
	data : {
		raw_data : [],
        pagination: {
            "total": 500,
            "per_page": 1,
            "current_page": 1,
            "first_page": 100,
            "last_page": 10000,
            "current_page_seq": 100,
            "next_page_url": "/survey?page_seq=",
            "prev_page_url": "/survey?page_seq=200",
            "from": 1,
            "to": 2,
        }
	},
	methods: {
        get_raw_data: function () {
            var self = this;
            var current_page = self.pagination.next_page_url + self.pagination.current_page_seq;
            //noinspection JSUnresolvedVariable axios library.
            axios.get(current_page)
                .then(function (response) {
                    console.log(response.data);
                    self.raw_data = response.data;
                })
                .catch(function (error) {
                    console.log(error);
                });

        },
        page_up : function () {
            var self = this;
            self.pagination.current_page_seq += 100;
            this.get_raw_data();
        },
        page_down : function () {
            var self = this;
            if(self.pagination.first_page !== self.pagination.current_page_seq){
                self.pagination.current_page_seq -= 100;
                this.get_raw_data();
            }else{
                console.log("Start page goes here!")
            }
        }
    },
    mounted(){
        //runs method on page load
        this.get_raw_data();
    }
})






