def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    dict_ = {}
    for users in report:
        if users.split()[1] not in dict_.keys():
            dict_[users.split()[1]] = [users.split()[0]]
        else:
            if users.split()[0] not in dict_.get(users.split()[1]):
                dict_[users.split()[1]] += [users.split()[0]]
    for users in dict_.values():
        if len(users) >= k:
            for user in users:
                answer[id_list.index(user)] += 1
    return answer