import random

l = ["A", "B", "C", "D", "E", "F"]
# リファクタリング
group_pattern = [2, 3, 4]
chose_pattern = random.choice(group_pattern)
group1 = random.sample(l, chose_pattern)
# group2 = [person for person in l if not person in group1]
group2 = list(set(l) - set(group1))

print(group1)
print(group2)

# 完成形----------------------------------------------------------------------------------------------------------
# group1_l = []
# group2_l = []
# group_choice = (group1_l, group2_l)

# for v in l:
#     if len(group1_l) < 4 and len(group2_l) < 4:
#         random.choice((group1_l,group2_l)).append(v)
#     elif len(group1_l) == 4:
#         group2_l.append(v)
#     elif len(group2_l) == 4:
#         group1_l.append(v)

# print(group1_l)
# print(group2_l)

# 「実装時に頭真っ白…」でもう悩まない！プログラムの実装方法に基づいた履歴----------------------------------------------------

# 2つの空のリストを作成する
# group1_l = []
# group2_l = []

# リストの要素を1つずつ取り出す
# for v in l:
    # print(v)

# リストの要素を2つのリストにランダムにappendしていく
    # random.choice((group1_l, group2_l)).append(v)
    # print(group1_l) 
    # print(group2_l) 

# リスト内の要素は 2:4 or 4:2 or 3:3 で条件分岐させる

# group_1,group2の要素数が4未満の場合
    # print(len(group1_l))
    # print(len(group2_l))
    # if len(group1_l) < 4 and len(group2_l) < 4:
    #     random.choice((group1_l,group2_l)).append(v)

# group_1の要素数が4の場合
    # elif len(group1_l) == 4:
    #     group2_l.append(v)

# group_2の要素数が4の場合
    # elif len(group2_l) == 4:
    #     group1_l.append(v)

# 2つのリストをprintする
# print(group1_l)
# print(group2_l)