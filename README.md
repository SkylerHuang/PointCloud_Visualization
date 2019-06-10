# PointCloud_Visualization
A Collection of point cloud visualization tools And the Usage of them

List:

* Render balls visualize(ToolOne)
* Matplot visualize(ToolTwo)



### Usage

***

Render balls visualize:

Dependency: Python2.7 (if you use python3, you need to update ` `python` path in .sh file)

Run ```sh compile_render_balls_so.sh``` to get .so file and then to run ```python show3d_balls.py```  to test if you have successfully compiled it.

You can visualize you point cloud by calling the ```showpoints()```function.

```
showpoints(pointcloud)
```

Get following rendering:

<img src="https://github.com/SkylerHuang/PointCloud_Visualization/blob/master/doc/render_balls.png" height="330" width="330" >
And you can set the color of the ball and background. see `show3d_balls.py` for more detailed.

## 

Matplotlib visualize

Install Matplotlib and mpl_toolkits

You can visualize you point cloud by calling the``` visual_pointcloud()```function.

```
visual_pointcloud(pointcloud)
```

Get following rendering:

<img src="https://github.com/SkylerHuang/PointCloud_Visualization/blob/master/doc/matplot.png" height="330" width="330" >
