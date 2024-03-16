from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings
from .serializers import Exchange_rateSerializer
from django.http import JsonResponse
from . models import Exchange_rate
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def save_exchange_rates(request):  # requests 모듈을 활용하여 정기예금 상품 목록 데이터를 가져와 정기예금 상품 목록과 옵션 목록을 DB에 저장
    api_key = settings.API_KEY2
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate=20180102&data=AP01'
    response = requests.get(url).json()
    exchange_list = Exchange_rate.objects.values_list('cur_unit', flat=True)
    # cur_unit = models.CharField(max_length=100)	# String 통화코드	
    # cur_nm	= models.CharField(max_length=250)	# 국가/통화명	
    # ttb	= models.CharField(max_length=250)	# 전신환(송금) 받으실때	
    # tts	= models.CharField(max_length=250)	# 전신환(송금) 보내실때	
    # deal_bas_r = models.CharField(max_length=250)	# 매매 기준율	
    # bkpr = models.CharField(max_length=250)	# 장부가격	
    # yy_efee_r = models.CharField(max_length=250)	# 년환가료율	
    # ten_dd_efee_r = models.CharField(max_length=250)	# 10일환가료율
    # kftc_deal_bas_r	= models.CharField(max_length=250)	# 서울외국환중개 매매기준율	
    # kftc_bkpr = models.CharField(max_length=250)	# 서울외국환중개 장부가격

    for li in response:
        cur_unit = li.get('cur_unit')
        if cur_unit in exchange_list:
            exchanges = Exchange_rate.objects.get(cur_unit=cur_unit)
            exchanges.cur_nm = li.get('cur_nm')
            exchanges.ttb = li.get('ttb')
            exchanges.tts = li.get('tts')
            exchanges.deal_bas_r = li.get('deal_bas_r')
            exchanges.bkpr = li.get('bkpr')
            exchanges.yy_efee_r = li.get('yy_efee_r')
            exchanges.ten_dd_efee_r = li.get('ten_dd_efee_r')
            exchanges.kftc_deal_bas_r = li.get('kftc_deal_bas_r')
            exchanges.kftc_bkpr = li.get('kftc_bkpr')
            
        else:
            save_data = {
                'cur_unit':li.get('cur_unit'),
                'cur_nm':li.get('cur_nm'),
                'ttb':li.get('ttb'),
                'tts' : li.get('tts'),
                'deal_bas_r' : li.get('deal_bas_r'),
                'bkpr' : li.get('bkpr'),
                'yy_efee_r' : li.get('yy_efee_r'),
                'ten_dd_efee_r' : li.get('ten_dd_efee_r'),
                'kftc_deal_bas_r' : li.get('kftc_deal_bas_r'),
                'kftc_bkpr' : li.get('kftc_bkpr'),
            }
            serializer = Exchange_rateSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    return JsonResponse({'message':'okay'})

@api_view(['GET'])
def get_exchange_rates(request): # GET: 전체 환율 목록 반환
    if request.method == 'GET':
        exchage_rates = Exchange_rate.objects.all()
        serializer = Exchange_rateSerializer(exchage_rates, many = True)
        return Response(serializer.data)
    
    # elif request.method == 'POST':
    #     serializer = Exchange_rateSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
