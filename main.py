import os

print("Enter the project name: ")
fileName = input();
path = f"D:\JAVASCRIPT_CODE\{fileName}"

try:
    os.mkdir(path)
    print(f"Project created of name : {fileName}");
except FileExistsError:
    print(f"A Project of name: {fileName} already exists!")

with open(f'D:\JAVASCRIPT_CODE\{fileName}\index.html','w') as h:
    line1 = f"<!DOCTYPE html> \n"
    line2 = f'      <html lang="en">  \n'
    line3 = f'      <head> \n'
    line4 = f'            <meta charset="UTF-8" /> \n'
    line5 = f'            <meta http-equiv="X-UA-Compatible" content="IE=edge" /> \n'
    line6 = f'            <meta name="viewport" content="width=device-width, initial-scale=1.0" /> \n'
    line7 = f'            <title>Document</title> \n'
    line8 = f'            <link rel="stylesheet" href="style.css" /> \n'
    line9 = f'        </head> \n'
    line10 = f'        <body> \n'
    line11 = f'            <script src="script.js"></script> \n'
    line12 = f'       </body> \n'
    line13 = f'       </html> \n'
    h.writelines([line1 ,line2,line3,line4 ,line5,line6,line7 ,line8,line9,line10 ,line11,line12,line13])
    h.close()


with open(f'D:\JAVASCRIPT_CODE\{fileName}\style.css','w') as s:
    line14 = f'*{{ \n'
    line15 = f' margin: 0px; \n'
    line16 = f' padding: 0px; \n'
    line17 = f'}} \n'

    s.writelines([line14,line15,line16,line17])
    s.close()

with open(f'D:\JAVASCRIPT_CODE\{fileName}\script.js','w') as sc:
    sc.close()