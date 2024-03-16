from django.db import models

# Create your models here.

class Exchange_rate(models.Model):
    cur_unit = models.CharField(max_length=100)	# String 통화코드	
    cur_nm	= models.CharField(max_length=250)	# 국가/통화명	
    ttb	= models.CharField(max_length=250)	# 전신환(송금) 받으실때	
    tts	= models.CharField(max_length=250)	# 전신환(송금) 보내실때	
    deal_bas_r = models.CharField(max_length=250)	# 매매 기준율	
    bkpr = models.CharField(max_length=250)	# 장부가격	
    yy_efee_r = models.CharField(max_length=250)	# 년환가료율	
    ten_dd_efee_r = models.CharField(max_length=250)	# 10일환가료율	
    kftc_deal_bas_r	= models.CharField(max_length=250)	# 서울외국환중개 매매기준율	
    kftc_bkpr = models.CharField(max_length=250)	# 서울외국환중개 장부가격
