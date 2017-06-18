def test(*para):
    num = len(para)
    print('参数个数为：',num)
    if num > 2:
        print('第二个参数为：', para[1])


test(1,'yuwei',546,7,8,89,78,987)
    
