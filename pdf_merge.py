import PyPDF2
import os
import shutil

# remove all files from folder
# ask user to drag files to merge to the input folder
# get a user input once they've finished  adding
# merge files

def prelim():
    print('Move the files you wish to merge into the input folder. Type "done" when finished or "q" to quit')
    print("If order matters to you, number the files please")
    temp = input()
    while temp != 'done':
        if temp == 'q':
            return 0
        else:
            print('Move the files you wish to merge into the input folder. Type "done" when finished or "q" to quit')
            temp = input()
    return 1
        

def merger():
    if os.path.isdir('input'):
        shutil.rmtree('input')
    os.mkdir('input')
    
    if not prelim():
        return
    
    print(f'Attempting to merge {len(os.listdir("input"))} file(s)')
    
    merger = PyPDF2.PdfFileMerger()
    count = 0
    
    for fn in sorted(os.listdir('input')):
        if fn.endswith(".pdf"):
            print(fn)
            merger.append(f'input/{fn}')
            count += 1
    
    merger.write('input/out.pdf')
    print(f"Successfully merged {count} file(s)")
    
merger()
