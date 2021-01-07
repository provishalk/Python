frame_size = 3
refrence_size = 12
refrence_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]


def index_of(arr, item):
    arr.reverse()
    if item in arr:
        return arr.index(item)
    else:
        return -50


def optimal_algo(ref, f_size):
    page_hit = 0
    frame = []
    for i, j in enumerate(ref):
        if len(frame) < f_size:
            frame.append(j)
            print("For {} : {}".format(j, frame))
        else:
            if j in frame:
                print("For {} : ".format(j))
                page_hit += 1
                continue
            else:
                a = index_of(ref[0:i], frame[0])
                b = index_of(ref[0:i], frame[1])
                c = index_of(ref[0:i], frame[2])
                if a >= b and a >= c:
                    frame.pop(0)
                    frame.append(j)
                    print("For {} : {}".format(j, frame))
                elif b >= a and b >= c:
                    frame.pop(1)
                    frame.append(j)
                    print("For {} : {}".format(j, frame))
                else:
                    frame.pop(2)
                    frame.append(j)
                    print("For {} : {}".format(j, frame))
    print("Page Hit : {}".format(page_hit))
    print("Page Fault : {}".format(refrence_size - page_hit))


optimal_algo(refrence_string, frame_size)
