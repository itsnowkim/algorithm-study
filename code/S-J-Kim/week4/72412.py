def solution(info, query):
    answer = []

    lang = {"java": set([]), "python": set([]), "cpp": set([])}
    part = {"backend": set([]), "frontend": set([])}
    exp = {"senior": set([]), "junior": set([])}
    soul = {"pizza": set([]), "chicken": set([])}
    scores = []

    for (idx, infomation) in enumerate(info):
        ilang, ipart, iexp, isoul, score = infomation.split()

        lang[ilang].add(idx)
        part[ipart].add(idx)
        exp[iexp].add(idx)
        soul[isoul].add(idx)
        scores.append(score)

    for command in query:
        ans = 0
        splited = command.split(" and ")
        splited[-1:] = splited[-1].split()

        ilang, ipart, iexp, isoul, score = splited

        arr = set([])

        arr |= (
            lang[ilang]
            if not ilang == "-"
            else lang["java"] | lang["python"] | lang["cpp"]
        )

        if ipart != "-" and arr:
            arr &= part[ipart]

        if iexp != "-" and arr:
            arr &= exp[iexp]

        if isoul != "-" and arr:
            arr &= soul[isoul]

        if arr:
            for candidate in list(arr):
                if int(scores[candidate]) >= int(score):
                    ans += 1

        answer.append(ans)

    return answer


solution(
    [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50",
    ],
    [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150",
    ],
)
