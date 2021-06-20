import json
import unittest
from django.test import TestCase
from django.test import Client
from .models import Seuser
from django.contrib.auth import get_user_model
from django.urls import reverse

# 웹 어플리케이션의 기능을 테스트 합니다.

info = { 'user_id' : 'rlagmlgus115',
    'user_name' : '김희현',
    'user_email' : 'rlagmlgus115@gmail.com',
    'password' : 'redbull250',
    'user_sex' : '남자',
    'user_age' : 25,
    'user_address' : '광주광역시 북구 첨단과기로 235',
    'user_interest' : '보컬 트레이닝'
    }

client = Client()

class Webapp_test(TestCase):
    def test_register(self):
        """
        회원가입 기능을 테스트 합니다.
        """

        response = client.post("/templetes/register", json.dumps(info), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)


    def test_login(self):
        """
        로그인 기능을 테스트 합니다.`
        """
        client.post("/templates/register", json.dumps(info), content_type = 'application/json')
        
        test_login_data = {
            'user_id' : 'rlagmlgus115',
            'password' : 'redbull250',
        }

        response = client.post("/templetes/login/", json.dumps(test_login_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_mv_category_page(self):
        """
        주화면에서 해당 카테고리 화면으로의 이동을 테스트 합니다.
        """
        return 1

    def test_mv_detailed_place_page(self):
        """
        해당 카테고리 화면에서 세부 장소 화면으로의 이동을 테스트 합니다.
        """
        return 1
    
    def back_to_main_page(self):
        """
        카테고리 화면과 세부 장소 화면에서 주화면으로의 이동을 테스트 합니다.
        """
        return 1

