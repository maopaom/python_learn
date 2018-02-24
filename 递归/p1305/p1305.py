# -*- coding:utf-8 -*-
#二叉树

import sys

class define(object):
	#定义每一个节点的状态
	def __init__(self,data):
		self.data = data
		self.leftchild = None
		self.rightchild = None

def insertleft(root,nood):
	#插入一个左子树
	if root:
		if root.leftchild:
			#如果左边子树已经有的话就继续向左
			insertleft(root.leftchild,nood)
		else:
			root.leftchild = nood

def insertright(root,nood):
	#插入一个右子树
	if root:
		if root.rightchild:
			insertright(root.rightchild,nood)
		else:
			root.rightchild = nood

def pre_order(root):
	if root:
		print(root.data)
		pre_order(root.rightchild)
		pre_order(root.leftchild)

number = sys.stdin.readline()
number = list(number)
number.pop()
numbers = ''
for i in number:
	numbers = numbers + i
numbers = int(numbers)

first_string = sys.stdin.readline()
first_string = list(first_string)

for i in range(1,numbers):
	string = list(sys.stdin.readline())
	string_root = string[0]
	for i in range(len(first_string)):
		if string_root == first_string[i]:
			first_string.insert(i+1,string[1])
			first_string.insert(i+2,string[2])

first_string.pop()
for i in range(len(first_string)):
	for j in range(len(first_string)):
		if first_string[j] == '*':
			del first_string[j]
			break

for i in first_string:
	print(i,end = '')


#感觉并没有用到二叉树
#不过学习了一下递归来表示二叉树





