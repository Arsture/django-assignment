# seminar-2023-django-assignment
세미나 2023 Django 과제 제출 레포지토리.

Generic view로 하면 좋았을건데, viewset으로 저질러버렸습니다.
그래도 잘 작동합니다.

관련있는 것들은 하나의 앱으로 뭉치면 좋다는데,,,
죄송합니다

왜인진 모르겠지만 login 하는거는 django api web view에서만 되고, 로그아웃은 django admin에서만 됩니다.

그래서 django api web view에서 로그인하고, django admin에서 로그아웃하면 됩니다.

근데 admin이 아니면 admin 사이트에 못들어가니, 아래의 계정을 참조하시면 됩니다.

https://d704-14-36-38-134.ngrok-free.app/api/
로 접속가능합니다
---
https://d704-14-36-38-134.ngrok-free.app/admin/
으로 오면 admin으로 들어 올 수 있습니다
- email:
  - admin@naver.com
- password:
  - kms0102@
---
https://d704-14-36-38-134.ngrok-free.app/swagger/
swagger도 있긴합니다