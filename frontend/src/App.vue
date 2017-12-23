<template>
	<div id="app">
		<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
			<router-link class="navbar-brand" to="/">EatCats</router-link>

			<ul class="navbar-nav ml-auto">
				<li class="nav-item" v-if="isLogin">
					<a class="nav-link" href="#" @click="goDashboard">Зайти до кабінета, {{ username }}</a>
				</li>
				<li class="nav-item" v-if="isLogin">
					<button class="btn btn-danger" href="#" @click="logout">Вийти з кабінету</button>
				</li>			
				<li class="nav-item" v-if="!isLogin">
					<router-link class="nav-link" to="/about" >Про нас</router-link>
				</li>
				<li class="nav-item" v-if="!isLogin">
					<a class="nav-link" data-toggle="modal" data-target="#reg-modal" href="#" >Регестрація</a>
				</li>
				<li class="nav-item" v-if="!isLogin">
					<button class="btn btn-outline-light" data-toggle="modal" data-target="#login-modal" href="#">Вхід до кабінета</button>
				</li>
			</ul>
		</nav>
		<router-view/>

		<div class="modal" id="login-modal" tabindex="-1" role="dialog">
			<div class="modal-dialog" role="document">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title">Вхід до кабінету</h5>
						<button type="button" class="close" data-dismiss="modal" aria-label="Close" ref="closeLogin">
							<span aria-hidden="true">&times;</span>
						</button>
					</div>
					<div class="modal-body">
						<form action="/" method="Post" id="login-form">
							<div class="form-group row">
								<label for="login" class="col-sm-2 col-form-label">Логін</label>
								<div class="col-sm-10">
									<input type="text" class="form-control" id="login" v-model="login" placeholder="Логін">
								</div>
							</div>
							<div class="form-group row">
								<label for="inputPassword" class="col-sm-2 col-form-label">Пароль</label>
								<div class="col-sm-10">
									<input type="password" class="form-control" id="inputPassword" v-model="password" placeholder="Пароль">
								</div>
							</div>
						</form>
					</div>
					<div class="modal-footer">
						<button type="submit" class="btn btn-primary" id="submit-form" :data-dismiss="modal"  @click="submitLogin">Ввійти</button>
						<button type="button" class="btn btn-secondary" data-dismiss="modal">Закрити</button>
					</div>
				</div>
			</div>
		</div>
		<div class="modal" id="reg-modal" tabindex="-1" role="dialog">
			<div class="modal-dialog" role="document">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title">Реєстрація</h5>
						<button type="button" class="close" data-dismiss="modal" aria-label="Close" ref="closeReg">
							<span aria-hidden="true">&times;</span>
						</button>
					</div>
					<div class="modal-body">
						<form>
							<div class="form-group row">
								<label for="newlogin" class="col-sm-2 col-form-label">Логін</label>
								<div class="col-sm-10">
									<input type="text" class="form-control" id="newlogin" v-model="newlogin" placeholder="Логін">
								</div>
							</div>
							<div class="form-group row">
								<label for="email" class="col-sm-2 col-form-label">Email</label>
								<div class="col-sm-10">
									<input type="text" class="form-control" id="email" v-model="email" placeholder="Email">
								</div>
							</div>
							<div class="form-group row">
								<label for="newpassword" class="col-sm-2 col-form-label">Пароль</label>
								<div class="col-sm-10">
									<input type="password" class="form-control" id="newpassword" v-model="newpassword" placeholder="Пароль">
								</div>
							</div>
						</form>
					</div>
					<div class="modal-footer">
						<button type="submit" class="btn btn-primary" id="submit-form" :data-dismiss="modal"  @click="regButton">Зареєструвати</button>
						<button type="button" class="btn btn-secondary" data-dismiss="modal">Закрити</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'app',
	data () {
		return {
			title: 'Якісне управління для кота',
			isLogin: false,
			login: '',
			password: '',
			newlogin: '',
			newpassword:'',
			email:'',
			username: '',
			modal:'',
			pk: ''
		}
	},
	methods: {
		submitLogin: function(event) {
			let close = this.$refs.closeLogin;
			let data = {
				login: this.login,
				password: this.password
			}

			this.$http.post('http://localhost:8000/users', data).then(response => {
				localStorage.setItem('pk', response.body.pk)
				localStorage.setItem('username', response.body.user)
				this.username = response.body.user
				this.isLogin = true
				close.click()
			}, err => {
				alert(err.msg)
			})
		},
		goDashboard: function(event) {
			let data = {
				pk: localStorage.getItem('pk')
			}
			this.$http.post('http://localhost:8000/', data).then(response => {
				this.$router.push('/dashboard/')
			}, err => {
				alert(err.msg)
			})
		},
		regButton: function(event) {
			let close = this.$refs.closeReg;
			let data = {
				login: this.newlogin,
				email: this.email,
				password: this.newpassword
			}
			this.$http.post('http://localhost:8000/reg', data).then(response => {
				alert(`Заэрестровано користувача ${this.newlogin}`)
				close.click();
			}, err => {
				console.log(err); 
			});
		},
		logout: function() {
			localStorage.removeItem('pk')
			this.isLogin = false
			this.$router.push('/')
		},
		checkoutLogin: function() {
			let jwt = localStorage.getItem('pk')
			if(jwt) {
				this.username = localStorage.getItem('username')
				this.isLogin = true
			}
			else {
				this.isLogin = false
				this.$router.push('/')  
			}
		},
	},
	created: function () {
		this.checkoutLogin();
	} 

}
</script>

<style>

</style>
