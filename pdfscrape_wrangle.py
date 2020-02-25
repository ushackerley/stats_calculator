import pandas as pd

scraped_data = pd.read_csv('./scraped_data.csv')

# Splitting up the strings to form a data frame
sliced_data = scraped_data.iloc[1:,0]
df = pd.DataFrame(sliced_data)
df.columns = ['unsplit']

def splitter_6(s):
	split_up = [s[i:i+6] for i in range(0, len(s), 6)]
	while len(split_up) < 3:
		split_up.append(None)
	return split_up

df = df.merge(df.unsplit.apply(lambda s : pd.Series({'0.1':splitter_6(s)[0], 
										'0.05':splitter_6(s)[1], 
										'0.025':splitter_6(s)[2]})), 
								left_index=True, right_index=True)
df = df.drop('unsplit', axis=1)
df = df.reset_index().drop(['index'], axis=1)
# print(df)

# Dimension column
integer_incremented = [i for i in range(4,31)]
tens_incremented = [i for i in range(40, 101, 10)]
dim_list = integer_incremented + tens_incremented
dim_col = pd.Series(dim_list, name='dimensions')
df.insert(0, 'dimensions', dim_col)
df = df.set_index('dimensions')

# Writing out to a csv file
df.to_csv('./spearman.csv')
