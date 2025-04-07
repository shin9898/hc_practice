SCORE_MAP = {
    -4: 'コンドル',
    -3: 'アルバトロス',
    -2: 'イーグル',
    -1: 'バーディ',
    0: 'パー',
    1: 'ボギー'
}

def take_values_func():
    x_list = list(map(int, input().split(',')))
    y_list = list(map(int, input().split(',')))
    return x_list, y_list


def scoring_func(x_list, y_list):
    return [y - x for x, y in zip(x_list, y_list)]


def score_output(x_list, y_list, result_list):
    output_result_list = []
    for x, y, result in zip(x_list, y_list, result_list):
        if x != 5 and y == 1:
            output_result_list.append('ホールインワン')
        elif result in SCORE_MAP:
                output_result_list.append(SCORE_MAP[result])
        elif result >= 2:
            output_result_list.append(f"{result}ボギー")
    print(*output_result_list, sep=',')


if __name__ == '__main__':
    x_list, y_list = take_values_func()
    result_list = scoring_func(x_list, y_list)
    score_output(x_list, y_list, result_list)

# 学習記録 -----------------------------------------------------------------------------------------------
# PRで指摘された内容で修正した部分
# SCORE_MAP = {
#     -4: 'コンドル',
#     -3: 'アルバトロス',
#     -2: 'イーグル',
#     -1: 'バーディ',
#     0: 'パー',
#     1: 'ボギー'
# }
# SCORE_MAP（定数）でkey:=スコア差,value=スコア名を定義しresutl=y-xでvalueを取得できるように修正

# for x, y, result in zip(x_list, y_list, result_list):
    # if x != 5 and y == 1:
    #     output_result_list.append('ホールインワン')
    # elif result in SCORE_MAP:
    #         output_result_list.append(SCORE_MAP[result])
    # elif result >= 2:
    #     output_result_list.append(f"{result}ボギー")
# まずトップに規定打数5以外で1打(ホールインワン)の条件を定義することでx==5 and y==1（コンドル）と
# x==5 and y==2(アルバトロス),x!=3 and result==-2(イーグル)の条件式をわざわざ定義する必要がなくなる
# なぜならx==4 result==-3,x==3 result==-2は最初のホールインワンでTrueになるから
# あとはresult in SCORE_MAPで合致したkeyのvalueを取得して格納し、
# 最後にresult>=2の条件式を定義すればすっきりとしたコードとなる

# case_1.txt 期待する出力
# イーグル,バーディ,コンドル,2ボギー,3ボギー,バーディ,ボギー,ホールインワン,ボギー,2ボギー,
# アルバトロス,ボギー,3ボギー,バーディ,ボギー,ボギー,バーディ,ボギー
# case_2.txt 期待する出力
# ボギー,イーグル,ホールインワン,アルバトロス,ホールインワン,バーディ,バーディ,バーディ,
# 3ボギー,パー,パー,バーディ,ホールインワン,3ボギー,4ボギー,バーディ,イーグル,イーグル

# PR提出1回目のscore_outputメソッド
# def score_output(x_list, y_list, result):
    # output_result = []
    # for x, y, result in zip(x_list, y_list, result):
    #     if x == 5 and y == 1:
    #         output_result.append("コンドル")
    #     if x != 5 and y == 1:
    #         output_result.append("ホールインワン")
    #     if x == 5 and y == 2:
    #         output_result.append("アルバトロス")
    #     if x != 3 and result == -2:
    #         output_result.append("イーグル")
    #     if result == -1:
    #         output_result.append("バーディ")
    #     if result == 0:
    #         output_result.append("パー")
    #     if result == 1:
    #         output_result.append("ボギー")
    #     if result >= 2:
    #         output_result.append(f"{result}ボギー")
    # print(*output_result, sep=',')

# 値受け取る関数
# def take_values_func():
# case_1.txtの値を受け取りX(規定打数)とY(プレイヤー打数)に代入
#   x_list = list(map(int, input().split()))
#   y_list = list(map(int, input().split()))
#   return x_list, y_list

# スコア差計算関数
# def scoring_func(x_list, y_list):

# X[i] - Y[1]で規定打数とプレイヤー打数のresult(差)を計算
    # result_list = []
    # for x, y in zip(x_list, y_list):
    # result = y - x
    # result_list.append(result)
    # print(result)
    # return result_list

# スコア出力関数
# コード書いている最中のひらめき
# 現状全てのスコアを計算している状況でx,yだけで条件を導き出せるものがあるので計算が必要なものだけscoring_funcを呼び出すようにする
# def score_output(x_list, y_list, result):
#     output_result = []
#     for x, y, result in zip(x_list, y_list, result):
# # X == 5 and result == 1 :コンドル result == 1からy == 1に修正
#         if x == 5 and y == 1:
#             output_result.append("コンドル")
# # X != 5 and Y == 1 :ホールインワン
#         if x != 5 and y == 1:
#             output_result.append("ホールインワン")
# # X == 5 and Y == 2 :アルバトロス
#         if x == 5 and y == 2:
#             output_result.append("アルバトロス")
# # result == -2 : イーグル
#         if x != 3 and result == -2:
#             output_result.append("イーグル")
# # result == -1 : バーディー
#         if result == -1:
#             output_result.append("バーディー")
# # result == 0 : パー
#         if result == 0:
#             output_result.append("パー")
# # result = 1 : ボギー
#         if result == 1:
#             output_result.append("ボギー")
# # result >= 2 : f"{result}ボギー
#         if result >= 2:
#             output_result.append(f"{result}ボギー")
#     print(*output_result, sep=',')
# # 関数実行
# if __name__ == '__main__':
#     x_list, y_list = take_values_func()
#     # print(x_l)
#     # print(y_l)
#     result = scoring_func(x_list, y_list)
#     # print(result)
#     score_output(x_list, y_list, result)

# 入力値
# 5 4 3 4 3 4 4 4 5 4 4 3 5 3 4 4 4 4
# 1 4 1 3 3 5 6 7 2 8 1 2 2 3 3 4 4 4
# 期待する出力
# コンドル,パー,ホールインワン,バーディー,パー,ボギー,2ボギー,3ボギー,アルバトロス,4ボギー,ホールインワン,バーディー,アルバトロス,パー,バーディー,パー,パー,パー
