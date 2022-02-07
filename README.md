
# 클론 받기 & 실행하기
1) git clone -b dev https://github.com/LikelionSideProj/vs
2) cd vs
3) pip install -r requirements.txt
4) python manage.py migrate => runserver
5) 각자 브랜치 파서 작업한 후 (git branch 브랜치이름) - 브랜치이름은 내가 만들 기능명..?ㅎㅎ 자유입니당!!
6) 그 브랜치로 이동해서 작업 진행 (git switch 브랜치이름) & 그 브랜치에서 git add . & git commit -m "작업내용"
7) 작업 구현완료됐으면 git push origin 브랜치이름
8) 깃허브 와서 pull request 떠있을텐데 그거 생성! (이때 향하는 브랜치가 master이 아닌 dev가 되게 해주세욥!)
9) pull request 보고 conflict 없고, 문제없고 다른 팀원들도 그 코드보고 문제없다 생각하면
10) merge 시켜주고 작업한 브랜치 삭제(깃허브에서 삭제  가능해욥!ㅎㅎ)

# 업데이트 된 사항 있으면 pull 하면서 작업하기!
`git pull origin dev`로 dev 브랜치에 업데이트된 아이들 받아오면서 작업해주시면 됩니다!

# db 등록
-> admin 페이지에서 Vote 모델 10개 (우리가 보여줄 질문의 갯수-이름은 상관 x 걍 번호로 붙이는 것도 상관 없어용 ㅎㅎ)
-> Choice 모델 만들 때 한 Vote 당 2개의 Choice 가 존재할 수 있도록 만들어주면 됩니당!
- 아래와 같이 Choice 만들 때 얘가 속할 Vote 선택해주면 됩니당 ! 1번 질문에 민초 vs 반민초 를 하고 싶으니깐 1번 vote를 외래키로 가지는 choice 모델 두개 (민초, 반민초) 를 만들어주면 되겠죵!?

![image](https://user-images.githubusercontent.com/76711238/152468763-17c1fea1-4e57-41b7-9291-ef83b40663da.png)

![image](https://user-images.githubusercontent.com/76711238/152468781-77a930d8-0cf4-4f8d-840b-63b66b42ef9c.png)


# (+) Git 브랜치 두개로 나눠서 작업합시다! 😎
- 그리고 기능 만들 때는 각자 브랜치 만들어서 (브랜치명은 프론트면 `fe/기능명` , 백이면 `be/기능명` 정도? 너무 딱딱하게 지키시진 않아도 돼욥 ㅎㅎ) 작업하고
`git push origin 자신의브랜치이름` 으로 pull request 만든 다음에 이 pull request가 `dev`로 향하도록 설정해주면 됩니다!!

- 따로 오류사항 존재하지 않으면 해당하는 아이를 dev를 향하게 merge 시키면 됩니다! 


1) master 브랜치
=> 최종 배포할 수 있을 정도로 완벽한 아이가 올라가는 브랜치

2) dev 브랜치
=> 우리가 기능 만들 때마다(수정의 가능성 존재하는 모든 코드들) push 할 브랜치
