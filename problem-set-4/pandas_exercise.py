import pandas as pd


ACS = pd.read_csv("\\\\cbo.gov\\shares\\PUBLIC_DATA\\ACS\\1-year\\2018\\psam_pusa.csv", nrows=1000)
print(ACS.describe())

ACS['YEAR'] = 2018

ACS_subset = ACS[['YEAR', 'SERIALNO', 'ST', 'AGEP', 'SSP', 'RETP']]
print('Head of ACS_subset:')
print(ACS_subset.head(10), '\n')

print('Means of ACS_subset:')
print(ACS_subset.mean(), '\n')

# With copy to avoid SettingWithCopyWarning
ACS_subset = ACS_subset.copy()
ACS_subset['AGE_50_PLUS'] = (ACS_subset.loc[:, 'AGEP'] >= 50).astype(int)
print('Head of ACS_subset with `AGE_50_PLUS` dummy variable')
print(ACS_subset.head(10), '\n')

# With .assign() method, which also avoids the SettingWithCopyWarning
ACS_subset = ACS_subset.assign(AGE_LT_50 = (ACS_subset.loc[:, 'AGEP'] < 50).astype(int))
print('Head of ACS_subset with `AGE_LT_50` dummy variable:')
print(ACS_subset.head(10), '\n')
