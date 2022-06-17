import pandas as pd
import sys

args = sys.argv

log_data = pd.read_csv(args[1], header=0)
#print(logData)
#print(logData["player_id"])

player_score_dict = dict()
for player_ID,player_score in zip(log_data["player_id"],log_data["score"]):
    if player_ID not in player_score_dict:
        player_score_dict[player_ID] = [player_score, 1] #playerIDをキーとして持ち，総スコアとプレイ回数を要素としてもつリストをバリューとする辞書を作成
    else:
        player_score_dict[player_ID][0] += player_score #スコアの更新
        player_score_dict[player_ID][1] += 1 #プレイ回数の更新

#print(player_score_dict)

player_average_score = dict()
for player_ID, score_and_count_list in player_score_dict.items():
    player_average_score[player_ID] = round(score_and_count_list[0]/score_and_count_list[1]) #スコア平均を取得
#print(player_average_score)

sorted_player_average_score = sorted(player_average_score.items(), key=lambda i: i[1], reverse=True)
print(sorted_player_average_score)

player_average_dataframe = pd.DataFrame(list(sorted_player_average_score), columns = ['player_id','mean_score'])
print(player_average_dataframe)
print(player_average_dataframe.rank(numeric_only=True, ascending=False).astype(int))
