from os import listdir


def get_book_list(input_file):
    """
    reads a user profile and the users name andreturn a list of all lines after "Books\n"
    :type input_file: file
    """
    is_book = False
    title_list = []  # type: List[str]
    # name=input_file.readline()
    for line in input_file:
        if is_book and not line.isspace():
                title_list.append(line[:-1])
                # stores the book title, slicing away the carridge retun in a list
        if line == 'Books:\n':
            is_book = True
    return title_list  # ,name


def get_interests(path="./data/profiles/"):
    """
    :type path: str
    :rtype: dict
    """
    user_interests={}
    profiles = [profile for profile in listdir(path) if profile[-4:] == ".txt"]
    for profile in profiles:
        with open(path + profile, 'r') as input_file:
            book_list = get_book_list(input_file)
            input_file.close()
            user_interests[profile] = book_list
    return user_interests