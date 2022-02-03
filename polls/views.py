from ssl import OP_NO_TLSv1_1
from django.shortcuts import render, redirect
from .models import *

total_question_number = 10 # 총 질문의 갯수


def is_powerful(opt1, opt2) :
    if (opt1.count > opt2.count) :
        opt1.powerful = 1
        opt2.powerful = 0
        return 1
    else :
        opt1.powerful = 0
        opt2.powerful = 1
        return 0


def start_page(request) :
    total_voted_number = Choice.objects.get(id=1).count +Choice.objects.get(id=2).count # 총 투표한 사람들의 수
    return render(request, 'start.html', {'total_voted_number' : total_voted_number })


def main_page(request) :
    total_voted_number = Choice.objects.get(id=1).count +Choice.objects.get(id=2).count # 총 투표한 사람들의 수
    vote = Vote.objects.all()
    choice = Choice.objects.all()
    return render(request, 'main.html', {'vote':vote, 'choice':choice, 'total_voted_number' : total_voted_number })


def vote_page(request) :
    """
    투표 페이지로 가는 뷰
    """
    vote = Vote.objects.all()
    total_voted_number = Choice.objects.get(id=1).count +Choice.objects.get(id=2).count # 총 투표한 사람들의 수

    return render(request, 'vote.html', {'vote':vote, 'total_voted_number' : total_voted_number })


def vote(request):
    """
    1) 투표한 항목들 값 갱신
    2) 주류항목인 애들 골라서 powerful=1 로 필드값 설정
    3) 유저가 선택한 항목에서 주류 갯수 따라서 result 값 반환 
    """
    if request.method == "GET":

        # 1) 투표한 항목들 값 갱신

        voted_choice_id = []
        for j in range(1,total_question_number+1) :
            voted_choice_id.append(int(request.GET[f'choice{j}']))
        
        for i in voted_choice_id :
            voted_choice = Choice.objects.get(id=i)
            voted_choice.count+=1
            voted_choice.save()

        #2) 주류 항목인 애들 고르기& 유저가 택한 값 중에서 주류인 것 판별 (user_type으로 주류 선택한 것 갯수)

        user_type = 0
        for k in range(1, total_question_number//2 + 1) :
            if is_powerful(Choice.objects.get(id=k), Choice.objects.get(id=k+1)): #id=k가 주류인 경우
                if (voted_choice_id[k-1]==k) :
                    user_type+=1

        #3) user_type (주류 갯수 고른 것) 따라서 type 정해줌 (총 4 type 종류 있음)

        if user_type <= 1 :
            user_type_num = 1
        elif user_type <= 4 :
            user_type_num = 2
        elif user_type <= 7 :
            user_type_num = 3
        else : user_type_num = 4     

    return render(request, 'vote_complete.html', {'user_type_num' : user_type_num})


def vote_result(request, type_pk) : 
    return render(request, f'vote_result{type_pk}.html')

