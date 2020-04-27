import datetime
import json

from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from ranking.models import Mark


class Ranking(View):
    """客户端排行榜视图"""

    def get(self,request):
        req_data = request.GET
        client = req_data.get('client')
        start_rank = req_data.get('start_rank','')
        end_rank = req_data.get('end_rank','')
        marks = Mark.objects.all().order_by('-mark').values('client','mark')
        i = 0
        rank_data =  []
        current_client = {}
        for mark in marks:
            i += 1
            mark['rank'] = i
            if mark['client'] == client:
                current_client = mark
            rank_data.append(mark)
        if not current_client:
            return JsonResponse({"message":"此客户端没有上传分数"}, status=400)
        rank_data.append(current_client)
        if start_rank and end_rank:
            start_rank = int(start_rank)
            end_rank = int(end_rank)
            rank_data = rank_data[start_rank-1:end_rank]
        return JsonResponse({'result': rank_data}, status=200)




    

    def post(self,request):
        req_data = json.loads(request.body)
        client = req_data.get('client')
        mark = req_data.get('mark')
        print(client,mark)
        try:
            mark_obj = Mark.objects.get(client=client)
        except Mark.DoesNotExist:
            Mark.objects.create(client=client,mark=mark)
        else:
            mark_obj.mark = mark
            mark_obj.update_time = datetime.datetime.now()
            mark_obj.save(update_fields=['mark','update_time'])
        return JsonResponse({'result':'S0001'}, status=200)


