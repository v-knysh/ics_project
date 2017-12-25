import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import App from '@/App'

describe('Vue app', () => {
  it('should render correct contents', () => {
    Vue.use(Router);
    const router = new Router({
      routes: [
        { path: '/', name: 'Main', component: Main },
      ],
    });
    const vm = new Vue({
      el: document.createElement('div'),
      router: router,
      render: h => h('router-view'),
    });
    expect(vm.$el.querySelector('.main-title').textContent)
    .to.equal('Якісне управління для кота');
  })
})
// describe('App.vue', () => {
//    it('sets the correct default data', () => {
//    	expect(typeof App.data).toBe('function')
//     const defaultData = App.data()
//     expect(defaultData.message).toBe('hello!')
//   })
// })
