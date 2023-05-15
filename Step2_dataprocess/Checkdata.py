import os

#检查HCPD生成的mask和ref文件，使用时可打开注释
HCPDpath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/fmriprep_REST1_NMSM'
subid = os.listdir(HCPDpath)

# lwzy = []
# for i in subid:
#     maskpath = HCPDpath + '/' + i + '/func/' + i + '_task-REST1_acq-AP_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'
#     if not os.path.exists(maskpath):
#         lwzy.append(i)
#
#         print('subid-', i)
# print(lwzy)

# HCPDxcpdpath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/HCP_xcpd/xcp_abcd'
# xcpdid = os.listdir(HCPDxcpdpath)
# lwzy = []
# for i in subid:
#     if i not in xcpdid:
#         lwzy.append(i)
# print(lwzy)

# HCP = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/fmriprep_REST1_NMSM'
# subid = os.listdir(HCP)
# lwzy = []
# for i in subid:
#     maskpath = HCP + '/' + i + '/anat/' + i + '_desc-brain_mask.nii.gz'
#     if not os.path.exists(maskpath):
#         lwzy.append(i)
#
#         #print('subid-', i)
# print(lwzy)
# print('sum:', len(lwzy))
fmripreplwzy = []
dataName=['sub-462139', 'sub-351938', 'sub-995174', 'sub-171734', 'sub-822244', 'sub-159845', 'sub-150423', 'sub-117728', 'sub-693461', 'sub-145531', 'sub-165234', 'sub-239136', 'sub-142424', 'sub-160931', 'sub-552544', 'sub-734247', 'sub-171128', 'sub-107220', 'sub-201717', 'sub-114924', 'sub-248238', 'sub-953764', 'sub-623137', 'sub-121315', 'sub-150019', 'sub-190132', 'sub-109325', 'sub-209531', 'sub-113417', 'sub-613235', 'sub-221218', 'sub-662551', 'sub-121820', 'sub-186949', 'sub-128329', 'sub-689470', 'sub-173233', 'sub-578158', 'sub-129533', 'sub-569965', 'sub-169141']

for i in dataName:
    fmripreppath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/fmriprep_REST1_NMSM/derivatives/fmriprep/'+i+'/fmriprep/'+i

    if not os.path.exists(fmripreppath):
        fmripreplwzy.append(i)

print(fmripreplwzy)
print(len(fmripreplwzy))
