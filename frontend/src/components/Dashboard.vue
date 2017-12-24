<template>
	<div class="container-fluid">
		<div class="row">
			<nav class="col-xs-3 bg-faded sidebar">
				<ul class="nav nav-pills flex-column">
					<li class="nav-item">
						<router-link class="nav-link" to="/dashboard/about">Про кота</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link" to="/dashboard/refrigerator">Холодильник</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link" to="/dashboard/plan">План їжі</router-link>
					</li>
				</ul>
			</nav>
			<div class="col-xs-9" id="main">
				<router-view></router-view>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Dashboard',
	data () {
		return {
			title: 'Якісне управління для кота',
		}
	},
	created: function() {
		let data = {
			pk: localStorage.getItem('pk')
		}
		this.$http.post('http://localhost:8000/dashboard', data).then(response => {
		}, err => {
			alert(err.msg)
		})
		this.$router.push('/dashboard/about');
	}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
#sticky-sidebar {
	background-color: #343a40;
	position:fixed;
	width: 200px;
	height: 100%;
}
#sticky-sidebar .nav-item{
	margin: 0;
	padding: 0;
}
#sticky-sidebar .nav-item .nav-link{
	color: #ddd;
	border-bottom: 1px solid #eee;
}
#sticky-sidebar .nav-item .nav-link.active{
	text-decoration: underline;
	color: #fff;
}
#sticky-sidebar .nav-item .nav-link:hover{
	color: #fff
}
#main{
	padding: 20px 40px;
}
#main h2{
	margin-bottom: 40px;
}
</style>
