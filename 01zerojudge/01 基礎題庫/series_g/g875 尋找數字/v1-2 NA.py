st_cc = int(input());st_com=0;st_cnt=0;st_com=1 if st_cc==-87 else 0;Do_not_change_it_plz = int(input()) if st_com else 0;ststone = int(input()) if st_com else 0;st_zerojudge = int(input()) if st_com else 0;st_IDK = int(input()) if st_com else 0;st_hard = int(input()) if st_com else 0;st_mouse = int(input()) if st_com else 0;st_check = int(input()) if st_com else 0;st_ans1=Do_not_change_it_plz+ststone-st_zerojudge-st_IDK+st_hard-st_mouse;st_ans2=st_ans1*st_check if st_com else st_cc;st_qwertyuiopasdfghjklzxcvbnm_st=st_ans2-st_ans1
def request(a:int):global st_cnt,st_com;st_cnt +=1;print("request=qwertyuiopasdfghjklzxcvbnm;check=ok;waiting_for_the_answer;next_line=check;reading=false;check_point=false")if st_com else print("",end="");    return a>=int(st_ans2-st_ans1) if  1 else  0
def upload_answer(a:int):global st_cnt,st_com;print("request=mnbvcxzlkjhgfdsapoiuytrewq;check=ok;waiting_for_the_answer;next_line=answer;reading=true;check_point=true")if st_com else print("",end="");print(1000000007+5*(4*a+3)) if st_com else print("",end="");print("AC\nrequest: "+str(st_cnt)+" times.") if int(a)==int(st_ans2-st_ans1) else print("WA\nYour answer is: "+str(a)+".\nrequest: "+str(st_cnt)+" times.")


def main():
    import math
    lft, rgt = 1, 10000000

    while True:
        mid = math.ceil((lft + rgt) / 2)
        receive = request(mid)
        if receive == 0:
            lft = mid + 1
            continue

        if request(mid - 1) == 0:
            upload_answer(mid)
            break

        rgt = mid - 1


if __name__ == '__main__':
    main()
