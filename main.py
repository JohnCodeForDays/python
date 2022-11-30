
def calculate_depth_increase(depths):

    # guard clauses are generally un-pythonic. if it's not an iterable, or doesn't have even one item,
    # then the question of depths is moot, just fail
    depths_iterable = iter(depths)
    previous_depth = next(depths_iterable)

    depth_increase_counts = 0

    for depth in depths:
        # we could make the case here that we want to ensure long before this point,
        # that every entry was a valid int or number..
        if depth > previous_depth:
            depth_increase_counts += 1
        previous_depth = depth

    return depth_increase_counts


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    try:

        input_file_of_depths = open(".\\input.txt", mode="rt", encoding="utf-8")
        increase_counts = calculate_depth_increase(input_file_of_depths.readlines())
        print("The depth increased {} times.".format(increase_counts))

    # in general if we hit any exception in this scenario, we know there's no point trying to
    # come back with some inaccurate final answer,
    # but we can handle or provide more insight into common problems, like so..
    except IOError as eio:
        print("Something is wrong with your file, champ..\n")
        print(eio)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
