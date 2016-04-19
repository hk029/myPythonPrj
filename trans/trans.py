# -*- encoding: utf-8 -*-
import re;

Map = {'leet':'LeetCode:','n':''}
Mypath = 'C://Users/锴/Documents/印象笔记/'
if __name__ == '__main__':

    filename = raw_input('FILE NAME: ')
    tips = raw_input('tips:')
    inpath = (Mypath+filename+'.md').decode('utf-8').encode('cp936')
    outpath = (Mypath+Map[tips]+filename+'.md').decode('utf-8').encode('cp936')
    fp = open(inpath,'r')
    text = fp.readlines()
    fp.close()
    fp = open(outpath,'w')
    out = ""
    flag = False;
    for line in text[2:]:
        tmp = line
        # 标题加粗
        if len(line) > 1:
            i = 0
            while line[i] == ' ' :
                i += 1
            if line[i] == '`':
                flag = not flag
            elif flag or line[i] == '\t' or line[i] == '|' or line[i] == '!':
                pass
            elif re.search('#+(.*)',line):
                title = re.search('#*(.*)',line).group(1)

                tmp = re.sub(title,'**'+title+'**',line);
            elif re.search('(-\s|\d\.\s|>)(.*)',line):
                title = re.search('(-\s|\d\.|>)(.*)',line).group(2)
                if len(title) > 1:
                    tmp = re.sub(title,'<font size=4>'+title,line);
                #print tmp
            else:
                 tmp = '<font size=4>'+line
        out += tmp
    # print out
    fp.write(out)
    fp.close()
