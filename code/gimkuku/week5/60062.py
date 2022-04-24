from itertools import permutations

def go_friend(weak, friends, dist_list):
    answer = len(friends) + 1
    # 출발 지점 i
    for start in range(len(weak)):
        idx = start
        visited = []
        answer_element = 0
        for i in friends:
            # 다 방문했으면 멈춤
            if (len(visited)) == len(weak):
                break
            # 친구 출발! 
            answer_element += 1
            # 다음 친구는 다음 지점에서 출발
            start_point = dist_list[idx]
            for j in dist_list[idx:]:
                if (len(visited)) == len(weak):
                    break
                # 혼자 못가는 상황이면
                if ((j - start_point) > (i)):
                    break 
                visited.append(j)
                idx += 1
        if len(visited) < len(weak) : answer_element = len(friends) + 1
        answer = min(answer,answer_element)
    return answer
            
def solution(n, weak, dist):
    answer = n
    # dist에 n 더한거 만큼 뒤에 붙여주기
    dist_list = weak[:] 
    for i in weak:
        dist_list.append(i + n)
        
    # 친구들 순서 정하기
    friends_per = list(map(list, permutations(dist, len(dist))))
    answer = len(dist) + 1
    
    for i in friends_per:
        answer = min(answer, go_friend(weak, i, dist_list))
        
    # 불가능하면 -1 로 리턴
    if answer > len(dist):
        return - 1
    return answer