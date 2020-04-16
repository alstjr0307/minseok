import re
jpeg_head=b'\xFF\xD8\xFF\xE0'
jpeg_put=b'\xFF\xD9'

f= open(r'C:\Users\user\Desktop\text.docx', 'rb')
data = f.read()
f.close()

head_list=[match.start() for match in re.finditer(re.escape(jpeg_head), data)]
put_list=[match.start() for match in re.finditer(re.escape(jpeg_put), data)]

subdata= data[head_list[0]:put_list[0]+2]
img=open('img.jpg' , 'wb')
img.write(subdata)
img.close()
