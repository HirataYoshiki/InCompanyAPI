import Signin from '@/apps/signin/Sign in'

export const SigninRoute = {
  name: 'signin',
  path: '/signin',
  component: Signin,
  props: {
    signup: false
  }
}