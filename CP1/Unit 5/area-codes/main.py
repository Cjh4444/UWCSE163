# Define your function up here!
def area_codes(list):

    temp_list = [x.split("-") for x in list]
    temp_list = [x[0] for x in temp_list]
    return set(temp_list)


def main():
    print(area_codes([
        '123-456-7890',
        '206-123-45676',
        '123-000-0000',
        '425-999-9999'
    ]))


if __name__ == '__main__':
    main()
