
def solution(info, query):
    answer = []
    
    recruit_dict = {}
    # dict 만들기
    for lang in ["java", "python", "cpp", "-"]:
        for part in ["backend", "frontend", "-"]:
            for career in ["junior", "senior", "-"]:
                for food in ["chicken", "pizza", "-"]:
                    recruit_dict[lang+part+career+food] = []

    # 배열에 잘 넣기
    for i in info:
        lang, part, career, food, score = i.split()
        for _lang in [lang, "-"]:
            for _part in [part, "-"]:
                for _career in [career, "-"]:
                    for _food in [food, "-"]:
                        recruit_dict[_lang+_part+_career+_food].append(int(score))
                        
    for key in recruit_dict.keys():
        recruit_dict[key].sort()

    # print("recruit_dict",recruit_dict)
    # 배열에서 골라서 갯수 세기
    for i in query:
        # print(i)
        lang, a1, part, a2, career, a3, food, score = i.split()
        query_list = recruit_dict[lang+part+career+food]

        low = 0
        high = len(query_list)
        while low < high:
            mid = (low + high) // 2
            if int(score) <= query_list[mid]:
                high = mid
            else:
                low = mid+1

        answer.append(len(query_list)-low)
    return answer