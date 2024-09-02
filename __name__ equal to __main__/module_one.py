#print(dir())
# print(__name__)
#prints which file is it running from, from the current file or imported

def main():
    print(f'Moduule one : {__name__}')


if __name__ == '__main__':
    main()