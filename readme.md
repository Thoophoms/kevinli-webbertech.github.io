# Resources

https://www.tradingview.com/widget-docs/widgets/charts/advanced-chart/
https://www.tradingview.com/widget-docs/widgets/charts/symbol-overview/
https://stackoverflow.com/questions/48272265/left-column-fixed-until-right-column-is-scrollable

## Run build.sh

* Run `build.sh` to generate the uglified js and all the html files are ok.
  It calls the script from the package.json.
* Only blog.html will need to be unlocked.

## Run test_website.sh

This is another way of testing blank or 404 pages. Maybe the blank pages function needs to be revisited by right now it is faster than the Google chrome plugin.

```shell
(base) xiaofengli@xiaofenglx:~/git/kevinli-webbertech.github.io$ ./test_broken_links.sh 
debugging here...
https://kevinli-webbertech.github.io/css/index.css, status_code: 200
https://kevinli-webbertech.github.io/css/tree.css, status_code: 200
https://kevinli-webbertech.github.io/blog/html/learning_resources.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/database/mysql_driver.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/scikit_learn/clustering.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/scikit_learn/dimensionality_reduction.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/scikit_learn/anomaly_detection.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/scikit_learn/casestudies.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/scikit_learn/advanced_topics.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/scikit_learn/resources.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_intro.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_installation.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_backendConfiguration.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_module.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_layer.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_model.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_model_compilation.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_modelEvalAndPrediction.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_ConvolutionNeuralNetwork.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_RegressionPrediction_MPL.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_TimeSeriesPrediction_LSTM_RNN.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_application.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_RealTimePrediction_ResNet_Model.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/ref/machine_learning/keras/keras_Pre-TrainedModels.html, status_code: 200
https://kevinli-webbertech.github.io/blog/html/courses_list.html, status_code: 200
https://kevinli-webbertech.github.io/index.html, status_code: 200
==============Printing Broken Links======================
https://kevinli-webbertech.github.io/blog/html/courses/data_visualization/mathplotlib/homework/homework2.html
https://kevinli-webbertech.github.io/blog/html/courses/computer_architecture/quantum.html
https://kevinli-webbertech.github.io/blog/html/courses/dev_ops/k8s/k8s_basic.html
https://kevinli-webbertech.github.io/blog/html/courses/dev_ops/k8s/k8s_config.html
https://kevinli-webbertech.github.io/blog/html/courses/dev_ops/k8s/k8s_lab1.html
https://kevinli-webbertech.github.io/blog/html/courses/dev_ops/k8s/k8s_lab2.html
https://kevinli-webbertech.github.io/blog/html/courses/dev_ops/k8s/k8s_security.html
https://kevinli-webbertech.github.io/blog/html/ref/python/pandas/Pandas_IOtools.html
https://kevinli-webbertech.github.io/blog/html/ref/mobile/flutter.html
```

### Other linkchecker of Python

* `pip3 install linkchecker`

* `linkchecker http://www.example.org/myhomepage/`

#### Ref

`https://linkchecker.github.io/linkchecker/` 

#### TODO

Cleanup this file
