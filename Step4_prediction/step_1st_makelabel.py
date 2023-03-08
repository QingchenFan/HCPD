import pandas as pd

subid = pd.read_csv('/Users/fan/Documents/Data/HCPData/HCPDsubID.csv')
allinfo = pd.read_csv('/Users/fan/Documents/Data/HCPData/behavior/flanker01.csv')

allinfo = allinfo.drop([0])
allinfoid = list(allinfo['src_subject_id'])

res = []
besideid = []
for i in subid['subID']:
    if i[4:] in allinfoid:
        indexid = allinfoid.index(i[4:])
        testid = allinfo.loc[indexid + 1, 'src_subject_id']
        if i[4:] != testid:
         print('有错误：', i[4:], testid)
         break
        score = allinfo.iloc[indexid+1, :]
        res.append(score)
    else:
        besideid.append(i)

label = pd.DataFrame(res)
label.to_csv('flanker01_lable.csv')

# 找出来有行为数据没有影像数据的被试
test = ['sub-'+i for i in allinfoid if 'sub-'+i not in list(subid['subID'])]

print(test, len(test))