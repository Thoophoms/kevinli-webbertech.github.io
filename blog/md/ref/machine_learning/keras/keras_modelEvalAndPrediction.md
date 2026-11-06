# Keras - Model Evaluation and Model Prediction

## Model Evaluation

Model evaluation is a process during the development of the model to check whether the model is a good fit for the given problem and corresponding data. 

Keras provides a function, `evaluate`, for model evaluation. This function assesses the performance of the model on the test data and returns the loss value and metrics.

### Function

```python
model.evaluate(x, y, verbose=...)
```
Keras provides a function, `evaluate`, for model evaluation. It has three main arguments:

- **Test data**
- **Test data label**
- **Verbose**: `True` or `False`


##  Evaluate the Model

To evaluate the model, use the following code:

```python
score = model.evaluate(x_test, y_test, verbose=0)

print('Test loss:', score[0])
print('Test accuracy:', score[1])
```

**Output:**
0
The test accuracy is 98.28%.

## Model Prediction

Prediction is the final step and the expected outcome of the model generation.

The signature of the `predict` method is as follows:

```python
predict(
   x, 
   batch_size=None, 
   verbose=0, 
   steps=None, 
   callbacks=None, 
   max_queue_size=10, 
   workers=1, 
   use_multiprocessing=False
)
```
## Prediction for Our MLP Model

To make predictions with the model, use the following code:

```python
pred = model.predict(x_test) 
pred = np.argmax(pred, axis=1)[:5] 
label = np.argmax(y_test, axis=1)[:5] 

print(pred) 
print(label)
```


The output of the above application is as follows:


[7 2 1 0 4] 
[7 2 1 0 4]


