import sys

# 値受け取る関数
# case_1.txtの値を受け取りX(規定打数)とY(プレイヤー打数)に代入
input_line = int(input())
for X in range(input_line):
    Y = input().rstrip().split(' ')
    print(X)
    print(Y)
    # return X, Y

# スコア差計算関数
# def scoring(X, Y):

# X[i] - Y[1]で規定打数とプレイヤー打数のresult(差)を計算
    # for x, y in zip(X, Y):
    #   result = x - y
    #   print(result)
    #   return score_output(X, Y, result)

# スコア出力関数
# def score_output(X, Y, result):

# X == 5 and result == -4 :コンドル
    # if X == 5 and result == -4:
# X != 5 and Y == 1 :ホールインワン

# X == 5 and Y == 2 :アルバトロス

# result == -2 : イーグル

# result == -1 : バーディー

# result == 0 : パー

# result = 1 : ボギー

# result >= 2 : f"{result}ボギー