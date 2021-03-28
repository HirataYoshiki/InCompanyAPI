import Report from '@/apps/report/Report'
import ReportCheck from '@/apps/report/components/Check/ReportCheck'
import ContentMde from '@/apps/report/components/Content/ContentMde'

export const ReportRoute = {
  path: '/report',
  name: 'report',
  component: Report,
  children: [
    {
      path: 'check',
      component: ReportCheck
    },
    {
      path: 'content',
      component: ContentMde
    }
  ]
}