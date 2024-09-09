class person:
    name ="waleed"
    position='Data scientist'
    networth='1000000000000000000000000000000000000000000000000'
    def info(self):
        print(f'{self.name} is {self.position}')


a=person()
b=person()

b.name='waleed1'
b.position='data engineer'

a.info()
b.info()