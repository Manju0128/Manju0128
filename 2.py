{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cb6ba293",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the size of the list 8\n",
      "Enter element 1: 1\n",
      "Enter element 2: 2\n",
      "Enter element 3: 3\n",
      "Enter element 4: 4\n",
      "Enter element 5: 5\n",
      "Enter element 6: 6\n",
      "Enter element 7: 7\n",
      "Enter element 8: 8\n",
      "The range of the list is  7\n"
     ]
    }
   ],
   "source": [
    "def difference(arr):\n",
    "  if (len(arr) <=  3 ):\n",
    "    return -1\n",
    "  # maximum = max(arr)\n",
    "  # return max(arr) - min(arr)\n",
    "  maximum = max(arr)\n",
    "  minimum = min(arr)\n",
    "  return (int(maximum) - int(minimum))\n",
    "\n",
    "list_size = int(input(\"Enter the size of the list \"))\n",
    "arr = []\n",
    "\n",
    "for i in range(list_size):\n",
    "  element = input(f\"Enter element {i+1}: \")\n",
    "  arr.append(element)\n",
    "\n",
    "range1 = difference(arr)\n",
    "if range1 <= 0:\n",
    "  print(\"Range determination not possible\")\n",
    "else:\n",
    "  print(\"The range of the list is \", range1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "370f3d61",
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
