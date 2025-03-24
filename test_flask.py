{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d091374b-326f-45f9-80e2-2ad20bac5dfa",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "url = \"httpa;//127.0.0.1:5001/predict\"\n",
    "data = {\"feature\": [6, 148, 72,35, 0, 33.6,0.627,50]}\n",
    "response = requests.post(url, json=data)\n",
    "print(response.json"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
