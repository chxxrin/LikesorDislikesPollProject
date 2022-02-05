from calendar import c
from email import message
from ssl import OP_NO_TLSv1_1
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

total_question_number = 10 # 총 질문의 갯수


def is_powerful(opt1, opt2) :
    if (opt1.count > opt2.count) :
        opt1.powerful = True
        opt2.powerful = False
        opt1.save()
        opt2.save()
        return 1
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
        not_answered = []
        for j in range(1,total_question_number+1) :
            if (request.GET.get(f'choice{j}') == None):
                not_answered.append(int(j)) # 투표 안한 항목 번호
            else:
                voted_choice_id.append(int(request.GET[f'choice{j}']))

        if(len(not_answered) != 0): # 투표 다 안한 경우
            messages.warning(request, "모든 항목에 투표해주세요.")
            vote = Vote.objects.all()
            total_voted_number = Choice.objects.get(id=1).count +Choice.objects.get(id=2).count # 총 투표한 사람들의 수
            return render(request, 'vote.html',{'vote':vote, 'total_voted_number' : total_voted_number, 'answered' : voted_choice_id})
            
        else: # 10개 다 선택한 경우
            for i in voted_choice_id :
                voted_choice = Choice.objects.get(id=i)
                voted_choice.count+=1
                voted_choice.save()

            #2) 주류 항목인 애들 고르기& 유저가 택한 값 중에서 주류인 것 판별 (user_type으로 주류 선택한 것 갯수)

            user_type = 0
            for k in range(1, total_question_number*2,2) :
                if is_powerful(Choice.objects.get(id=k), Choice.objects.get(id=k+1)): #id=k가 주류인 경우
                    if (voted_choice_id[k//2]==k) :
                        user_type+=1
                else :
                    if (voted_choice_id[k//2]==k+1):
                        user_type+=1

            #3) user_type (주류 갯수 고른 것) 따라서 type 정해줌 (총 4 type 종류 있음)

            if user_type <= 1 :
                user_type_num = 1
            elif user_type <= 4 :
                user_type_num = 2
            elif user_type <= 7 :
                user_type_num = 3
            else : user_type_num = 4

            #4) 내가 선택한 아이디값

            v1=voted_choice_id[0]
            v2=voted_choice_id[1]
            v3=voted_choice_id[2]
            v4=voted_choice_id[3]
            v5=voted_choice_id[4]
            v6=voted_choice_id[5]
            v7=voted_choice_id[6]
            v8=voted_choice_id[7]
            v9=voted_choice_id[8]
            v10=voted_choice_id[9]
     
            return render(request, 'vote_complete.html',{'user_type_num' : user_type_num, 'v1':v1, 'v2':v2, 'v3':v3, 'v4':v4, 'v5':v5, 'v6':v6, 'v7':v7, 'v8':v8, 'v9' :v9, 'v10' : v10 })


def vote_result(request, type_pk, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10) : 
    final_choice_list=[]
    for i in [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]:
        final_choice_list.append(Choice.objects.get(id=i))
    return render(request, f'vote_result{type_pk}.html', {'final_choice_list' : final_choice_list, 'c1':c1,'c2':c2, 'c3':c3, 'c4':c4, 'c5':c5, 'c6':c6, 'c7':c7, 'c8':c8, 'c9':c9, 'c10':c10})
