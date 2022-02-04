
# 실행하기
1) git clone -b dev https://github.com/LikelionSideProj/vs
2) cd vs
3) pip install -r requirements.txt
4) python manage.py migrate => runserver

-> admin 페이지에서 Vote 모델 10개 (우리가 보여줄 질문의 갯수-이름은 상관 x 걍 번호로 붙이는 것도 상관 없어용 ㅎㅎ)
-> Choice 모델 만들 때 한 Vote 당 2개의 Choice 가 존재할 수 있도록 만들어주면 됩니당!
- 아래와 같이 Choice 만들 때 얘가 속할 Vote 선택해주면 됩니당 ! 1번 질문에 민초 vs 반민초 를 하고 싶으니깐 1번 vote를 외래키로 가지는 choice 모델 두개 (민초, 반민초) 를 만들어주면 되겠죵!?

![image](https://user-images.githubusercontent.com/76711238/152468763-17c1fea1-4e57-41b7-9291-ef83b40663da.png)

![image](https://user-images.githubusercontent.com/76711238/152468781-77a930d8-0cf4-4f8d-840b-63b66b42ef9c.png)


# (+) Git 브랜치 두개로 나눠서 작업합시다! 😎
- 그리고 기능 만들 때는 각자 브랜치 만들어서 (브랜치명은 프론트면 `fe/기능명` , 백이면 `be/기능명` 정도로만..) 작업하고
`git push origin 자신의브랜치이름` 으로 pull request 만든 다음에 이 pull request가 `dev`로 향하도록 설정해주면 됩니다!!

1) master 브랜치
=> 최종 배포할 수 있을 정도로 완벽한 아이가 올라가는 브랜치

2) dev 브랜치
=> 우리가 기능 만들 때마다(수정의 가능성 존재하는 모든 코드들) push 할 브랜치

**PR 만드는 방법**

1) 한 기능을 생성할 때마다 `git branch feature/내가하고자하는기능` 으로 가지 생성 

2) `git swtich 가지이름` 으로 해당 가지에서 기능 작업

3) 해당 가지에서 작업이 완료되면 (모든 커밋 완료) → `**git push origin 내가작업한가지이름**`  적어주면 pull request가 github에 옵니당! (아래 이미지의 초록색 부분 눌러주면 됨)

- **3) 에 대한 이미지 첨부**
    
   ![image](https://user-images.githubusercontent.com/76711238/152401741-f91a257a-f562-41c0-bf2a-f50463fbadaa.png)
    

4) `pull request`  만들어서 올려주기! 

- **4) 에 대한 이미지 첨부**
    
    **base가 디폴트로 main으로 되어있을텐데**
    
    ![image](https://user-images.githubusercontent.com/76711238/152401647-372063d5-49f3-4525-b333-e773143cce96.png)
    
    - 아래와 같이 눌러서 fe, be 브랜치로 변경해주어야 해용~~!! (dev는 be,fe 작업 마무리되면 합칠공간!!)
    
    ![image](https://user-images.githubusercontent.com/76711238/152401700-9fca7ece-4cce-473c-8a28-5216a818e2b1.png)
    

5) `pull request` 온 부분을 상대방이 읽어주고 의문점, 발견한 에러 같은 것 리뷰해주고 → pr 보낸 분이 해당 부분 답변, 수정하고 → `squash and merge` !! ~~
