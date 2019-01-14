# from inteliService.models import CompanyCategory, Company

def getChatMessage(self, request):
        HTTP_HOST = request.META['HTTP_HOST']
        data = [
            {
                "公用模块": {
                    "获取应用信息": "api/system/info",
                },
                "登录模块": {
                    "获取认证Token": "api/account/api-token-auth",
                    "刷新登录Token": "api/account/api-token-refresh",
                    "验证登录Token": "api/account/api-token-verify",
                },
                "博客模块": {
                    "获取简历信息": "api/blog/resume",
                }
            },
        ]
        for index, item in enumerate(data):
            for k, v in item.items():
                for t_k, t_v in v.items():
                    value = t_v
                    new_value = "http://" + HTTP_HOST + "/" + value
                    data[index][k][t_k] = new_value
        return Response(data)