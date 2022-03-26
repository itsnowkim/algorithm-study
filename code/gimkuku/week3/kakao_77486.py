def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)

    # 칫솔 판매 금액 개당 백원
    for idx, money in enumerate(amount):
        amount[idx] = money * 100
    
    # enroll 리스트로 dict 만들기
    enroll_dict = {}
    for idx,name in enumerate(enroll):
        enroll_dict[name] = idx
        
    # seller 판매한거 for문
    for idx, name in enumerate(seller):
        idx_seller = enroll_dict[name]
        ref_name = referral[idx_seller]
        share = int(amount[idx] * 0.1)
        answer[idx_seller] += amount[idx] - share

        while (ref_name != "-" and share):
            idx_ref = enroll_dict[ref_name]
            ref_name = referral[idx_ref]
            answer[idx_ref] += share - int(share*0.1)
            share = int(share*0.1)
            
    return answer

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],	["young", "john", "tod", "emily", "mary","young"],	[12, 4, 2, 5, 10,11])