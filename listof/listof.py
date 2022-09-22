import os
import pandas as pd
import sys
import tkinter.filedialog as tkfd

d_ext_desc = {'csv':'CSV file',
              'db':'Thumbnail',
              'doc':'Microsoft Word Document',
              'docx':'Microsoft Word Document',
              'GIF':'GIF Image file',
              'html':'HTML file',
              'ico':'Icon Image file',
              'jpg':'JPG Image file',
              'JPEG':'JPEG Image file',
              'json':'JSON file',
              'lnk':'Shortcut file',
              'msg':'Microsoft Outlook Message file',
              'pdf':'PDF file',
              'pkl':'Pickle (python) file',
              'png':'PNG Image file',
              'ppt':'Microsoft Powerpoint file',
              'pptx':'Microsoft Powerpoint file',
              'pst':'Microsoft Outlook Data file',
              'py':'Python file',
              'pyc':'Python file (compiled)',
              'rtf':'Rich Text Format',
              'svg':'SVG Image file',
              'txt':'Text document',
              'url':'Hyperlink',
              'vsd':'Microsoft Visio file',
              'xls':'Microsoft Excel file',
              'xlsb':'Microsoft Excel file',
              'xlsm':'Microsoft Excel (Macro-enabled) file',
              'xlsx':'Microsoft Excel file',
              'yml':'Requirements file (python)',
              'zip':'ZIP file'}

def ext_desc(ext):
    try:
        desc = d_ext_desc[ext]
    except KeyError:
        desc = ''
    else:
        pass
    return desc

def generate_index(path=None, max=500):
    # stops generating index whenever there are more than 500 records, to test if the script works
    # use 'max=0' to generate the full index
    
    path = path if path else tkfd.askdirectory() # Request path if not provided
    def size():
        file_size = [os.path.getsize(p) for p in paths]
        new_size=[]
        for i in file_size:
           new_size.append(float(round(i/ (1024 * 1024), 3))) # formula for converting bytes in gigabytes, upto 3 decimal places
        return new_size
    df = pd.DataFrame(columns=['File','Size in MB','File Type','Folder Location','Link','Path'])
    for root, _ , files in os.walk(path):
        files = [f for f in files if not f.startswith('~') and f!='Thumbs.db']
        paths = [os.path.join(root, f) for f in files]
        exts = [os.path.splitext(f)[1][1:].lower() for f in files]
        filetypes = [ext_desc(ext) for ext in exts]
        file_links = ['=HYPERLINK("{}","link")'.format(p) if len(p) < 256 else '' for p in paths]
        folders = [os.path.dirname(p) for p in paths]
        df1 = pd.DataFrame({'File': files,
                            'Size in MB': size(),
                            'File Type': filetypes,
                            'Folder Location': folders,
                            'Link': file_links,
                            'Path': paths})
        df = df.append(df1)
        if max and (df.shape[0]>max):
            break
    df = df.reset_index(drop=True)
    return df
  
if __name__ == '__main__':
    df = generate_index(max=0)
    df.to_excel('file_index.xlsx')