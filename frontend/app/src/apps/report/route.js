import Report from '@/apps/report/Report'
import ReportCheck from '@/apps/report/components/Check/ReportCheck'
import CreateContent from '@/apps/report/components/Content/CreateContent'
import ReportDetail from '@/apps/report/components/Check/ReportDetail'
import CreateReport from '@/apps/report/components/Report/CreateReport'
import Contents from '@/apps/report/components/Contents/Contents'
import MDViewer from '@/apps/report/components/Viewer/MDViewer'
import ContentEditor from '@/apps/report/components/objects/ContentEditor'

export const ReportRoute = {
  path: '/report',
  component: Report,
  children: [
    {
      path: 'content',
      component: CreateContent
    },
    {
      path: 'report',
      component: CreateReport,
      children: [
        {
          path: 'viewer',
          name: 'createreportviewer',
          component: MDViewer,
          props: true
        }
      ]
    },
    {
      path: 'contents',
      component: Contents,
      children: [
        {
          path: 'viewer',
          name: 'createcontentsviewer',
          component: ContentEditor,
          props: true
        }
      ]
    },
    {
      path: 'check',
      component: ReportCheck,
      children: [
        {
          path: 'detail',
          component: ReportDetail,
          props: true,
          children: [
            {
              path: 'viewer',
              name: 'detailreportviewer',
              component: MDViewer,
              props: true
            }
          ]
        }
      ]
    }
  ]
}