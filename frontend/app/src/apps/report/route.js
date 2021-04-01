import Report from '@/apps/report/Report'
import ReportCheck from '@/apps/report/components/Check/ReportCheck'
import ContentMde from '@/apps/report/components/Content/ContentMde'
import ReportDetail from '@/apps/report/components/Check/ReportDetail'
import CreateReport from '@/apps/report/components/Report/CreateReport'
import Contents from '@/apps/report/components/Contents/Contents'
import MDViewer from '@/apps/report/components/Viewer/MDViewer'

export const ReportRoute = {
  path: '/report',
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
      path: 'contents',
      component: Contents
    },
    {
      path: 'viewer',
      name: 'viewer',
      component: MDViewer,
      props: true
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