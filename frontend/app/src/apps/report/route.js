import Report from '@/apps/report/Report'
import ReportCheck from '@/apps/report/components/Check/ReportCheck'
import ContentMde from '@/apps/report/components/Content/ContentMde'
import ReportDetail from '@/apps/report/components/Check/ReportDetail'
import CreateReport from '@/apps/report/components/Report/CreateReport'

export const ReportRoute = {
  path: '/report',
  name: 'report',
  component: Report,
  children: [
    {
      path: 'content',
      component: ContentMde
    },
    {
      path: 'report',
      component: CreateReport
    },
    {
      path: 'check',
      component: ReportCheck,
      children: [
        {
          path: 'detail',
          component: ReportDetail,
          props: {
            new: false
          }
        }
      ]
    }
  ]
}