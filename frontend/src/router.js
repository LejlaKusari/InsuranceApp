import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import NewRisk from './views/NewRisk.vue'
import RiskEntry from './views/RiskEntry.vue'
import RisksList from './views/RisksList.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/new-risk-entry/:id',
      name: 'risk-entry',
      // props: true,
      component: RiskEntry
    },
    {
      path: '/new-risk-model',
      name: 'new-risk',
      component: NewRisk, 
    },
    {
      path: '/risks-list',
      name: 'risks-list',
      component: RisksList
    }
  ],
})
