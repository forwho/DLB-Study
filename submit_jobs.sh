#!/bin/bash

for file in `ls /mnt/parscratch/users/md1weih/dlb/data/fs_subs_split*`
do
  sbatch -o ../logs/${file##*/}.log --export=subfile=$file ./fs_jobs.sh
done
