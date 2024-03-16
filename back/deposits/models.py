from django.db import models


# 예금 모델
class DepositProducts(models.Model):
    fin_prdt_cd = models.CharField(max_length=200) # 금융 상품 코드
    dcls_month = models.IntegerField() # 공시 제출월 [YYYYMM]
    kor_co_nm = models.CharField(max_length=200) # 금융회사명
    fin_prdt_nm = models.CharField(max_length=200) # 금융 상품명
    etc_note = models.TextField() # 금융 상품 설명
    join_deny = models.IntegerField() # 가입 제한(1: 제한없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField() # 가입 대상
    join_way = models.TextField() # 가입 방법
    spcl_cnd = models.TextField() # 우대 조건
    max_limit = models.IntegerField(null=True) # 최고한도

    

# 예금 상품 옵션 모델 필드
class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, related_name='depositoptions',on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField() # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100) # 저축 금리 유형명
    intr_rate = models.FloatField() # 저축금리
    intr_rate2 = models.FloatField() # 최고우대금리
    save_trm = models.IntegerField() # 저축 기간(단위: 개월)



###########################################################################################################


# 적금 모델
class SavingProducts(models.Model):
    fin_prdt_cd = models.CharField(max_length=200) # 금융상품 코드
    dcls_month = models.IntegerField() # 공시 제출월 [YYYYMM]
    kor_co_nm = models.CharField(max_length=200) # 금융회사 명
    fin_prdt_nm = models.CharField(max_length=200) # 금융 상품명
    join_way = models.TextField() # 가입 방법
    mtrt_int = models.TextField() # 만기 후 이자율
    spcl_cnd = models.TextField() # 우대 조건
    join_deny = models.IntegerField() # 가입 제한(1: 제한없음, 2:서민전용, 3:일부제한)
    join_member	= models.TextField() # 가입 대상
    etc_note = models.TextField() # 기타 유의사항
    max_limit = models.IntegerField(null=True) # 최고한도

# 적금 상품 모델
class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, related_name='savingoptions',on_delete=models.CASCADE)
    fin_prdt_cd = models.CharField(max_length=200) # 금융상품 코드
    intr_rate_type_nm = models.CharField(max_length=100) # 저축 금리 유형명
    rsrv_type_nm = models.CharField(max_length=100) # 적립 유형명
    save_trm = models.IntegerField() # 저축 기간(단위: 개월)
    intr_rate = models.FloatField() # 저축금리
    intr_rate2 = models.FloatField() # 최고우대금리


###########################################################################################################

# 적금에 대한 새로운 테이블

class NewDeposits(models.Model):
    dcls_month = models.IntegerField()
    kor_co_nm = models.CharField(max_length=200)
    fin_prdt_nm = models.CharField(max_length=200)
    intr_rate_6 = models.FloatField(null=True, blank=True)
    intr_rate_12 = models.FloatField(null=True, blank=True)
    intr_rate_24 = models.FloatField(null=True, blank=True)
    intr_rate_36 = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.dcls_month} - {self.kor_co_nm} - {self.fin_prdt_nm}"

class NewSavings(models.Model):
    dcls_month = models.IntegerField()
    kor_co_nm = models.CharField(max_length=200)
    fin_prdt_nm = models.CharField(max_length=200)
    rsrv_type_nm = models.CharField(max_length=50)
    intr_rate_6 = models.FloatField(null=True, blank=True)
    intr_rate_12 = models.FloatField(null=True, blank=True)
    intr_rate_24 = models.FloatField(null=True, blank=True)
    intr_rate_36 = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.dcls_month} - {self.kor_co_nm} - {self.fin_prdt_nm} - {self.rsrv_type_nm}"

