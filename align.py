#this script takes two input subtitle files and copies the 1st file's timestamps into the second one, replacing the second file's timestamps within a new subtitle (.srt) file.
import sys
import string
import re
import math

'''
the required timestamp formats for input .vtt or .srt files are:
00:00:05.100 --> 00:00:16.040
or
00:00:05,100 --> 00:00:16,040

'''

def retrieve_timestamps(i: str):
    with open(i, mode='r',encoding='UTF-8') as myfile:
        try:
            lines = myfile.readlines()
        except Exception as e:
            print(e)
            print('No such readable file: ',filename)
        timestamps = []
        for j,line in enumerate(lines):
            if (line[13:16].strip() == '-->') & (line[-3:].strip().isdigit()):
                timestamps.append(line)
    #print(timestamps)
    return timestamps
    
    
def retrieve_text(i: str):     
    with open(i, mode='r',encoding='UTF-8') as myfile:
        try:
            lines = myfile.readlines()
        except Exception as e:
            print(e)
            print('No such readable file: ',filename)
        text = []
        k = 0
        for j,line in enumerate(lines):
            try:
                if (line[13:16] != '-->') & (line[-3:].isdigit() == False) & ((line.strip().isdigit() == False) & (lines[j-1] != "")) & (line.strip() != "") & (line.strip() != "WEBVTT"):
                    #print(j)
                    #print(k)
                    #print('\n')
                    if k == (j-1):
                        #print(k,j)
                        text[-1] += line
                    else:
                        text.append(line)
                    k = j
            except IndexError as e:
                print('ERROR')
                text.append(line)
    return text

def redistribute_texts(a: list,b: list):
    #if there are more timestamps than text slices, function adds an empty text chunk (a dash)
    print('There are ',len(a)-len(b),' more timestamps than text slices')
    diff = len(a)-len(b)
    rem = len(a)%len(b)
    insertion_interval = math.floor(len(a)/diff)
    for i in range(insertion_interval,len(a),insertion_interval):
        #print(i)
        b.insert(i,'-\n')
    return a,b
    
def concat_texts(a: list,b: list):
    print('There are ',len(b)-len(a),' more text slices than timestamps')
    #print(len(b)%len(a))
    #print(len(b)/len(a))
    #print(len(a)/(len(b)%len(a)))
    j = 0
    k = 0
    b1 = []
    for x in a:
        try:
            to_append = b[j] + b[j+1]
            if k <= (len(b)%len(a)):
                to_append += b[j+2]
                j+=1
                k+=1
            b1.append(to_append)
            j+=2
        except IndexError as e:
            try:
                to_append = b[j]
                b1.append(to_append)
            except IndexError as e:
                print(e)
    return a,b1

def print_newfile(a: list,b: list,b_fn,ext):
    if len(a) > len(b):
        a,b = redistribute_texts(a,b)
    elif len(a) < len(b):
        a,b = concat_texts(a,b)
        
    with open(b_fn[:-4] + "_new" + ext, 'w', encoding='UTF-8') as newfile:
        for i,t in enumerate(a):
            newfile.write(str(i+1))
            newfile.write('\n')
            newfile.write(str(t))
            try:
                newfile.write(str(b[i]))
                newfile.write('\n')
            except IndexError as e:
                #print(i)
                #print(e)
                pass

if __name__ == "__main__":
    if len(sys.argv) == 3:
        a = str(sys.argv[-2])
        b = str(sys.argv[-1])
        print_newfile(retrieve_timestamps(a),retrieve_text(b),b,'.srt')
    else:
        print("2 args required: input filename 1 and input filename 2. Example: 'python align.py input.srt input.srt'")
