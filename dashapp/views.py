from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from .models import Influencer, Post

import re


class InstaDataView(ListView):
    model = Post
    context_object_name = 'influencer_data' # context의 변수 이름
    template_name = 'dashapp/dashboard.html'
    paginate_by = 10

    # pagination 설정
    def get_context_data(self, **kwargs):
        context = super(InstaDataView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 10  # Display only 10 page numbers
        max_index = len(paginator.page_range) # 전체 페이지 수

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context
    

    # 쿼리문으로 데이터 불러와서 물음표 -> 공백 처리
    # get_queryset 설정안하면 default값으로 objects.all() 객체 생성
    def get_queryset(self):
        post_data = Post.objects.values()
        influencer_data = Influencer.objects.values()

        for post in post_data:
            for data in influencer_data:
                d = data['username']
                d = re.sub('[?]', ' ', d)
                data['username'] = d
                if post['unique_id'] == data['unique_id']:
                    post['insta_id'] = data['insta_id']
                    post['username'] = data['username']
                    post['follower'] = data['follower']
        return post_data
