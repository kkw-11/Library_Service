# -*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', db='eliceproject', charset='utf8') 
cursor = conn.cursor() 

print("dbconnection!!")
# book_name	publisher	author	publication_date	pages	isbn	description	link





# sql = '''
#     INSERT INTO BOOK(book_name, publisher, author, publication_date, pages, isbn, description, link)
#     VALUES ("주니어를 위한 최선의 코딩 학습 똑똑한 파이썬",	"코딩스쿨(인포앤북)", "황재호/황예린", "2019-07-01", "240", "9791196440916",
#     "주니어의 코딩 학습을 위한 최상의 파이썬 학습서
# 초등학교에서 스크래치, 엔트리 등의 블록코딩으로 알고리즘의 기초를 배우고 난 후 글자로 된 텍스트 코딩 단계에 들어가면 아이들이 어려워하게 된다. 
# 이 책은 동물 일러스트를 활용하고 쉽고 재미있는 예제들을 많이 수록하여 아이들이 혼자서 재미있게 코딩을 공부할 수 있도록 하였다. 또한 이 책은 파이썬 코딩과 
# 알고리즘에 대한 기초 지식이 없는 초등학교 고학년생과 중학생들을 대상으로 한 코딩 및 알고리즘 수업의 교재로 활용하기 적합하게 집필되었다.",	
# "http://codingschool.info/book/index.php?book=smart_python")
# '''

# sql = '''
#     INSERT INTO BOOK(book_name, publisher, author, publication_date, pages, isbn, description, link)
#     VALUES(	"	혼자 공부하는 자바	"	,	"	한빛출판네트워크	"	,	"	신용권	"	,	"	2019-06-10	"	,	"	708	"	,	"	9791162241875	"	,	"혼자 해도 충분하다! 1:1 과외하듯 배우는 자바 프로그래밍 자습서 (JAVA 8 &11 지원) 

# 이 책은 독학으로 자바를 배우는 입문자가 ‘꼭 필요한 내용을 제대로’ 학습할 수 있도록 구성했다. ‘무엇을’ ‘어떻게’ 학습해야 할지 조차 모르는 입문자의 막연한 마음을 살펴, 과외 선생님이 알려주듯 친절하게, 그러나 핵심적인 내용만 콕콕 집어준다. 책의 첫 페이지를 펼쳐서 마지막 페이지를 덮을 때까지, 혼자서도 충분히 자바를 배울 수 있다는 자신감과 확신이 계속될 것이다!

 

# 20명의 베타리더 검증으로, ‘함께 만든’ 입문자 맞춤형 도서

# 20명의 베타리더와 함께 구성하여 입문자에게 맞는 난이도, 분량, 학습 요소 등을 적극 반영했다. 어려운 용어와 개념은 한번 더 풀어 쓰고, 복잡한 설명은 눈에 잘 들어오는 그림으로 풀어 냈다. ‘혼자 공부해본’ 여러 입문자의 초심과 눈높이가 책 곳곳에 반영된 것이 이 책의 가장 큰 장점이다."	,	"	https://www.hanbit.co.kr/store/books/look.php?p_code=B5635758676	"	)	,
# (	"	파이썬 라이브러리를 활용한 데이터 분석	"	,	"	한빛출판네트워크	"	,	"	웨스 맥키니	"	,	"	2019-05-20	"	,	"	664	"	,	"	9791162241905	"	,	"빅데이터 분석에 관한 가장 완벽한 교재! 

 

# 이 책은 NumPy, pandas, matplotlib, IPython, Jupyter 등 다양한 파이썬 라이브러리를 사용해서 효과적으로 데이터를 분석하는 방법을 알려준다. pandas의 새로운 기능뿐만 아니라 메모리 사용량을 줄이고 성능을 개선하는 고급 사용법까지 다룬다. 또한 모델링 도구인 statsmodels와 scikit-learn 라이브러리도 소개한다. 연대별 이름 통계 자료, 미 대선 데이터베이스 자료 등 실사례로 따라 하다 보면 어느덧 여러분도 데이터에 알맞게 접근하고 효과적으로 분석하는 전문가가 될 것이다. 

 

 

# 『파이썬 라이브러리를 활용한 데이터 분석』 드디어 개정!

 
# 이 책의 초판이 출간된 2012년은 pandas 개발 초기로, 파이썬용 오픈소스 데이터 분석 라이브러리가 흔하지 않았습니다. 이번에 pandas의 새로운 기능과 5년여간의 세월이 흐르는 동안 낡았거나 사용법이 바뀐 내용을 모두 반영하여 책 전반을 다시 다듬었습니다. 또한 당시에는 존재하지 않았거나 책에 싣기에는 불안했던 갓 나온 도구들을 새로 소개하는 내용을 추가했습니다. 2판의 주요 변경 사항은 다음과 같습니다."	,	"	https://www.hanbit.co.kr/store/books/look.php?p_code=B6417848794	"	)	,
# (	"	이것이 리눅스다 	"	,	"	한빛출판네트워크	"	,	"	우재남	"	,	"	2020-04-10	"	,	"	812	"	,	"	9791162242605	"	,	"리눅스 분야 5년간 부동의 1위,『이것이 리눅스다』최신 CentOS 8을 반영한 개정판 출간!

 

# 2015년 출간 후 리눅스 도서 분야 부동의 베스트셀러 1위를 지켜오던 『이것이 리눅스다』가 CentOS 8 버전을 반영하여 개정되었다. 1판보다 더욱 현장감 넘치는 실무 예제와 함께 리눅스의 ‘1층부터 옥상까지’ 탄탄히 기초를 쌓으며 올라가듯 상세한 실습 과정을 담았다.

 

 

# 실무형 리눅스 교재 + 50여개 무료 동영상 강좌+ 네이버 카페를 통한 저자 응답 서비스 = 독학 리눅서를 위한 완벽 패키지 제공!

 

# 이 책은 1대의 컴퓨터만으로도 실무와 똑같은 환경처럼 학습 가능하도록 구성된 실무형 리눅스 교재다. 따라서 실습 없이 지나치기 쉬운 서버 구축도 직접 따라해보며 실무 적응력을 높일 수 있다. 또 책만으로는 이해하기 어려운 실습도 무료로 제공되는 50여 개의 [저자 동영상 강의]를 보며 더욱 쉽게 익힐 수 있다. 그래도 어려운 부분이 있다면, 회원수 1만 명의 [이것이 리눅스다 네이버 카페]에 질문을 올려도 좋다. 저자가 직접 모든 질문에 1:1로 답변을 달아주며, 리눅스 최신 기술도 공유할 수 있다.   

# 이번 개정판도 ‘책 내용만 그대로 따라한다면 처음부터 마지막 장까지 막힘없이 실습 가능할 것’을 보장한다. 이제, 독학 리눅서를 위한 최고의 패키지와 함께 리눅스의 세계로 자신있게 진입하자!"	,	"	https://www.hanbit.co.kr/store/books/look.php?p_code=B8529915277	"	)	,
# (	"	혼자 공부하는 첫 프로그래밍 파이썬	"	,	"	한빛출판네트워크	"	,	"	문헌일	"	,	"	2020-06-30	"	,	"	336	"	,	"	9791162243039	"	,	"비전공자도 ‘혼공’ 할 수 있다!

# 1:1 과외하듯 배우는 왕초보 코딩 입문서

 

# 유튜브 강의! 그림으로 보여주는 ‘눈코딩’ 예제! 프로그램 설치 없이 온라인 실습! 부록 용어 노트! 이 모든 것을 제공하기에 비전공자도 프로그래밍을 독학할 수 있습니다.

# 이 책은 비전공자가 시중에 나온 프로그래밍 책을 이해할 수 있게, 기존 입문서보다 더 기초부터 알려줍니다. 프로그래밍을 배우기 전 알아야 하는 문법 원리를 비전공자의 눈높이에 맞춰 그림으로 보는 ‘눈코딩’으로 보여주고, 직접 따라 해보는 짧은 ‘손코딩’으로 연습합니다. 일상생활 속 친근한 예시로 프로그래밍이 어디에서 어떻게 쓰이는지를 알게 해, 이해가 쉽고 동기 부여가 됩니다."	,	"	https://www.hanbit.co.kr/store/books/look.php?p_code=B9609283195	"	)
    
    
#     '''



# sql = '''
#     CREATE TABLE BookComment(
#         id int(100) NOT NULL,
#         book_id int(100) NOT NULL,
#         email varchar(255) NOT NULL,
#         content text NOT NULL,
#         rating int NOT NULL,
#         PRIMARY KEY (id),

#         FOREIGN KEY (book_id) REFERENCES book (book_id)
#         )
#     '''


###############################################

# sql = '''
#     CREATE TABLE book(
#         book_id int(100) NOT NULL AUTO_INCREMENT PRIMARY KEY,
#         book_name varchar(255) NOT NULL,
#         publisher varchar(255) NOT NULL,
#         author varchar(255) NOT NULL,
#         publication_date date NOT NULL,
#         pages varchar(255) NOT NULL,
#         isbn varchar(255) NOT NULL,
#         description text,
#         link varchar(255),
#         remaining int
#     )
# '''

# sql = '''
#     CREATE TABLE user (
#         user_id int(100) NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
#         email varchar(255) NOT NULL  UNIQUE ,
#         password varchar(100) NOT NULL,
#         name varchar(100) NOT NULL

#     )
#     '''

# sql = '''
# CREATE TABLE borrowbook(
# id int(100) NOT NULL AUTO_INCREMENT PRIMARY KEY,
# book_id int(100) NOT NULL,
# email varchar(255) NOT NULL,
# rental_date DATE NOT NULL,
# return_date DATE
# )
# '''


# sql = '''
#     INSERT INTO user(email, password, name)
#     VALUES('elice@elice.kr', '1234', 'elice')
# '''

# sql = '''
#     CREATE TABLE bookcomment(
#         id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
#         book_id int NOT NULL,
#         email varchar(255) NOT NULL,
#         content text NOT NULL,
#         rating int
#     )
# '''

sql = '''alter table book add rating int;'''


cursor.execute(sql) 
conn.commit() 
conn.close() 