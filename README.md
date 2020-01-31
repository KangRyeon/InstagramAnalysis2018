# InstagramAnalysis2018

# 기간
    1개월 (2018-07-28 ~ 2018-09-09)
    
    
    
# 개요
    많이 사용하는 단어에 따른 성별 분류가 가능한 지에 대해 알아보기 위해 
    인스타그램의 게시글을 분석하는 프로젝트를 진행했습니다.
    (미완)
    
    
# 사용한 라이브러리 및 구현 환경
    1. 구현 환경
        - Window 7
        - Python
    2. 사용한 라이브러리 및 기능
        - Google Vision API를 사용해 인물, 성별 탐지
        - KoNLP를 사용한 형태소 분석
        - openpyxl을 사용한 분석한 데이터 자동 문서화


# 필요 기능과 과정
    * 글에 대한 <본문 내용>과 그 글을 올린 사람의 <성별>에 대한 정보가 필요합니다.
    * <본문 내용>은 크롤링을 통해 수집할 수 있었으나, 
      <성별>은 인스타그램에서 정보를 공개하지 않기에 Google Vision API를 통해 분류했습니다.
      
    1. 게시글 이미지, 댓글, 본문 크롤링 기능
        - 오늘의 훈남, 얼스타그램, 셀스타그램, 예비군, 일상 등 자신에 대한 
          글을 많이 올렸을 법한 태그를 기준으로 검색해 크롤링합니다.
        - 크롤링한 정보를 openpyxl을 통해 자동으로 엑셀에 저장합니다.
    2. 이미지로 성별 분류하는 기능
        - id에 따른 성별 정보가 필요한데, 인스타그램 자체에 성별에 대한 정보가 없어 프로필 이미지
          , 그 사람의 게시글 이미지를 Google Vision API를 사용해 나온 label 값으로 성별을 분류했습니다.
          (girl, beauty, long hair, woman) / (boy, military, suit, man, male)
    3. 형태소 분석 기능
        - KoNLP, Gensim doc2vec을 사용해 본문과 댓글의 형태소를 분석했습니다.

# 구현 화면



# 주요 기능별 소스코드 설명
    instagram_crawling_1-1(txt_version).py : 인스타그램 게시글의 아이디, 태그, 본문 저장하기
        - instagrampost.txt : 코드 실행 후 검색된 게시글 전체의 url 저장.
        - instagram.txt : 코드 실행 후 [ 아이디 / 게시글 / 태그 ]를 저장.
    instagram_crawling_1-2(txt_version).py : 인스타그램 아이디에 따른 프로필 이미지 다운받기
        - instagrampost.txt가 있어야 함. => 1번 파일을 실행 후 저장된 것.
        - [크롤러] 폴더 : 코드 실행 후 각 아이디의 프로필 사진 저장.
        
    instagram_crawling_2-1(excel_version).py : 
