
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_discs, start_peg, end_peg):
    print(num_discs)
    if num_discs == 1:
        move_disk(num_discs, start_peg, end_peg)
    else:
        other_peg = 6 - start_peg - end_peg
        hanoi(num_discs - 1, start_peg, other_peg)
        move_disk(num_discs, start_peg, end_peg)
        hanoi(num_discs - 1, other_peg, end_peg)
    return
hanoi(3, 1, 3)
def hanoi1(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
    if num_disks == 1:
        move_disk(num_disks, start_peg, end_peg)

# 테스트 코드 (포함하여 제출해주세요)
#hanoi(3, 1, 3)

