import pandas as pd

subid = pd.read_csv('/Users/fan/Documents/Data/HCPData/HCPDsubID.csv')
allinfo = pd.read_csv('/Users/fan/Documents/Data/HCPData/behavior/flanker01.csv')

allinfo = allinfo.drop([0])
print(allinfo)

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
        print(i)
        besideid.append(i)
print(len(besideid))
label = pd.DataFrame(res)
label.to_csv('flanker01_lable.csv')