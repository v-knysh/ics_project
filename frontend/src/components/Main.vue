<template>
  <section class="header">
       <div class="header-title animated fadeInUp">
        <h2 class="main-title">{{ title }}</h2>
        <p class="main-description">{{ descriptition }}</p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Main',
  data () {
    return {
      title: 'Якісне управління для кота',
      descriptition:'Заходь та керуй їжею без зайвих складнощів'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	.header{
	  height: calc(100vh - 56px);
	  width: 100%;
	  display: flex;
	  justify-content: center;
	  align-items: center;
	  background-image: url(../assets/wallpaper-cat-eat-fish.jpg);
	  background-position: center;
	  background-size: cover;
	  background-attachment: fixed;
	}
	.header .header-title{
	  text-align: center;
	  color: #fff;

	}
	.header .header-title h2{
	  font-weight: 300;
	  font-size: 40px;
	  margin-bottom: 5px;
	  text-transform: uppercase;
	  letter-spacing: 1px;
	}
	.header .header-title p{
	  font-weight: 300;
	  margin-top: 5px;
	  font-size: 18px;
	}
	.header .header-title button{
	  font-size: 18px;
	  margin-top: 20px;
	  background-color: transparent;
	  border: 3px solid #fff;
	  padding: 5px 30px;
	  transition: all 0.3s;
	}
	.header .header-title button:hover,
	.header .header-title button:focus{
	  background-color: #fff;
	  color: #000;
	}

</style>
