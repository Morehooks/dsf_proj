
Vue.component('data-item', {
	props: ['raw_data'],
	template: '<li>{{ raw_data.section_seq }}</li>'
})

var app8 = new Vue({
    el: '#app8',
	data : {
		raw_data : [],
        questions : []
	},
	methods: {
        get_raw_data: function () {
            var self = this;
            //noinspection JSUnresolvedVariable axios library.
            axios.get('/survey?page_seq=100')
                .then(function (response) {
                    console.log(response.data);
                    self.raw_data = response.data;
                })
                .catch(function (error) {
                    console.log(error);
                });

        }
    },
    mounted(){
        //runs method on page load
        this.get_raw_data();
    }
})





