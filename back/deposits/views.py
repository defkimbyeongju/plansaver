# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingProductsSerializer, SavingOptionSerializer, NewDepositSerializer, NewSavingSerializer
from django.http import JsonResponse
from . models import DepositOptions, DepositProducts, SavingProducts, SavingOptions, NewDeposits, NewSavings
from rest_framework import status


#################################################################################################################################
@api_view(['GET'])
def save_deposit_products(request):  # requests 모듈을 활용하여 정기예금 상품 목록 데이터를 가져와 정기예금 상품 목록과 옵션 목록을 DB에 저장
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()
    deposit_list = DepositProducts.objects.values_list('fin_prdt_cd', flat=True)
    
    for li in response.get("result").get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd')

        if fin_prdt_cd in deposit_list:
            # 이미 존재하는 경우, 필터링된 객체를 가져와 업데이트
            deposit_product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            deposit_product.dcls_month = li.get('dcls_month')
            deposit_product.kor_co_nm = li.get('kor_co_nm')
            deposit_product.fin_prdt_nm = li.get('fin_prdt_nm')
            deposit_product.etc_note = li.get('etc_note')
            deposit_product.join_deny = li.get('join_deny')
            deposit_product.join_member = li.get('join_member')
            deposit_product.join_way = li.get('join_way')
            deposit_product.spcl_cnd = li.get('spcl_cnd')
            deposit_product.max_limit = li.get('max_limit')
            deposit_product.save()
        else:
            # 존재하지 않는 경우, 새로운 객체 생성 및 저장
            save_data = {
                'fin_prdt_cd': li.get('fin_prdt_cd'),
                'dcls_month': li.get('dcls_month'),
                'kor_co_nm': li.get('kor_co_nm'),
                'fin_prdt_nm': li.get('fin_prdt_nm'),
                'etc_note': li.get('etc_note'),
                'join_deny': li.get('join_deny'),
                'join_member': li.get('join_member'),
                'join_way': li.get('join_way'),
                'spcl_cnd': li.get('spcl_cnd'),
                'max_limit': li.get('max_limit')
            }
            serializer_1 = DepositProductsSerializer(data=save_data)
            if serializer_1.is_valid(raise_exception=True):
                serializer_1.save()

    deposit_cd_savetrm_list = list(DepositOptions.objects.values_list('fin_prdt_cd', 'save_trm')) # 코드와 저축기간 담은 리스트 생성
    for li in response.get("result").get('optionList'):
        # DepositProducts 모델에서 fin_prdt_cd로 해당 상품을 조회하여 PK를 가져옴
        try:
            product_instance = DepositProducts.objects.get(fin_prdt_cd=li.get('fin_prdt_cd'))
            product_pk = product_instance.pk
        except DepositProducts.DoesNotExist:
            product_pk = None  # 해당 상품을 찾을 수 없는 경우
        fin_prdt_cd_2, save_trm = li.get('fin_prdt_cd') or -1, li.get('save_trm') or -1
        if (fin_prdt_cd_2, int(save_trm)) in deposit_cd_savetrm_list:
            deposit_options = DepositOptions.objects.get(fin_prdt_cd=fin_prdt_cd_2, save_trm=save_trm)
            # print(deposit_options)
            deposit_options.intr_rate = li.get('intr_rate') or -1
            deposit_options.intr_rate2 = li.get('intr_rate2')
        else:
            save_data_2 = {
                'product': product_pk,  # product_pk가 None이면 외래 키는 비워짐
                'fin_prdt_cd': li.get('fin_prdt_cd'),
                'intr_rate_type_nm': li.get('intr_rate_type_nm'),
                'intr_rate': li.get('intr_rate') or -1,
                'intr_rate2': li.get('intr_rate2'),
                'save_trm': li.get('save_trm'),
            }
            serializer_2 = DepositOptionsSerializer(data=save_data_2)
            if serializer_2.is_valid(raise_exception=True):
                serializer_2.save()

    return JsonResponse({'message':'okay'})

#################################################################################################################################

@api_view(['GET'])
def save_saving_products(request):  # requests 모듈을 활용하여 적금 상품 목록 데이터를 가져와 정기예금 상품 목록과 옵션 목록을 DB에 저장
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()
    saving_list = SavingProducts.objects.values_list('fin_prdt_cd', flat=True)
    for li in response.get("result").get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        if fin_prdt_cd in saving_list:
            # 이미 존재하는 경우, 필터링된 객체를 가져와 업데이트
            saving_product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            saving_product.dcls_month = li.get('dcls_month')
            saving_product.kor_co_nm = li.get('kor_co_nm')
            saving_product.fin_prdt_nm = li.get('fin_prdt_nm')
            saving_product.mtrt_int = li.get('mtrt_int')
            saving_product.etc_note = li.get('etc_note')
            saving_product.join_deny = li.get('join_deny')
            saving_product.join_member = li.get('join_member')
            saving_product.join_way = li.get('join_way')
            saving_product.spcl_cnd = li.get('spcl_cnd')
            saving_product.max_limit = li.get('max_limit')
            saving_product.save()
        else:
            # 존재하지 않는 경우, 새로운 객체 생성 및 저장
            save_data = {
                'fin_prdt_cd': li.get('fin_prdt_cd'),
                'dcls_month': li.get('dcls_month'),
                'kor_co_nm': li.get('kor_co_nm'),
                'fin_prdt_nm': li.get('fin_prdt_nm'),
                'mtrt_int': li.get('mtrt_int'),
                'etc_note': li.get('etc_note'),
                'join_deny': li.get('join_deny'),
                'join_member': li.get('join_member'),
                'join_way': li.get('join_way'),
                'spcl_cnd': li.get('spcl_cnd'),
                'max_limit': li.get('max_limit')
            }
            serializer_1 = SavingProductsSerializer(data=save_data)
            if serializer_1.is_valid(raise_exception=True):
                serializer_1.save()
    saving_cd_savetrm_list = list(SavingOptions.objects.values_list('fin_prdt_cd', 'save_trm', 'rsrv_type_nm'))
    for li in response.get("result").get('optionList'):
        # SavingProducts 모델에서 fin_prdt_cd로 해당 상품을 조회하여 PK를 가져옴
        try:
            product_instance = SavingProducts.objects.get(fin_prdt_cd=li.get('fin_prdt_cd'))
            product_pk = product_instance.pk
        except SavingProducts.DoesNotExist:
            product_pk = None  # 해당 상품을 찾을 수 없는 경우
        fin_prdt_cd_2, save_trm, rsrv_type_nm = li.get('fin_prdt_cd') or -1, li.get('save_trm') or -1, li.get('rsrv_type_nm')
        
        if (fin_prdt_cd_2, int(save_trm), rsrv_type_nm) in saving_cd_savetrm_list:
            saving_options = SavingOptions.objects.get(fin_prdt_cd=fin_prdt_cd_2, save_trm=save_trm, rsrv_type_nm=rsrv_type_nm)
            saving_options.intr_rate = li.get('intr_rate')
            saving_options.intr_rate2 = li.get('intr_rate2')
        else:
            save_data_2 = {
                'product': product_pk,  # product_pk가 None이면 외래 키는 비워짐
                'fin_prdt_cd': li.get('fin_prdt_cd'),
                'intr_rate_type_nm': li.get('intr_rate_type_nm'),
                'rsrv_type_nm':li.get('rsrv_type_nm'),
                'intr_rate': li.get('intr_rate') or -1,
                'intr_rate2': li.get('intr_rate2'),
                'save_trm': li.get('save_trm'),
            }
            serializer_2 = SavingOptionSerializer(data=save_data_2)
            if serializer_2.is_valid(raise_exception=True):
                serializer_2.save()

    return JsonResponse({'message':'okay'})

#################################################################################################################################

@api_view(['GET'])
def make_newdeposits(request):
    for product in DepositProducts.objects.all():
        options = DepositOptions.objects.filter(product=product.pk)
        new_table_data = {
            'dcls_month': product.dcls_month,
            'kor_co_nm': product.kor_co_nm,
            'fin_prdt_nm': product.fin_prdt_nm,
            'intr_rate_6': options.filter(save_trm=6).first().intr_rate if options.filter(save_trm=6).exists() else None,
            'intr_rate_12': options.filter(save_trm=12).first().intr_rate if options.filter(save_trm=12).exists() else None,
            'intr_rate_24': options.filter(save_trm=24).first().intr_rate if options.filter(save_trm=24).exists() else None,
            'intr_rate_36': options.filter(save_trm=36).first().intr_rate if options.filter(save_trm=36).exists() else None,
        }
        NewDeposits.objects.create(**new_table_data)
    return JsonResponse({'message':'okay'})


@api_view(['GET'])
def new_deposits(request):
    new_deposits = NewDeposits.objects.all()
    serializer = NewDepositSerializer(new_deposits, many=True)
    return Response(serializer.data)




########################################################


@api_view(['GET'])
def make_newsavings(request):
    for product in SavingProducts.objects.all():
        options_freedom = SavingOptions.objects.filter(product=product.pk, rsrv_type_nm='자유적립식')
        options_fixed = SavingOptions.objects.filter(product=product.pk, rsrv_type_nm='정액적립식')

        # 정액적립식 데이터 생성
        if options_fixed:
            new_table_data_fixed = {
            'dcls_month': product.dcls_month,
            'kor_co_nm': product.kor_co_nm,
            'fin_prdt_nm': product.fin_prdt_nm,
            'rsrv_type_nm': "정액적립식",
            'intr_rate_6': options_fixed.filter(save_trm=6).first().intr_rate if options_fixed.filter(save_trm=6).exists() else None,
            'intr_rate_12': options_fixed.filter(save_trm=12).first().intr_rate if options_fixed.filter(save_trm=12).exists() else None,
            'intr_rate_24': options_fixed.filter(save_trm=24).first().intr_rate if options_fixed.filter(save_trm=24).exists() else None,
            'intr_rate_36': options_fixed.filter(save_trm=36).first().intr_rate if options_fixed.filter(save_trm=36).exists() else None,
        }
            NewSavings.objects.create(**new_table_data_fixed)


        # 자유적립식 데이터 생성
        if options_freedom:
            new_table_data_freedom = {
                'dcls_month': product.dcls_month,
                'kor_co_nm': product.kor_co_nm,
                'fin_prdt_nm': product.fin_prdt_nm,
                'rsrv_type_nm': "자유적립식",
                'intr_rate_6': options_freedom.filter(save_trm=6).first().intr_rate if options_freedom.filter(save_trm=6).exists() else None,
                'intr_rate_12': options_freedom.filter(save_trm=12).first().intr_rate if options_freedom.filter(save_trm=12).exists() else None,
                'intr_rate_24': options_freedom.filter(save_trm=24).first().intr_rate if options_freedom.filter(save_trm=24).exists() else None,
                'intr_rate_36': options_freedom.filter(save_trm=36).first().intr_rate if options_freedom.filter(save_trm=36).exists() else None,
            }
            NewSavings.objects.create(**new_table_data_freedom)

    # 응답 주기
    return JsonResponse({'message': 'okay'})


@api_view(['GET'])
def new_savings(request):
    new_savings = NewSavings.objects.all()
    serializer = NewSavingSerializer(new_savings, many=True)
    return Response(serializer.data)








#################################################################################################################################



@api_view(['GET', 'POST'])
def deposit_products(request): # GET: 전체 정기예금 상품 목록 반환, POST: 상품 데이터 저장
    if request.method == 'GET':
        deposit_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_products, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def saving_products(request): # GET: 전체 정기예금 상품 목록 반환, POST: 상품 데이터 저장
    if request.method == 'GET':
        saving_products = SavingProducts.objects.all()
        serializer = SavingProductsSerializer(saving_products, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SavingProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd): # 특정 상품의 옵션 리스트 반환
    deposit_products_options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(deposit_products_options, many=True)
    return Response(serializer.data)










'''
from django.db.models import Max
@api_view(['GET'])
def top_rate(request): # 가입 기간에 상관없이 금리가 가장 높은 상품과 해당 상품의 옵션 리스트 출력
    max_intr_rate2 = DepositOptions.objects.aggregate(intr_rate2=Max('intr_rate2'))

    max_intr_rate_value = max_intr_rate2['intr_rate2']
    
    # 가장 높은 금리를 가진 상품의 옵션 정보를 가져옵니다.
    # top_rate_options = DepositOptions.objects.filter(intr_rate2 = max_intr_rate_value).first()
    # top_rate_options = DepositOptions.objects.filter(intr_rate2 = max_intr_rate_value)
    
    # 가장 높은 금리 상품 정보 가져옴
    # top_rate_products = DepositProducts.objects.get(pk=top_rate_options[0].product_id)
    # top_rate_products = top_rate_options.products.all()
    # 결과를 시리얼라이즈하거나 필요한 형식으로 가공한 후 반환합니다.
    # serializer = DepositProductsSerializer(top_rate_products)
    # serializer2 = DepositOptionsSerializer(top_rate_options)
    # serializers = [serializer.data,serializer2.data]

    # first() 로 중복되는 값이 있으면 첫번째 값만 받아옴
    tro = DepositOptions.objects.filter(intr_rate2 = max_intr_rate_value).first()
    trp = DepositProducts.objects.get(pk=tro.product_id)

    data = {
        'options': trp.options,
        'product': trp,
    }

    serializer = Test(data)
    return Response(serializer.data)
'''