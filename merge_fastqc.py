#!/usr/bin/env python
import pandas as pd
import sys
import os 
# Usage: ./merge_fastqc.py a.txt output/pigz/ 


saveFile = sys.argv[1]
directory = sys.argv[2]

count_files = [filename for filename in os.listdir(directory) if filename.endswith(".count")]



#samples = metadata['sample'].tolist()
df = pd.DataFrame(columns=['Sample','ReadNum',"BaseNum","Q20","Q30","GC"])
for sample in count_files:
    file_path = os.path.join(directory, sample)
    print(file_path)
    count = pd.read_csv(file_path,sep="\t",header=None)
    count.columns = ['ReadNum',"BaseNum","Q20","Q30","GC"]
    count['Sample']=sample
    df = pd.concat([df,count])
    # print(count)
    df.to_csv(saveFile, sep='\t',index=False)
