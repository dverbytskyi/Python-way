def index_all(search_list, item):
    indices = list()
    try:
        for i in range(len(search_list)):
            if search_list[i] == item:
                indices.append([i])
            elif isinstance(search_list[i], list):
                for index in index_all(search_list[i], item):
                    indices.append([i] + index)
        return indices
    except ValueError as error:
        print(f'Element "{item}" not found in the list :', error)


if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))
    print(index_all(example, [1, 2, 3]))
