{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "99707b77",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[46, 55]\n",
      "[66, 79]\n"
     ]
    }
   ],
   "source": [
    "def matrix_multiply(A, B):\n",
    "    n = len(A)\n",
    "    C = [[0] * n for _ in range(n)]\n",
    "    for i in range(n):\n",
    "        for j in range(n):\n",
    "            for k in range(n):\n",
    "                C[i][j] += A[i][k] * B[k][j]\n",
    "    return C\n",
    "\n",
    "def matrix_power(A, m):\n",
    "    n = len(A)\n",
    "\n",
    "    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]\n",
    "\n",
    "    base = A\n",
    "\n",
    "    while m > 0:\n",
    "        if m % 2 == 1:\n",
    "            result = matrix_multiply(result, base)\n",
    "        base = matrix_multiply(base, base)\n",
    "        m //= 2\n",
    "\n",
    "    return result\n",
    "\n",
    "A = [[4, 5],\n",
    "     [6, 7]]\n",
    "m = 2\n",
    "\n",
    "result = matrix_power(A, m)\n",
    "for row in result:\n",
    "    print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd8d510b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
