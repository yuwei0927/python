import re
import pickle
import time
pickle_file = open('area.pkl','rb')
pickle_ip = open('Address_dict.pkl','rb')
area = pickle.load(pickle_file)
city = pickle.load(pickle_ip)
#Errors=['验证通过!','身份证号码位数不对!','身份证号码出生日期超出范围或含有非法字符!','身份证号码校验错误!','身份证地区非法!']
def checkIdcard(idcard):
    Errors=['验证通过!','身份证号码位数不对!','身份证号码出生日期超出范围或含有非法字符!','身份证号码校验错误!','身份证地区非法!']
    #area={"11":"北京","12":"天津","13":"河北","14":"山西","15":"内蒙古","21":"辽宁","22":"吉林","23":"黑龙江","31":"上海","32":"江苏","33":"浙江","34":"安徽","35":"福建","36":"江西","37":"山东","41":"河南","42":"湖北","43":"湖南","44":"广东","45":"广西","46":"海南","50":"重庆","51":"四川","52":"贵州","53":"云南","54":"西藏","61":"陕西","62":"甘肃","63":"青海","64":"宁夏","65":"新疆","71":"台湾","81":"香港","82":"澳门","91":"国外"}
    idcard=str(idcard)
    idcard=idcard.strip()
    idcard_list=list(idcard)
   #地区校验
    if(not area[(idcard)[0:2]]): 
        print (Errors[4])
   #15位身份号码检测
    if(len(idcard)==15):
        if((int(idcard[6:8])+1900) % 4 == 0 or((int(idcard[6:8])+1900) %100 == 0 and (int(idcard[6:8])+1900) % 4 == 0 )):
            erg=re.compile('[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[/hide]')#//测试出生日期的合法性
        else:
            ereg=re.compile('[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[/hide]')#//测试出生日期的合法性
        if(re.match(ereg,idcard)):
            #get_ip = idcard[:6]
            #ip = '%s'%get_ip
            #print(city['%s'%get_ip])
            get_id(idcard)
        else:
            print (Errors[2])
   #18位身份号码检测
    elif(len(idcard)==18):
       #出生日期的合法性检查
       #闰年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))
       #平年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))
        if(int(idcard[6:10]) % 4 == 0 or (int(idcard[6:10]) % 100 == 0 and int(idcard[6:10])%4 == 0 )):
            ereg=re.compile('[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]')#[/hide]')#//闰年出生日期的合法性正则表达式
        else:
            ereg=re.compile('[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]')#[/hide]')#//平年出生日期的合法性正则表达式
       #//测试出生日期的合法性
        if(re.match(ereg,idcard)):
           #//计算校验位
            S = (int(idcard_list[0]) + int(idcard_list[10])) * 7 +(int(idcard_list[1]) + int(idcard_list[11])) * 9 +(int(idcard_list[2]) + int(idcard_list[12])) * 10 +(int(idcard_list[3]) + int(idcard_list[13])) * 5 +(int(idcard_list[4]) + int(idcard_list[14])) * 8 +(int(idcard_list[5]) + int(idcard_list[15])) * 4 +(int(idcard_list[6]) + int(idcard_list[16])) * 2 +int(idcard_list[7]) * 1 + int(idcard_list[8]) * 6 +int(idcard_list[9]) * 3
            Y = S % 11
            M = "F"
            JYM = "10X98765432"
            M = JYM[Y]#判断校验位
            if(M == idcard_list[17]):#检测ID的校验位
                get_id(idcard)
            else:
                print (Errors[3])
        else:
            print (Errors[2])
    else:
        get_id(idcard)

def main():
    while True:
        idcard = input('输入需要检索的身份证号[退出按n]:')
        if idcard == 'n':
            break
        elif idcard == 'N':
            break
        else:
            checkIdcard(idcard)

def get_id(idcard):
    odd = ['1','3','5','7','9']  #定义奇数 
    get_ip = idcard[:6]          #获取身份证前6位数
    age = time.strftime('%Y')    #获得年份
    get_age = idcard[6:10]       #获取第六位到第十位数字 ,也就出生年份
    gender = idcard[-2]
    if gender in odd:
        print('\n性别:  男')
    else:
        print('\n性别:  女')
    print('年龄: ',int(age)-int(get_age))
    print('地址:',city['%s'%get_ip],'\n')
        
if __name__ == '__main__':
    main()
