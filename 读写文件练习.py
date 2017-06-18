f=open('record.txt')

boy=[]
girl=[]
count=1

for each_line in f:
    if each_line[:6] != '======':
        (role, line_spoken) = each_line.split(':',1)
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_spoken)
    else:
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'

        boyFile = open(file_name_boy, 'w')
        girlFile = open(file_name_girl, 'w')

        boyFile.writelines(boy)
        girlFile.writelines(girl)

        boyFile.close()
        girlFile.close()
        
        boy=[]
        girl=[]
        count += 1



f.close()
