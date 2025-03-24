{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eceffb26-5b29-41eb-8b87-3e3af858203c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask,request,jsonify\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "app=Flask(_name_)\n",
    "\n",
    "# load the tarined model\n",
    "model=joblib.load(\"model.pkl\")\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return \"Welcome to the ML model api!\"\n",
    "\n",
    "@app.route('/predict',methods=['POST'])\n",
    "def predict():\n",
    "    data=request.get_json()\n",
    "    features=np.array(data['features']).reshape(1,-1)\n",
    "    prediction=model.predict(features)\n",
    "    return jsonify({'prediction':prediction.tolist()})\n",
    "\n",
    "if _name_ == '_main_':\n",
    "    app.run(debug=True)"
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
