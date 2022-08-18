#this script takes two input subtitle files and copies the 1st file's timestamps into the second one, replacing the second file's timestamps
import sys
import string
import re


'''
00:00:05.100 --> 00:00:16.040
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
                        print(k,j)
                        text[-1] += line
                    else:
                        text.append(line)
                    k = j
            except IndexError as e:
                print('ERROR')
                text.append(line)
    return text
        
def print_newfile(a,b,b_fn,ext):
    with open(b_fn[:-4] + "_new" + ext, 'w', encoding='UTF-8') as newfile:
        for i,t in enumerate(a):
            newfile.write(str(i+1))
            newfile.write('\n')
            newfile.write(str(t))
            try:
                newfile.write(str(b[i]))
            except IndexError as e:
                print(i)
                print(e)
            newfile.write('\n')
'''  
def print_to_file(filename: str, subtitles: dict, ext: str):
    print('Printing to file')
    with open(filename + "_new" + ext, 'w', encoding='UTF-8') as newfile:
        if ext == '.srt':
            for k,v in subtitles.items():
                newfile.write(str(k))
                newfile.write('\n')
                try:
                    newfile.write(v[0] + " --> " + subtitles[k+1][0])
                except KeyError:
                    newfile.write(v[0] + " --> " + subtitles[k][0])
                newfile.write('\n')
                try:
                    [newfile.write(t+'\n') for t in v[1:]]
                except UnicodeEncodeError as e:
                    print(e)
                    print('Unprintable char is in: ',v[1:])
                                
                newfile.write('\n')
                newfile.write('\n')
        elif ext == '.vtt':
            pass

'''

if __name__ == "__main__":
    if len(sys.argv) == 3:
        a = str(sys.argv[-2])
        b = str(sys.argv[-1])
        print_newfile(retrieve_timestamps(a),retrieve_text(b),b,'.srt')
    else:
        print("2 args required: input filename 1 and input filename 2. Example: 'python convert.py input.srt input.srt'")
