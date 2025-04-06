# 値受け取る関数
def take_values_func():
# case_1.txtの値を受け取りX(規定打数)とY(プレイヤー打数)に代入
  x_list = list(map(int, input().split()))
  y_list = list(map(int, input().split()))
  return x_list, y_list

# スコア差計算関数
def scoring_func(x_list, y_list):

# X[i] - Y[1]で規定打数とプレイヤー打数のresult(差)を計算
    result_list = []
    for x, y in zip(x_list, y_list):
      result = x - y
      result_list.append(result)
      # print(result)
    return result_list

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

# 関数実行
if __name__ == '__main__':
    x_list, y_list = take_values_func()
    # print(x_l)
    # print(y_l)
    result = scoring_func(x_list, y_list)
    # print(result)
