import Vue from 'vue'
import Resource from 'vue-resource';
import Router from 'vue-router'
import Main from '@/components/Main'
import Dashboard from '@/components/Dashboard'
import AboutCat from '@/components/AboutCat'
import Plan from '@/components/Plan'
import Refrigerator from '@/components/Refrigerator'
import About from '@/components/About'

Vue.use(Router)
Vue.use(Resource);

Vue.http.headers.common['Content-Type'] = 'application/json'
// Vue.http.headers.common['Access-Control-Allow-Origin'] = '*'

export default new Router({
  linkActiveClass: 'active',
  routes: [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    children: [
    {
      path: 'about',
      component: AboutCat
    },
    {
      path: 'refrigerator',
      component: Refrigerator
    },
    {
      path: 'plan',
      component: Plan
    },
    ]
  }
  ]
})
