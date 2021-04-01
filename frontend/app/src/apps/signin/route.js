import Signin from '@/apps/signin/Sign in'

export const SigninRoute = {
  name: 'signin',
  path: '/signin',
  component: Signin,
  props: {
    signup: false
  }
}

export const SignupRoute = {
  name: 'signup',
  path: '/signup',
  component: Signin,
  props: {
    signup: true
  }
}