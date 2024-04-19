import os
import glob
import re
import nibabel as nib
import numpy as np

def dcm2nii_dlb(spath,tpath):
    subs=os.listdir(spath)
    for sub in subs:
        files=glob.glob("%s/%s/*/*" % (spath,sub))
        for file in files:
            date=re.search("\d{4}-\d{2}-\d{2}_\d{2}_\d{2}",file,).group()
            if not os.path.exists("%s/%s_%s/anat" % (tpath,sub,date)):
                os.makedirs("%s/%s_%s/anat" % (tpath,sub,date))
            cmd="dcm2niix -z n -f t1 -o %s/%s_%s/anat/ %s" % (tpath,sub,date,file)
            os.system(cmd)

def global_pib(spath,tpath,mask):
    image_data=nib.load(spath).get_fdata()
    mask_data=nib.load(mask).get_fdata()
    suvr=np.mean(image_data[mask_data==1,:],axis=0)
    np.savetxt(tpath,suvr)

if __name__=="__main__":
    spath="/mnt/parscratch/users/md1weih/dlb/data/pet_stat_data/"
    tpath="/mnt/parscratch/users/md1weih/dlb/data/pet_stat_data/"
    mask="/mnt/parscratch/users/md1weih/dlb/data/pet_stat_data/global_pib_crop.nii.gz"
    global_pib("%s/nc.nii.gz" % spath, "%s/nc.txt" % spath,mask)
    global_pib("%s/ad.nii.gz" % spath, "%s/ad.txt" % spath,mask)
    global_pib("%s/dlb.nii.gz" % spath, "%s/dlb.txt" % spath,mask)
    #dcm2nii_dlb(spath, tpath)
