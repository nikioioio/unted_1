from django.shortcuts import render,HttpResponse
from django.views.generic import View,TemplateView


# def index_page(request):
#     return render(request,'indexpage/index.html')


class IndexPageView(View):
    template_name = 'indexpage/index.html'

    def get(self,request):
        args = {
            'spam':'eggs',
            'foo':'bar',
        }
        return render(request,template_name=self.template_name,context= args)

    def post(self,request):
        return HttpResponse('OK')


# class IndexPageView(TemplateView):
#     template_name = 'indexpage/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({
#             'spam': 'eggs',
#             'foo':'bar',
#         })
#
#         return context