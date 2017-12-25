<template>
	<div class="container">
		<div class="col-xs-12">
			<h2>Загальна інформація про кота</h2>
		</div>
		<div class="col-xs-12">
			<div class="col-xs-3"><b>Ім'я кота:</b> {{ name }}</div>
			<div class="col-xs-3"><b>Вік:</b> {{ age }}</div>
			<div class="col-xs-3"><b>Маса:</b> {{ weight }}</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'AboutCat',
	data () {
		return {
			name: '',
			weight: '',
			age: '',
		}
	},
	created: function() {
		let data = {
			pk: localStorage.getItem('pk')
		}
		this.$http.post('http://localhost:8000/dashboard/petinfo', data, {emulateJSON: true}).then(response => {
			this.name = response.body.name
			this.weight = response.body.weight
			this.age = response.body.age
		}, err => {
			alert(err.body.msg)
		});
	}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	.col-xs-3{
		font-size: 18px;
	}
</style>
