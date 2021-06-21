test.py 모듈 (검사)
=================

링킹 스페이스에서 구현한 테스트 케이스 모듈입니다.

Webapp_test 클래스 내에 2개의 메소드(회원가입 검사, 로그인 검사)가 구현되어 있습니다.

회원가입 기능을 테스트 합니다.
++++++++++++++++++++++


response 객체의 status code

200 : 서버가 요청을 처리했다는 뜻입니다. 해당 요청은 view.py 내부의 test에서 문제가 발견되어 renter()함수를 통해 반환됩니다. 

302 : view.py 내부의 test에서 문제가 없이 redirection 되어 현재 서버가 다른 위치의 페이지로 요청에 응답합니다.

    1) 회원가입이 정삭적으로 수행된 경우 redirection을 통하여 response의 status code를 302로 반환합니다.

    2) 회원가입 항목 중 비밀번호와 비밀번호 확인 값이 동일하지 않은 경우 redirection 하지 않고 response의 status code를 200으로 반환합니다.
    
    3) 회원가입 항목 중 Null 값이 허용되지 않는 항목이 비어있을 경우 redirection 하지 않고 response의 status code를 200로 반환합니다.

구현 코드::

    def test_register(self):
        # 1. 회원가입이 정상적으로 이루어진 경우 입니다.
        response = client.post("/seuser/register/", info)
        self.assertEqual(response.status_code, 302)
        print("\n")
        print(" test_register - 1 : PASS")

        # 2. 비일번호와 비밀번호 확인 항목이 일치하지 않을 경우 입니다.
        info_2 = { 'user_id' : 'rlagmlgus115',
        'user_name' : '김희현',
        'user_email' : 'rlagmlgus115@gmail.com',
        'password' : 'redbull250',
        're-password' : 'no match',
        'user_sex' : '남자',
        'user_age' : 25,
        'user_address' : '광주광역시 북구 첨단과기로 235',
        'user_interest' : '보컬 트레이닝'
        }
        
        response = client.post("/seuser/register/", info_2)
        self.assertEqual(response.status_code, 200)
        print(" test_register - 2 : PASS")


        # 3. 회원가입 항목에 공백이 존재하는 경우 입니다. (Null 허용 항목 제외)
        info_3 = { 
        'password' : 'redbull250',
        're-password' : 'redbull250',
        'user_sex' : '남자',
        'user_age' : 25,
        'user_address' : '광주광역시 북구 첨단과기로 235',
        'user_interest' : '보컬 트레이닝'
        }
        
        response = client.post("/seuser/register/", info_3)
        self.assertEqual(response.status_code, 200)
        print(" test_register - 3 : PASS")



로그인 기능을 테스트 합니다.
+++++++++++++++++++++

response 객체의 status code

200 : 서버가 요청을 처리했다는 뜻입니다. 해당 요청은 view.py 내부의 test에서 문제가 발견되어 renter()함수를 통해 반환됩니다. 

302 : view.py 내부의 test에서 문제가 없이 redirection 되어 현재 서버가 다른 위치의 페이지로 요청에 응답합니다.

    1) 로그인이 정삭적으로 수행된 경우 redirection을 통하여 response의 status code를 302로 반환합니다.
        
    2) 아이디와 비밀번호 중 하나를 입력하지 않은 경우 redirection 하지 않고 response의 status code를 200으로 반환합니다.
        
    3) 아이디에 대한 비밀번호가 일치하지 않은 경우 redirection 하지 않고 response의 status code를 200로 반환합니다.
        
    4) 입력한 아이디가 존재하지 않을 경우 redirection 하지 않고 response의 status code를 200으로 반환합니다.
구현::

    def test_login(self):
            
            # 1. 로그인이 정상적으로 수행된 경우입니다.
            response = client.post("/seuser/register/", info)

            test_login_data = {
                'user_id' : 'rlagmlgus115',
                'password' : 'redbull250',
            }

            response = client.post("/seuser/login/", test_login_data)
            self.assertEqual(response.status_code, 302)
            print("\n")
            print(" test_login - 1 : PASS")


            # 2. 모든 값을 입력하지 않은 경우입니다.
            test_login_data = {
                'password' : 'redbull250',
            }
            response=client.post("/seuser/login/", test_login_data)
            self.assertEqual(response.status_code, 200)
            print(" test_login - 2 : PASS")

            # 3. 비밀번호가 일치하지 않는 경우입니다.
            test_login_data = {
                'user_id' : 'rlagmlgus115',
                'password' : 'no match',
            }
            response=client.post("/seuser/login/", test_login_data)
            self.assertEqual(response.status_code, 200)
            print(" test_login - 3 : PASS")


            # 4. 아이디가 존재하지 않는 경우입니다.
            test_login_data = {
                'user_id' : 'no body',
                'password' : 'redbull250',
            }
            response=client.post("/seuser/login/", test_login_data)
            self.assertEqual(response.status_code, 200)
            print(" test_login - 4 : PASS")

.. automodule:: manage
   :members:
   :undoc-members:
   :show-inheritance: