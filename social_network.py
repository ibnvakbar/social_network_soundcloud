import sys


def mapper(data):
    connection_list = []
    for line in data:
        line = line.strip()
        connection = line.split()
        user = connection[0]
        for friend in connection[1:]:
            connection_list.append([user,friend,1])
            connection_list.append([friend, user, 1])

    return sorted(connection_list, key=lambda x: (x[0], x[1]))


def mapper_iteration(data):

    new_user = None
    connection_dict = dict()
    connection_list = []

    for line in data:
        user = line[0]
        friend = line[1]
        depth = line[2]
        if new_user == user:

            for people in connection_dict:
                updated_depth = depth + connection_dict[people]
                connection_list.append([friend, people,updated_depth])
                connection_list.append([people,friend,updated_depth])

        else:
            new_user = user
            connection_dict.clear()

        connection_dict[friend] = depth
    connection_list = connection_list + data

    return sorted(connection_list, key=lambda x: (x[0], x[1]))


def reducer_iteration(data):
    new_connection = []
    pairs = None
    for line in data:
        if pairs != line:
            pairs = line
            new_connection.append(line)

    return new_connection


def reducer(data,N):
    current_user = None
    connection_set = set()
    result = {}

    for line in data:
        user = line[0]
        friend = line[1]
        depth = line[2]

        if current_user == user:
            if depth <= N:
                connection_set.add(friend)
        else:
            if current_user:
                result[current_user] = sorted(connection_set)
            connection_set.clear()
            if depth <= N:
                connection_set.add(friend)
            current_user = user

    if current_user == user:
        result[current_user] = sorted(connection_set)

    return result

if __name__ == '__main__':
    with open('input.txt') as f:
        contents = f.read().split("\n")

    mutuals = mapper(contents)

    N = int(sys.argv[1])
    counter = 0
    while counter < N:
        mutuals = mapper_iteration(mutuals)
        agg_mutual = reducer_iteration(mutuals)
        counter += 1

    mutual_list = reducer(agg_mutual,N)

    for r in mutual_list:
        lines = r+' '+' '.join(map(str, mutual_list[r]))
        with open('output.txt', 'a') as f:
            f.write(lines + '\n')
