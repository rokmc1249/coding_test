def recursive_func(i):
    if i==15:
        print(i,'번째 재귀함수를 종료합니다.')
        return
    print(i,'번째 재귀 함수에서', i+1,'번쨰 재귀 함수를 호출 합니다.')
    recursive_func(i+1)
    
    
    

recursive_func(1)
