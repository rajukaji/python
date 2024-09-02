import module_one
#it imports module_one file/python script, and run all the codes,

#since the methods are not called, they do not run on their own, first need to make call
#imported __name__ doesn't equal to __main__, so this conditional is avoided, ie, not run

#we can call the method with the module name

module_one.main()
#prints module_one name, ie, module_one

def main():
    print(f'Module two name: {__name__}')

if __name__ == '__main__':
    main()