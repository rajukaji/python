def sort_by_length(arr):
    return sorted(arr, key=len)

#sort based on lenght of strings



def sort_by_ascending(arr):
    return sorted(arr)


def main():
    print(sort_by_length(['aaabbbb', 'aa', 'a', 'aaaaaaaaaaaaaaaaaaaaa']))
    print(sort_by_ascending([4, 5, 3, 6, 5, 1, 2]))

if __name__ == '__main__':
    main()