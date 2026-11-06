# Introduction to Apache ECharts

## What is Echarts

**Apache ECharts**

Apache ECharts is an open-source, powerful, and interactive data visualization library developed by the Apache Software Foundation. It is written in JavaScript and provides a highly customizable way to create a variety of charts and graphs.

![echarts](../../../../images/data_visualization/echarts/echarts.png)

## Features

**Rich Chart Types** – Supports bar charts, line charts, pie charts, scatter plots, maps, radar charts, heatmaps, and more.

**High Performance** – Built on canvas (instead of SVG), making it efficient for large datasets.

**Responsive & Interactive** – Supports zooming, tooltips, data highlighting, and real-time updates.

**Extensible** – Allows customization with themes and plugins.
Works with Multiple Frameworks – Supports Vanilla JavaScript, React, Vue, and Angular.

**Cross-platform** – Works in browsers and Node.js environments.


![features](../../../../images/data_visualization/echarts/features.png)

## ECharts: A Declarative Framework for Rapid Construction of Web-based Visualization

![declarative_framework1](../../../../images/data_visualization/echarts/declarative_framework1.png)

[ECharts: A Declarative Framework for Rapid Construction of Web-based Visualization](https://www.sciencedirect.com/science/article/pii/S2468502X18300068)

![declarative_framework2](../../../../images/data_visualization/echarts/declarative_framework2.png)

Examples of ECharts chart types. From top to down, left to right: scatterplot, line chart, candle-stick charts, geomap, radar chart, node-link graph, heatmap, tree diagram, sankey diagram, parallel coordinates, gauge chart, treemap.

![chart_types](../../../../images/data_visualization/echarts/chart_types.png)

## Who uses ECharts

![who_uses_echarts](../../../../images/data_visualization/echarts/who_uses_echarts.png)

## Powerful Visualization Capabilities

Here are some examples that you can see the richess of the chart types it offered,

### Radar charts

![example0](../../../../images/data_visualization/echarts/example0.png)

### GEO MAP

![example1](../../../../images/data_visualization/echarts/example1.png)

### Candle Stick

![example2](../../../../images/data_visualization/echarts/example2.png)

### Boxplot

![example3](../../../../images/data_visualization/echarts/example3.png)

### Heatmap

![example4](../../../../images/data_visualization/echarts/example4.png)

### Graph

![example5](../../../../images/data_visualization/echarts/example5.png)

### Lines

![example6](../../../../images/data_visualization/echarts/example6.png)

### Tree

![example7](../../../../images/data_visualization/echarts/example7.png)

### Treemap

![example8](../../../../images/data_visualization/echarts/example8.png)

### Sunburst

![example9](../../../../images/data_visualization/echarts/example9.png)

### Parallel

![example10](../../../../images/data_visualization/echarts/example10.png)

### Sankey

![example11](../../../../images/data_visualization/echarts/example11.png)

### Funnel

![example12](../../../../images/data_visualization/echarts/example12.png)

### Gauge

![example13](../../../../images/data_visualization/echarts/example13.png)

### PictorialBar

![example14](../../../../images/data_visualization/echarts/example14.png)

### Calendar

![example15](../../../../images/data_visualization/echarts/example15.png)

### Dataset

![example16](../../../../images/data_visualization/echarts/example16.png)

### 3D Bar

![example17](../../../../images/data_visualization/echarts/example17.png)

### 3D Scatter

![example18](../../../../images/data_visualization/echarts/example18.png)

### 3D Surface

![example19](../../../../images/data_visualization/echarts/example19.png)

### 3D Map

![example20](../../../../images/data_visualization/echarts/example20.png)

### Flow GL

![example21](../../../../images/data_visualization/echarts/example21.png)

## Let us run some code

* Save the following into `barchart.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ECharts Example with Vanilla JS</title>
  <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.1/dist/echarts.min.js"></script>
  <style>
    #main {
      width: 600px;
      height: 400px;
    }
  </style>
</head>
<body>
  <h2>ECharts Example</h2>
  <div id="main"></div>

  <script>
    // Initialize the chart
    var chart = echarts.init(document.getElementById('main'));

    // Chart options
    var option = {
      title: {
        text: 'ECharts Basic Example'
      },
      tooltip: {},
      legend: {
        data: ['Sales']
      },
      xAxis: {
        data: ['Shirts', 'Cardigans', 'Chiffon', 'Pants', 'Heels', 'Socks']
      },
      yAxis: {},
      series: [
        {
          name: 'Sales',
          type: 'bar',
          data: [5, 20, 36, 10, 10, 20]
        }
      ]
    };

    // Set the options
    chart.setOption(option);
  </script>
</body>
</html>
```

* Open it with your browser (Chrome or firefox).

![barchart0](../../../../images/data_visualization/echarts/barchart0.png)

* The html will be rendered in the broswer like the following.

![barchart](../../../../images/data_visualization/echarts/barchart.png)

**This code:**

* Loads ECharts from a CDN.
* Creates a div element as a container.
* Initializes an ECharts instance and configures a basic bar chart.
* Renders the chart inside the container.

>Hint: For doing any future works, we could,
* modify the above html to fit our need.
* just use the cdn url for the js library of the echarts for the rest of the tutorials.

### Ref

- https://echarts.apache.org/en/index.html