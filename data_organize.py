import os
import glob
import re

def dcm2nii_dlb(spath,tpath):
    subs=os.listdir(spath)
    for sub in subs:
        files=glob(["%s/%s/*/*" % (spath,sub)])
        for file in files:
            date=re.search("\d{4}-\d{2}-\d{2}_\d{2}_\d{2}",file,).group()
            if not os.path.exists("%s/%s_%s/anat" % (tpath,sub,date)):
                os.makedirs("%s/%s_%s/anat" % (tpath,sub,date))
            cmd="dcm2niix -f t1.nii.gz -o %s/%s_%s/anat/ %s" % (tpath,sub,date,file)
            os.system(cmd)

if __name__=="__main__":
    spath=""
    tpath=""
    dcm2nii_dlb(spath, tpath)