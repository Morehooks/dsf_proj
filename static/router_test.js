/**
 * Created by jakel on 16/04/2017.
 */
const Foo = { template: '<div>foo</div>' }
const Bar = { template: '<div>bar</div>' }
const User = {
    template: '<div>page</div>'

}

const routes = [
   { path: '/foo', component: Foo },
   { path: '/bar', component: Bar },
   { path: '/counting', component: User },

]

const router = new VueRouter({
  routes // short for routes: routes
})

const app = new Vue({
    router,
    data :{
        page : 1
    },
    methods: {
        onSubmit: function() {
            // Do some stuff here
            router.push({path :'counting'});
        }
    }

}).$mount('#app')