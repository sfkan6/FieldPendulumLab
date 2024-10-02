import { Settings, Calculations , Charting, Charts, CreatingDataSample, PageNotFound, PendulumOfField, DataSamples, DataSample } from "@/pages"
import { dataSamplesTitles } from '@/pages/DataSamples'
import { chartsTitles } from '@/pages/Charting'
import { settingsTitles } from '@/pages/Settings'


export const routes = [
  {
    path: "/settings/:path",
    component: Settings,
    meta: { 
      title: route => settingsTitles[route.params.path],
      active: true,
    },
    props: true
  },
  { 
    path: '/',
    redirect: {name: 'pendulum_of_field'}
  },
  { 
    path: "/data_samples/angle/create",
    name: 'pendulum_of_field',
    component: PendulumOfField,
    meta: { 
      title: "Маятник поля"
    },
  },
  { 
    path: "/calculations",
    component: Calculations,
    meta: { 
      title: "Вычисления" 
    },
  },
  { 
    path: "/charts",
    component: Charts,
    meta: { 
      title: "Графики" 
    },
  },
  {
    path: "/charts/:chartType",
    component: Charting,
    meta: { 
      title: route => chartsTitles[route.params.chartType],
      active: true,
    },
    props: true
  },
  { 
    path: "/data_samples/:dataType/create",
    component: CreatingDataSample,
    meta: {
      title: route => dataSamplesTitles[route.params.dataType],
      active: true,
    },
    props: true
  },
  { 
    name: 'dataSample',
    path: "/data_samples/:dataType/:name",
    component: DataSample,
    meta: {
      title: route => dataSamplesTitles[route.params.dataType],
      active: true,
    },
    props: true
  },
  { 
    path: "/data_samples/:dataType",
    component: DataSamples,
    meta: {
      title: route => dataSamplesTitles[route.params.dataType],
      active: true,
    },
    props: true
  },
  { 
    path: "/:pathMatch(.*)*", 
    component: PageNotFound,
    meta: { title: "Page Not Found" },
  },
]

