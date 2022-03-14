def solution(id_list, report, k):

    report_table = {}
    reported_count = {reportee: 0 for reportee in id_list}
    mail_count = {reporter: 0 for reporter in id_list}

    for single_report in report:
        reporter, reportee = single_report.split()

        if reporter in report_table.keys():
            if reportee not in report_table[reporter]:
                report_table[reporter].add(reportee)
                reported_count[reportee] += 1

        else:
            report_table[reporter] = set([reportee])
            reported_count[reportee] += 1

    banned = list(
        map(lambda x: x[0], (filter(lambda x: x[1] >= k, reported_count.items())))
    )

    for (reporter, reportee) in report_table.items():
        for reported_user in reportee:
            if reported_user in banned:
                mail_count[reporter] += 1

    return list(mail_count.values())


solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
