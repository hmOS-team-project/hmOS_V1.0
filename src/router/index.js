import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

const VueRouter = new Router({
    routes: [{
            path: '/',
            redirect: '/login'
        },
        {
            path: '/',
            component: () =>
                import ( /* webpackChunkName: "home" */ '../components/common/Home.vue'),
            meta: { title: '自述文件' },
            children: [{
                    path: '/home',
                    component: () =>
                        import ( /* webpackChunkName: "home" */ '../components/page/Home.vue'),
                    meta: { title: '系统首页' }
                },
                {
                    path: '/tasktype',
                    component: () =>
                        import ( /* webpackChunkName: "home" */ '../components/page/TaskType.vue'),
                    meta: { title: '任务类型' }
                },
                {
                    path: '/tasklist',
                    component: () =>
                        import ( /* webpackChunkName: "home" */ '../components/page/TaskList.vue'),
                    meta: { title: '任务列表' }
                },
                {
                    path: '/mytask',
                    component: () =>
                        import ( /* webpackChunkName: "home" */ '../components/page/MyTask.vue'),
                    meta: { title: '用户任务' }
                },
                {
                    path: '/taskmode',
                    component: () =>
                        import ( /* webpackChunkName: "home" */ '../components/page/TaskMode.vue'),
                    meta: { title: '人机协作模式' }
                },
                {
                    path: '/identificationtask',
                    component: () =>
                        import ( /* webpackChunkName: "dashboard" */ '../components/page/IdentificationTask.vue'),
                    meta: { title: '识别任务' }
                },
                {
                    path: '/resourceManagement',
                    component: () =>
                        import ( /* webpackChunkName: "resourceManagement" */ '../components/page/ResourceManagement.vue'),
                    meta: { title: '资源管理' },
                    // children: [{
                    //     path: '/resourceManagement/resourceList',
                    //     component: () => import(/* webpackChunkName: "resourceList" */ '../components/page/ResourceList.vue'),
                    //     meta: { title: '资源列表' }
                    // }]
                },
                {
                    path: '/icon',
                    component: () =>
                        import ( /* webpackChunkName: "icon" */ '../components/page/Icon.vue'),
                    meta: { title: '自定义图标' }
                },
                {
                    path: '/table',
                    component: () =>
                        import ( /* webpackChunkName: "table" */ '../components/page/BaseTable.vue'),
                    meta: { title: '任务列表' }
                },
                {
                    path: '/tabs',
                    component: () =>
                        import ( /* webpackChunkName: "tabs" */ '../components/page/Tabs.vue'),
                    meta: { title: '消息列表' }
                },
                {
                    path: '/form',
                    component: () =>
                        import ( /* webpackChunkName: "form" */ '../components/page/BaseForm.vue'),
                    meta: { title: '任务描述' }
                },
                {
                    // HumanComputing组件
                    path: '/humancomputing',
                    component: () =>
                        import ( /* webpackChunkName: "humancmputing" */ '../components/page/HumanComputing.vue'),
                    meta: { title: '人机计算接口' }
                },
                {
                    // ComputingResult组件
                    path: '/computingresult',
                    component: () =>
                        import ( /* webpackChunkName: "computingresult" */ '../components/page/ComputingResult.vue'),
                    meta: { title: '计算结果查看' }
                },
                {
                    // 图片上传组件
                    path: '/upload',
                    component: () =>
                        import ( /* webpackChunkName: "upload" */ '../components/page/Upload.vue'),
                    meta: { title: '数据上传' }
                },
                {
                    // ComputingStatus组件
                    path: '/computingstatus',
                    component: () =>
                        import ( /* webpackChunkName: "computingstatus" */ '../components/page/ComputingStatus.vue'),
                    meta: { title: '计算状态查看' }
                },
                {
                    // 拖拽列表组件
                    path: '/drag',
                    component: () =>
                        import ( /* webpackChunkName: "drag" */ '../components/page/DragList.vue'),
                    meta: { title: '拖拽列表' }
                },
                {
                    // 拖拽Dialog组件
                    path: '/dialog',
                    component: () =>
                        import ( /* webpackChunkName: "dragdialog" */ '../components/page/DragDialog.vue'),
                    meta: { title: '拖拽弹框' }
                },
                {
                    // 国际化组件
                    path: '/i18n',
                    component: () =>
                        import ( /* webpackChunkName: "i18n" */ '../components/page/I18n.vue'),
                    meta: { title: '国际化' }
                },
                {
                    // 权限页面
                    path: '/permission',
                    component: () =>
                        import ( /* webpackChunkName: "permission" */ '../components/page/Permission.vue'),
                    meta: { title: '权限测试', permission: true }
                },
                {
                    path: '/404',
                    component: () =>
                        import ( /* webpackChunkName: "404" */ '../components/page/404.vue'),
                    meta: { title: '404' }
                },
                {
                    path: '/403',
                    component: () =>
                        import ( /* webpackChunkName: "403" */ '../components/page/403.vue'),
                    meta: { title: '403' }
                },
                {
                    path: '/donate',
                    component: () =>
                        import ( /* webpackChunkName: "donate" */ '../components/page/Donate.vue'),
                    meta: { title: '支持作者' }
                },
                {
                    path: '/resourceList',
                    component: () =>
                        import ( /* webpackChunkName: "icon" */ '../components/page/ResourceList.vue'),
                    meta: { title: '资源列表' }
                },
                {
                    path: '/humanDetail',
                    component: () =>
                        import ( /* webpackChunkName: "icon" */ '../components/page/HumanDetail.vue'),
                    meta: { title: '人类详情' }
                },
            ]
        },
        {
            path: '/login',
            component: () =>
                import ( /* webpackChunkName: "login" */ '../components/page/LoginPlus.vue'),
            meta: { title: '登录' }
        },
        {
            path: '/homeplus',
            component: () =>
                import ( /* webpackChunkName: "login" */ '../components/page/HomePlus.vue'),
            meta: { title: '首页' }
        },
        {
            path: '/tasktypeplus',
            component: () =>
                import ( /* webpackChunkName: "login" */ '../components/page/TaskTypePlus.vue'),
            meta: { title: '类型' }
        },
        {
            path: '/identificationtaskplus',
            component: () =>
                import ( /* webpackChunkName: "login" */ '../components/page/IdentificationTaskPlus.vue'),
            meta: { title: '分类任务' }
        },
        {
            path: '/taskmodeplus/:input',
            component: () =>
                import ( /* webpackChunkName: "login" */ '../components/page/TaskModePlus.vue'),
            meta: { title: '协作模式' }
        },
        {
            // HumanComputing组件
            path: '/humancomputingplus',
            component: () =>
                import ( /* webpackChunkName: "humancmputing" */ '../components/page/HumanComputingPlus.vue'),
            meta: { title: '人机计算接口' }
        },
        {
            // ComputingResult组件
            path: '/computingresultplus',
            component: () =>
                import ( /* webpackChunkName: "computingresult" */ '../components/page/ComputingResultPlus.vue'),
            meta: { title: '计算结果查看' }
        },
        {
            // ComputingStatus组件
            path: '/computingstatusplus',
            component: () =>
                import ( /* webpackChunkName: "computingstatus" */ '../components/page/ComputingStatusPlus.vue'),
            meta: { title: '计算状态查看' }
        },

        {
            path: '*',
            redirect: '/404'
        },
        {
            path: '/tasklistplus',
            component: () =>
                import ( /* webpackChunkName: "login" */ '../components/page/TaskListPlus.vue'),
            meta: { title: '任务查看' }
        },
        {
            path: '/crowdsourcingaccess',
            component: () =>
                import ( /* webpackChunkName: "login" */ '../components/page/CrowdsourcingAccess.vue'),
            meta: { title: '众包接入' }
        },
        {
            path: '/inviteusers',
            component: () =>
                import ( /* webpackChunkName: "login" */ '../components/page/InviteUsers.vue'),
            meta: { title: '用户邀请' }
        },
        {
            path: '/resourcemanagementplus',
            component: () =>
                import ( /* webpackChunkName: "login" */ '../components/page/ResourceManagementPlus.vue'),
            meta: { title: '资源管理' }
        }
    ]
});
// 登录拦截
VueRouter.beforeEach((to, from, next) => {
    if (to.path === '/login') {
        next()
    } else {
        let token = localStorage.getItem('Authorization')
        if (!token) {
            next('/login')
        } else {
            next()
        }
    }
})
export default VueRouter