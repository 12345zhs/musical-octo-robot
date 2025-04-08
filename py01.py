#集合 集合是无序的
# set={1,2,3}
# print(set)
# print(type(set))

# s1={}    #空字典
# print(type(s1))


s1=set()
print(s1,type(s1))

s1={"a","b","c"}
print(s1)
s2={1,2,3}
print(s2)

s1={1,2,3,1,2,3,4,5,6}
print(s1)

s2={1,2,3,4,5}
print(s2)
s2.add(6)
print(s2)
s2.add(6)
print(s2)
#s2.add(5,6)
s2.add((5,6))  #添加了一个元组
print(s2)

s2={1,2,3,4,5}
print("原集合：",s2)
s2.update("567")
print("现集合：",s2)
s2.update([5,6,7])
print(s2)


s2={1,2,3,4}
s2.remove(3)
print(s2)
#s2.remove(5)   没有5报错
print(s2)

s2={2,3,4,5,1}
s2.pop()
print(s2)
s2={"c","b","a","d"}
s2.pop()
print(s2)

s2={1,2,3,4}
print("原集合：",s2)
s2.discard(3)
print("现集合：",s2)
s2.discard(5)
print(s2)

a={"a","b"}
b={"b","c"}
print(a&b)

a={1,2,3,4}
b={3,4,5,6}  #并集的只会算作一次
print(a|b)
l=a|b
print(type(a|b))