from q08_base import *

pd.set_option('display.max_rows', None)

feature_df = pd.DataFrame([[1, 120, np.nan], 
                          [3, 100, np.nan],
                          [np.nan, np.nan, np.nan],
                          [4, 200,1.5],
                          [2, np.nan, np.nan]])

print(f'original shape: {feature_df.shape}')
print(feature_df)

print('-------------------------------------')
print('全ての要素が欠損値になっている行を削除')
feature_df = feature_df.dropna(how="all")
print(f'original shape: {feature_df.shape}')
print(feature_df)

print('-------------------------------------')
print('欠損値の個数が2より多い列を削除')
feature_df = feature_df.dropna(axis=1, thresh=2)
print(f'original shape: {feature_df.shape}')
print(feature_df)

print('-------------------------------------')
print('欠損値を列ごとの平均値で置換')
feature_df = feature_df.fillna(feature_df.mean())
print(f'original shape: {feature_df.shape}')
print(feature_df)

print('-------------------------------------')
print('StandardScalerでスケーリング')
feature_df = StandardScaler().fit_transform(feature_df)
print(f'original shape: {feature_df.shape}')
print(feature_df)