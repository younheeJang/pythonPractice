def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 1:
        move_disk(num_disks, start_peg, end_peg)
    else:
        other_peg =10 - start_peg - end_peg
        hanoi(num_disks - 1, start_peg, other_peg)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks - 1, other_peg, end_peg)

# 10은 마지막기둥*2로.
hanoi(5, 1, 5)