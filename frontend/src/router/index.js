import Vue from 'vue'
import Resource from 'vue-resource';
import Router from 'vue-router'
import Main from '@/components/Main'
import Dashboard from '@/components/Dashboard'

Vue.use(Router)
Vue.use(Resource);

Vue.http.headers.common['Content-Type'] = 'application/json'
// Vue.http.headers.common['Access-Control-Allow-Origin'] = '*'

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    }
  ]
})
