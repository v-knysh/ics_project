<template>
	<div class="container">
		<div class="row">
			<h2>Продукти у холодильнику</h2>
						<table class="table">
				<thead class="thead-light">
					<tr>
						<th scope="col">Продукт</th>
						<th scope="col">Загальна кількість калорій</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td>Куриная ножка</td>
						<td>2224кКл</td>
					</tr>
					<tr>
						<td>Молоко</td>
						<td>3123кКл</td>
					</tr>
					<tr>
						<td>Сыр</td>
						<td>1231кКл</td>
					</tr>
					<tr>
						<td>Сухой корм</td>
						<td>4431кКл</td>
					</tr>
					<tr>
						<td>Мокрый корм</td>
						<td>3212кКл</td>
					</tr>
					<tr>
						<td>Куриная грудка</td>
						<td>2213кКл</td>
					</tr>
				</tbody>
			</table>
		</div>
	</div>
</template>

<script>
export default {
	name: 'AboutCat',
	data () {
		return {
			title: 'Якісне управління для кота',
		}
	}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
