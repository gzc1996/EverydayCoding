########three ways to add elements in list
member = ['aabb','葫芦娃',123]
print(member)
member.append('gzc')
print(member)
member.extend(['liangmeng','zhangzhisong'])
print(member)
member.insert(0,'joker')
print(member)
########three ways to delete elements in list
member.remove('aabb')
print(member)
del member[0]
print(member)
member.pop(1)
print(member)