import os

# 检查HCPD生成的mask和ref文件，使用时可打开注释
# HCPDpath = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCPD/fmriprep_rest_no_MSM'
# subid = os.listdir(HCPDpath)
# lwzy = []
# for i in subid:
#     maskpath = HCPDpath + '/' + i + '/func/' + i + '_task-REST1_acq-AP_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'
#     if not os.path.exists(maskpath):
#         lwzy.append(i)
#
#         print('subid-', i)
# print(lwzy)

HCP = '/ibmgpfs/cuizaixu_lab/fanqingchen/data/HCP/fmriprep_REST1_NMSM'
subid = os.listdir(HCP)
lwzy = []
for i in subid:
    maskpath = HCP + '/' + i + '/anat/' + i + '_desc-brain_mask.nii.gz'
    if not os.path.exists(maskpath):
        lwzy.append(i)

        #print('subid-', i)
print(lwzy)
print('sum:', len(lwzy))
