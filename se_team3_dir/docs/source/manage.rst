manage.py
=============
* manage.py는 Djnago project를 수행하는데 필요한 다양한 기능을 지원합니다.

해당 파일은 Django Framework에서 기본적으로 제공하는 파일이고, 다양하고 유용한 명령어들을 포함합니다.

이 중에서 자주 사용하고, 필수적으로 사용할 수 있어야 하는 명령어만 몇가지 소개합니다.

runserver
----------------
* 가벼운 개발용 서버를 로컬로 실행합니다.
 Code::

    $ python3 manage.py runserver

터미널에서 runserver를 하게되면

IP : 127.0.0.1(default)과

port : 8000(default)

으로 접근해서 웹을 확인할 수 있습니다.

./manage.py runserver를 실행한 후 해당 주소로 접속한 모습
+++++++++++++++++++++
.. figure::  ./runserver_img.png
   :align:   center

   local address로 접근한 결과

makemigrations
----------------
*모델에 대해 탐지된 변경사항을 기반으로 새 마이그레이션을 만듭니다.

Code::

    $ python3 manage.py makemigrations


`마이그레이션 설명서 <https://docs.djangoproject.com/en/3.2/topics/migrations/>`_
에는 마이그레이션, 애플리케이션과의 관계 등이 자세히 설명되어 있습니다.


migrate
----------------
*데이터베이스 상태를 현재 모델 및 마이그레이션 집합과 동기화합니다.

Code::

    $ python3 manage.py migrate


`마이그레이션 설명서 <https://docs.djangoproject.com/en/3.2/topics/migrations/>`_
에는 마이그레이션, 애플리케이션과의 관계 등이 자세히 설명되어 있습니다.




manage.py에 대한 세부 명세
----------------------
Linking Space Project에서는 manage.py의 놀라운 기능들 중에 아주 일부만 사용하고 있습니다. 더 다양한 활용예시와 명령어가 궁금하다면 공식 문서를 참조하시기 바랍니다.

*Django Framework를 사용하게 된다면 기본적으로 제공하는 파일으로, 자세한 내용은 공식 문서를 참고하기 바랍니다.

`공식문서로 이동하기 <https://docs.djangoproject.com/en/3.2/ref/django-admin/>`_

.. automodule:: manage
   :members:
   :undoc-members:
   :show-inheritance: