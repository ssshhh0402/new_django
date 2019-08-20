from django.db import models

# Create your models here.

# 기본 모델을 받아서 나만의 아티클을 생성한다는 느낌

# 1. 모델(스키마) 정의
# 데이터베이스 테이블을 정의하고, 
# 각각의 컬럼(혹은 필드)를 정의
class Article(models.Model):    # models.Model 을 상속 받는 형식으로 쓴다. ~.~.get()으로 앞으로 데이터 사용하는게 여기 들어있거든
    # id : integer 자동으로 정의(Primary Key)
    # id = models.AutoField(primary_key=True) -> Integer 값이 자동으로 하나씩 증가 (AUTOINCREMENT)
    # CharField -  필수인자로 max_length 지정
    title = models.CharField(max_length=10)  # 기사의 제목을 변수값으로 가지는데 그것은 캐릭터 필드이다. (일종의 스키마를 정의하는거야)
    content = models.TextField()
    # DateTimeField
    #   auto_now_add : 생성시 자동으로 저장
    #   auto_now : 수정시마다 자동으로 저장
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      # 이런식으로 다양한 필드 생성 가능. 다 쓰고나서 
                                                          # python manage.py makemigrations 해서 마이그레이션 파일 생성 (소원쪽지 같은거라고 보면 된다.) 이러면 migrations 파일이 만들어질거고
                                                          # python manage.py migrate 그 소원쪽지를 적용시켜줘! - db에 반영!
    def __str__(self):
        return f'<{self.id}> : {self.title}'

# models.py에서 - python 클래스 정의
#               - 모델 설계도
# makemigrations - migration 파일 생성
#                - DB 설계도 작성 !
# migrate - 위의 설계도, migration 파일 DB 반영