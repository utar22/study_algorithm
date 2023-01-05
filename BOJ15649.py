'''
BOJ 15649
N과 M 문제
N은 숫자의 수
M은 배열의 수
겹치지 않고 수열이 완성되는 경우를 출력함 
'''


n, m = map(int, input().split())

#map(적용함수, 입력변수)
#입력변수를 함수를 적용해서 보내준다.
#여기서는 입력 변수를 int로 변환하는 방법임
#[n, m] = [int(x) for x in input().strip().split()]
#이렇게도 해볼 수 있음

arr = [0] * 10  # 빈 배열을 이렇게 10개짜리로 만들어 볼 수 도 있다.
isUsed = [0] * 10 # 숫자는 정수(2진수, 10진수, 16진수), 실수와 관계없이 0이면 거짓, 0이 아닌 수는 참입니다.

print(arr)

# k개의 수를 선택한 상황에서 arr[k]를 정하는 함수
def func(k):
    # base condition
    if k == m:  # 마지막 배열까지 다 채웠으면 출력
        for i in range(m):
            print(arr[i], end = " ") #default로 print뒤에 개행이 들어가있음
        print("\n")
        return

    # 배열dl 아직 채워지고 있는 중이라면,
    #채워질 숫자는 1부터 n이므로, 돌아가면서 isUsed = False를 찾는다
    for i in range(1, n+1): 
        if not isUsed[i]:
            '''
            여기부분 k, i index 살 생각해보기
            '''
            arr[k] = i
            isUsed[i] = 1
            func(k+1)
            isUsed[i] = 0 #리턴 나왔으면 초기화

    #1부터 n까지의 수를 하나씩 찾아보면서 아직 쓰이지 않은 수를 확인함
    #dfs를 기본으로 하는데, 불필요한 경우는 제외하는것이 백트래킹
    #M과 N 문제의 경우 isUsed를 통해서 사용된 숫자가 겹치는 경우를 제외하는 것인듯


if __name__ == "__main__":
    func(0)




