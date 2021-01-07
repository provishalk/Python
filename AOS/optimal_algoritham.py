frame_size = 3
refrence_size = 12

refrence_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]


def index_of(arr, item, start, end):
    if item in arr[start:end]:
        return arr.index(item, start, end)
    else:
        return end


def optimal_algo(ref, f_size):
    frame = []
    page_hit = 0
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
                a = index_of(ref, frame[0], i, len(ref))
                b = index_of(ref, frame[1], i, len(ref))
                c = index_of(ref, frame[2], i, len(ref))
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
