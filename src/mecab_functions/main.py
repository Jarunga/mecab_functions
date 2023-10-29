import MeCab
import ipadic
import re
import numpy as np

CHASEN_ARGS = r' -F "%m\t%f[7]\t%f[6]\t%F-[0,1,2,3]\t%f[4]\t%f[5]\n"'
CHASEN_ARGS += r' -U "%m\t%m\t%m\t%F-[0,1,2,3]\t\t\n"'
TAGGER = MeCab.Tagger(ipadic.MECAB_ARGS + CHASEN_ARGS)

def get_fullname(txt):
    result=np.array([line.split() for line in TAGGER.parse(txt).splitlines() if re.search('人名\-名|人名\-姓',line.split()[-1])])

    if len(result)>0:
        pos=result[:,-1]

        if '名詞-固有名詞-人名-姓' in pos and '名詞-固有名詞-人名-名' in pos:    
            return " ".join(result[:,0])
        else:
            return None

    else:
        return None

def get_lastname(txt):
    result=np.array([line.split() for line in TAGGER.parse(txt).splitlines() if re.search('人名\-姓',line.split()[-1])])

    if len(result)>0:
        pos=result[:,-1]

        if '名詞-固有名詞-人名-姓' in pos:    
            return " ".join(result[:,0])
        else:
            return None

    else:
        return None
