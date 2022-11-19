def oops():
    my_list = [1, 2, 3]
    raise my_list[3]


def oops_go():
    try:
        oops()
    except IndexError as fail:
        print(fail)
    except KeyError as error:
        print(error)


oops_go()
