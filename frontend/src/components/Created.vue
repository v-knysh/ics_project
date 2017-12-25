<template>
	<div class="container">
		<h2>Реєстрування кота</h2>	
		<div class="form-group">
			<label for="name">Iм'я кота</label>
			<input type="text" class="form-control" id="name" v-model="name" placeholder="Iм'я кота">
		</div>
		<div class="form-group">
			<label for="name">Вік кота</label>
			<input type="number" class="form-control" id="age" v-model="age" placeholder="5">
		</div>
		<div class="form-group">
			<label for="name">Маса кота(кг)</label>
			<input type="number" class="form-control" id="weight" v-model="weight" placeholder="4.200">
		</div>
		<div class="col-xs-12">
			<button type="submit" class="btn btn-primary" id="submit-form"  @click="submitPet">Зареєструвати</button>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Created',
	data () {
		return {
			name: '',
			age: '',
			weight: '',
		}
	},
	methods: {
		submitPet: function() {
			let data = {
				pk: localStorage.getItem('pk'),
				name: this.name,
				age: this.age,
				weight: this.weight
			}
			this.$http.post('http://localhost:8000/dashboard/created', data, {emulateJSON: true}).then(response => {
				alert('Створено кота '+this.name)
				this.$emit('check');
			}, err => {

			}) 
		}	
	},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.mt-50{
	margin-top: 50px;
}
</style>
