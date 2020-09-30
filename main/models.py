from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError
import re
from datetime import *


#　生年月日の未来日エラーチェック
def check_futureday(value):
    if value >= date.today() + timedelta(days = 1):
       raise ValidationError('本日以前の日付を入力してください')


# Create your models here.
class Employee(models.Model):

    employeeNum = models.IntegerField(
        verbose_name='社員番号',
        validators=[MinValueValidator(0, '0以上の番号を入力してください'), MaxValueValidator(99999, '99999以下の番号を入力してください')],
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
        validators=[RegexValidator(r"^[あ-ん]+$", 'ひらがなを入力してください')],
    )

    firstKanaName = models.CharField(
        verbose_name='名（かな）',
        max_length=20,
        validators=[RegexValidator(r"^[あ-ん]+$", 'ひらがなを入力してください')],
    )

    phoneNumber = models.CharField(
        verbose_name='電話番号',
        max_length=13,
        validators=[RegexValidator(r"^0[789]0-[0-9]{4}-[0-9]{4}$", '○○○-○○○○-○○○○の形式で入力してください')],
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
        validators=[check_futureday],
    )

    gender = models.CharField(
        verbose_name='性別',
        max_length=10,
        choices=[
            ('未選択', '未選択'),
            ('男性', '男性'),
            ('女性', '女性'),
        ],
        default='未選択',
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

