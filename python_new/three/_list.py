bicycles = ['fenghuang', 'gnt', 'yongjiu', 'jiebao']

print(bicycles[0].title())

# last
print(bicycles[-1].title())

first_bicycle = bicycles[0]

print("The frist bicycle is "+first_bicycle)

bicycles[0] = 'aima'
print(bicycles[0])

bicycles.append("yamaha")

print(bicycles)


pcs=[]

pcs.append('hongqi')
print(pcs)
pcs.insert(0,'apple')
print(pcs)

# del pcs[0]

print(pcs)

# print(bicycles.pop(1))
a = bicycles.remove("aima")
print(bicycles)

to_expensive = 'yongjiu'

bicycles.remove(to_expensive)

print(bicycles)

print("\nBecause the bicycle is to expensive "+ to_expensive)



bicycles.sort()
print(bicycles)

sorted(bicycles,reverse=True)
print(bicycles)


zimu = ['a', 'c', 'b', 'd']

print(sorted(zimu,reverse=True))
# zimu.sort()

zimu.reverse()
print(zimu)

print(len(zimu))

print(zimu[-1])

for i in zimu:
    print(i)

peoples=['weiluming', 'xuyulin']