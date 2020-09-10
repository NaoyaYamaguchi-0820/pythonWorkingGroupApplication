from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Employee(models.Model):

    employeeNum = models.IntegerField(
        verbose_name='社員番号',
        validators=[MinValueValidator(0), MaxValueValidator(99999)],
    )

    lastName = models.CharField(
        verbose_name='氏（漢字）',
        max_length=20,
    )

    firstName = models.CharField(
        verbose_name='名（漢字）',
        max_length=20,
    )

    lastKanaName = models.CharField(
        verbose_name='氏（かな）',
        max_length=20,
    )

    firstKanaName = models.CharField(
        verbose_name='名（かな）',
        max_length=20,
    )

    phoneNumber = models.CharField(
        verbose_name='電話番号',
        max_length=11,
    )

    email = models.EmailField(
        verbose_name='eメールアドレス',
        max_length=100,
    )

    password = models.CharField(
        verbose_name='パスワード',
        max_length=20,
    )

    birthday = models.DateField(
        verbose_name='誕生日',
    )

    gender = models.BooleanField(
        verbose_name='性別',
    )

    section = models.CharField(
        verbose_name='部署',
        max_length=20,
        choices=[
            ('役員','役員'),
            ('イノベーション推進室','イノベーション推進室'),
            ('市場開発部','市場開発部'),
            ('経営管理本部','経営管理本部'),
            ('公共事業本部','公共事業本部'),
            ('システム開発事業部','システム開発事業部'),
        ]
    )

    jikoShokai = models.TextField(
        verbose_name='自己紹介',
        max_length=255,
    )
