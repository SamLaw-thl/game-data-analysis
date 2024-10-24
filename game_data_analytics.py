import pandas as pd
from matplotlib import pyplot as plt

"""Question 1"""
# load the gamdata.csv into crude dataframe object
raw_data = pd.read_csv("game_data.csv", header=None, index_col=0)

# transform data
row_list = []

for row in raw_data.iterrows():
    temp_value_list = []
    temp_row = str(row[0]).split("|")
    for value in temp_row:
        if value != "":
            temp_value_list.append(value.strip())
    row_list.append(temp_value_list)

# extract column name
column_name = row_list.pop(0)

# delete the element contains the "------"
del row_list[0]


# convert row_list into dataframe object
transformed_data = pd.DataFrame(row_list, columns=column_name)
print(transformed_data)
print()


# check if there are missing value and sum the missing value in the transformed data
print(transformed_data.isna().sum())
print()

# The data is cleaned due to no missing value
cleaned_data = transformed_data


# Create a new column score_category that categorizes scores
def score_categorization(score):
    if int(score) < 50:
        return "Low"
    elif int(score) >= 80:
        return "High"
    else:
        return "Medium"


cleaned_data["score_category"] = cleaned_data["score"].apply(score_categorization)
print(cleaned_data)
print()


# Group the data by level and calculate the average score for each level
cleaned_data["score"] = pd.to_numeric(cleaned_data["score"])
average_score_by_level = cleaned_data.groupby("level")["score"].mean()
print(average_score_by_level)
print()


"""Question 2"""
# What is the average score of players across all levels?
average_score_across_all_levels = cleaned_data["score"].mean()
print(f'What is the average score of players across all levels? Answer: {average_score_across_all_levels}')

# Which level has the highest average score?
level_has_the_highest_average_score = average_score_by_level.idxmax()
print(f'Which level has the highest average score? Answer: {level_has_the_highest_average_score}')

# How many players scored in the 'High' category?
player_scored_in_high_category = cleaned_data[cleaned_data["score_category"] == "High"]["player_id"].nunique()
print(f"How many players scored in the 'High' category? Answer: {player_scored_in_high_category}")


"""Question 3"""
# Create a bar chart that shows the average score for each level
average_score_by_level.plot(x="Level", y="Average Score", kind="bar")
plt.xticks(rotation=0)
plt.show()
plt.clf()

# Create a pie chart that displays the distribution of score categories ('Low', 'Medium', 'High').
distribution_of_score_categories = cleaned_data["score_category"].value_counts()
distribution_of_score_categories.plot(x="Score Category", y="Score", kind="pie")
plt.show()


"""Question 4"""
# Write a function that takes a player_id as input and returns the player's highest score and the level at which it was achieved.
def query_about_player_highest_score_and_level_achieved(player_id):
    player_records = cleaned_data[cleaned_data["player_id"] == player_id]
    highest_score = player_records["score"].max()
    level_achieved = player_records["level"].max()
    return highest_score, level_achieved


# Input the player id to query the highest score and level achieved by the player
player_id = input("Please enter the player id: ")
highest_score, level_achieved = query_about_player_highest_score_and_level_achieved(player_id)

print(f"player id = {player_id}, highest score = {highest_score}, level achieved = {level_achieved}")
