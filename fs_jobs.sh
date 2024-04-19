#!/bin/bash
#SBATCH --time=96:00:00
#SBATCH --mem=32G
#SBATCH --cpus-per-task=4

#subfile=""
spath=/mnt/parscratch/users/md1weih/dlb/data/nifti_data2
tpath=/mnt/parscratch/users/md1weih/dlb/data/fs_result
for sub in `cat $subfile`
do
  export FREESURFER_HOME=/mnt/parscratch/users/md1weih/software/freesurfer
  source $FREESURFER_HOME/SetUpFreeSurfer.sh
  $FREESURFER_HOME/bin/recon-all -subjid $sub -all -sd $tpath -i $spath/$sub/anat/t1.nii
done
