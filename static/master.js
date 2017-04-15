
Vue.component('message-item', {
	props: ['message'],
	template: '<p>{{ message }}</p>'
})

var app = new Vue({
	el: '#app',
	data: {
		message : 'Hello!'
	}
})

var app2 = new Vue({
	el: '#app2',
	data: {
		message : 'Todays date is: ' + new Date()
	}
})

var app3 = new Vue({
	el: '#app3',
	data: {
		seen: true
	}
})

var app4 = new Vue({
	el: '#app4',
	data:{
		todos:[
			{ text: 'Learn JavaScript'},
			{ text: 'Learn Vue'},
			{ text: 'Build something awesome'},
			{ text: 'Type in console app4.todos.push("json object here") to add a new item'}
		]
	}
})

var app5 = new Vue({
	el: '#app5',
	data: {
		message : 'Reversable Message!'
	},
	methods: {
		reverseMessage: function(){
			this.message = this.message.split('').reverse().join('')
		}
	}
})

var app6 = new Vue({
	el: '#app6',
	data: {
		message : 'Hello Vue!'
	}
})

Vue.component('todo-item', {
	props: ['todo'],
	template: '<li>{{ todo.text }}</li>'
})

var app7 = new Vue({
	el: '#app7',
	data: {
		groceryList: [
			{text: 'Vegatables'},
			{text: 'Cheese'},
			{text: 'Stuff'}
		]
	}
})