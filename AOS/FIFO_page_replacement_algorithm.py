
frame_size = int(input("Size of Frame:"))
n = int(input("Enter Size of Refrence String:"))
print("Enter Values:")
refrence_string = []
for i in range(int(n)):
    refrence_string.append(int(input()))


def fifo_algo(ref, frame_size):
    page_hit = 0
    frame = []
    for j in ref:
        if len(frame) < frame_size:
            frame.append(j)
            print("For {} : {}".format(j, frame))
        else:
            if j in frame:
                print("For {} : ".format(j))
                page_hit += 1
                continue
            else:
                frame.pop(0)
                frame.append(j)
                print("For {} : {}".format(j, frame))
    print("Page Hit : {}".format(page_hit))
    print("Page Fault : {}".format(n-page_hit))


fifo_algo(refrence_string, frame_size)
