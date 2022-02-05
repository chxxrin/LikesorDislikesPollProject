
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

- 따로 오류사항 존재하지 않으면 해당하는 아이를 dev를 향하게 merge 시키면 됩니다! 


1) master 브랜치
=> 최종 배포할 수 있을 정도로 완벽한 아이가 올라가는 브랜치

2) dev 브랜치
=> 우리가 기능 만들 때마다(수정의 가능성 존재하는 모든 코드들) push 할 브랜치
