#coding: utf-8
from __future__ import division
import sys
import numpy as np

def getMatrixString(idx):
	A = data[idx].replace("\n", ";")
	while A[-1:] == ";":
		A = A[:-1]
	return A

data = input()
try:
	A = np.array(np.matrix(getMatrixString("A")))
	B = np.array(np.matrix(getMatrixString("B")))
	n, m = B.shape
	B = B.reshape(m, n)[0]
	#print type(A), A
	#print type(B), B
except:
	print "矩阵格式错误！"
	sys.exit(1)

def to_latex_bmatrix(A):
	n, m = A.shape
	latexStr = "\\begin{bmatrix}"
	for i in range(0, n):
		for j in range(0, m - 1):
			latexStr += "%f&" % (A[i, j])
		latexStr += "%f\\\\\\\\" % (A[i, m - 1])
		# 由于markdown的缘故，所以需要输出4个`\`供markdown转义
	latexStr += "\\end{bmatrix}"
	return latexStr

X, residuals, rank, s = np.linalg.lstsq(A, B)
#print x, residuals, rank, s
n, m = A.shape
if rank == m:
	print "我们已为您求得解"
else:
	print "原方程有无穷多个解，这里给出范数最小的解"
for i in range(0, m):
	print "$$x\_{%d} = %f$$" % (i + 1, X[i].round(4))


sys.exit(0)
