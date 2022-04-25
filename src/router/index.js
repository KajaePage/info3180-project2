import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegistrationView.vue')
      },
      {
        path: '/login',
        name: 'login',
        component: () => import('../views/LoginView.vue')
        },
        {
          path: '/logout',
          name: 'logout',
          component: () => import('../views/LogoutView.vue')
          },
          {
            path: '/cars/new',
            name: 'carsn',
            component: () => import('../views/NewCarview.vue')
            },
            {
              path: '/explore',
              name: 'explore',
              component: () => import('../views/Carview.vue')
              },
              {
                path: '/users/:user_id',
                name: 'My Page',
                component: () => import('../views/Userview.vue')
                },
                {
                  path: '/cars/:car_id',
                  name: 'Carview',
                  component: () => import('../views/ViewCarView.vue')
                  },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router