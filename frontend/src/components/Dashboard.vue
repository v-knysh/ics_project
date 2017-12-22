<template>
	<div class="container-fluid">
		<div class="row">
			<div class="col-xs-4">
				<div class="col-xs-12" id="sticky-sidebar">
					<ul class="nav flex-column">
						<li class="nav-item">
							<a class="nav-link active" href="#">Кіт</a>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="#">Link</a>
						</li>
						<li class="nav-item">
							<a class="nav-link" href="#">Link</a>
						</li>
						<li class="nav-item">
							<a class="nav-link disabled" href="#">Disabled</a>
						</li>
					</ul>
				</div>
			</div>
			<div class="col-xs-8" id="main">
				Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
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
	}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
</style>
