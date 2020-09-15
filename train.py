import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np
#df = pd.read_csv('bitcoinEachMinute.csv')
#print(df)

def createModel(l1, l2):
    #prices = l1 #convert str to int
    inPrices = l1
    outValues = l2
    model = keras.Sequential([
        keras.layers.Dense(10, activation='relu'),
        keras.layers.Dense(2)
    ])
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
    model.fit(inPrices, outValues, epochs=5000)
    model.save('model')

    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    predictions = probability_model.predict([[10442.0189,
    10436.8317,
    10438.9549,
    10439.224,
    10434.1265,
    10434.2874,
    10436.8465,
    10433.411,
    10429.6035,
    10434.4509]])
    print(predictions[0])
    print(tf.nn.softmax(predictions[0]))
    print(np.argmax(predictions[0]))
    return np.argmax(predictions[0])

def formatData(prices):
    inPrices = []
    outValues = []
    for i in range(10, len(prices)):
        if prices[i] > prices[i-1]:
            outValues.append(1)
        else:
            outValues.append(0)
        #outPrices.append(prices[i])
        inList = []
        for j in range(0,10):
            inList.append(prices[i-10+j])
        inPrices.append(inList)
    print(inPrices)
    print(outValues)
    return inPrices, outValues

prices = [10442.0189,
10436.8317,
10438.9549,
10439.224,
10434.1265,
10434.2874,
10436.8465,
10433.411,
10429.6035,
10434.4509,
10434.46,
10437.1588,
10439.9283,
10440.1475,
10443.734,
10445.32,
10439.4681,
10438.6363,
10437.8479,
10437.7011,
10438.9971,
10442.8266,
10441.2071,
10442.8891,
10436.2156,
10434.3145,
10434.3726,
10435.686,
10439.6394,
10440.8368,
10441.7124,
10441.0201,
10437.0427,
10438.6573,
10438.1883,
10440.0283,
10436.5138,
10432.0019,
10430.5699,
10434.2459,
10435.6973,
10436.9217,
10436.7865,
10435.9693,
10433.4283,
10431.8991,
10428.1918
]

l1,l2 = formatData(prices)
createModel(l1, l2)

"""
def createModel(l1, l2):
    train_skills = [int(i) for i in l2] #convert str to int
    train_problems = []
    for item in l1:
        train_problems.append(mathEncoder(item))
    model = keras.Sequential([
        keras.layers.Dense(5, activation='relu'),
        keras.layers.Dense(4)
    ])
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
    model.fit(train_problems, train_skills, epochs=1000)
    model.save('models/sort/v1')
"""
