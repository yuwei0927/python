import time as t

class MyTimer():
	#begin 
	def start(self):
		self.begin = t.localtime()
		print('计时开始...')

	#end
	def stop(self):
		self.end = t.localtime()
		self._calc()
		print('计时结束！')

	#内部方法，计算运行时间
	def _calc(self):
		self.lasted=[]
		self.prompt='总共运行了'
		for index in range(6):
			self.lasted.append(self.end[index] - self.begin[index])
			if self.lasted[index]:
				self.prompt +=  (str(self.lasted[index]) + self.unit[index])

	def __str__(self):
		return self.prompt

	__repr__ =  __str__

	def __init__(self):
		self.prompt='未开始计时！'
		self.begin = 0
		self.end = 0
		self.lasted = [] 
		self.unit = ['年','月','天','小时','分钟','秒']
		self.flag = 0

	def __add__(self, other):
                prompt = "总共运行了"
                result = []
                for index in range(6):
                    result.append(self.lasted[index] + other.lasted[index])
                    if result[index]:
                        prompt += (str(result[index]) + self.unit[index])
                return result
        

