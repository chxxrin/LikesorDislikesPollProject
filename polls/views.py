from django.shortcuts import render
from .models import *

total_question_number = 10 # 총 질문의 갯수

def is_powerful(opt1, opt2) :
    # 1번과 2번이 같으면 -1 반환
    if (opt1.count == opt2.count) :
        opt1.powerful=True
        opt2.powerful=True
        opt1.save()
        opt2.save()
        return -1

    # 1번이 2번보다 많으면 1 반환
    elif (opt1.count > opt2.count) :
        opt1.powerful = True
        opt2.powerful = False
        opt1.save()
        opt2.save() 
        return 1
    
    # 1번이 2번보다 작으면 0 반환
    else :
        opt1.powerful = False
        opt2.powerful = True
        opt1.save()
        opt2.save()
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
            voted_choice.count+=1 # 내 선택 반영
            voted_choice.save()

        #2) 주류 항목인 애들 고르기& 유저가 택한 값 중에서 주류인 것 판별 (user_type으로 주류 선택한 것 갯수)

        user_type = 0
        for k in range(1, total_question_number*2,2) :
            powerful = is_powerful(Choice.objects.get(id=k), Choice.objects.get(id=k+1))

            # k번 > k+1번 : k번이 주류
            if (powerful == 1):
                if (voted_choice_id[k//2] == k): # 내 선택이 k일 때
                    user_type += 1

            # k번 < k+1번 : k+1번이 주류
            elif (powerful == 0):
                if (voted_choice_id[k//2] == k+1): # 내 선택이 k+1일 때
                    user_type += 1

            # k번 = k+1번 : 둘다 주류
            else:
                user_type += 1 # 내 선택에 상관없이

        #3) user_type (주류 갯수 고른 것) 따라서 type 정해줌 (총 4 type 종류 있음)

        if user_type <= 1 :
            user_type_num = 1
        elif user_type <= 4 :
            user_type_num = 2
        elif user_type <= 7 :
            user_type_num = 3
        else : user_type_num = 4

        #4) 내가 선택한 아이디값

        final_choice_list=[]
        for i in voted_choice_id:
            final_choice_list.append(Choice.objects.get(id=i))

        return render(request, 'vote_result.html', {'type_pk':user_type_num, 'user_type':user_type, 'final_choice_list' : final_choice_list})