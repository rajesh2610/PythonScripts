temperatures = [10,-20,-289,100];

def conv(deg):
    f = (deg*9)/5 + 32;
    f = str(f);
    return f;

file = open("temperatures in F.txt",'w+');

for temp in temperatures :
  if temp >= -273.15 :
    file.write(conv(temp)+'\n');


content = file.read();
print(content);
# file = open("References.txt",'r+');
# file.write('Nigger Hello');
# file.write('Line 4 \n')
# #file
# content  = file.readlines();
# print (content);
# content = [i.rstrip('\n') for i in content]
# print (content)
# file.close()
# with open('references.txt','a+') as file :
#     file.seek(0);
#     content = file.read()
#     file.write("\nLine 6")
#     print (content);
