# PROJECT COURSES ON COMPUTER GRAPHICS
## 1 INTRODUCTION
In this project, I need to develop a simple interface to display 3D human skeletons from structured 3D data. A 3D skeleton is composed of a pre-defined structure of:
- 17 joints
- 16 ‘bones’ connecting joints
### 1.1	STRICT REQUIREMENTS
I am required to deliver:
- A functioning code that can read a JSON file containing only one 3D pose and
display a very simple 3D skeleton (it can be composed, for example, of spheres for the joints and cylinders for the bones, like in the picture below).
- A camera rotating in a circular path around the skeleton, or, alternatively, you may rotate the skeleton around the vertical axis to emulate the camera movement.
- A simple surrounding environment. It may be composed of simple 3D geometry primitives (cubes, spheres, etc.) or other, more complex meshes.
- A report document explaining your project, including how the code is organized
- A document explaining in detail how to run the code and the used libraries
- A short video showing the results of your project

### 1.2	BONUSES
In order to aim to a higher mark, these are some examples of bonus requirements that you
may fulfill:
- Read a JSON file containing more than one 3D pose and animate the 3D skeleton accordingly (by iterating the poses in the JSON file).
- “Dress up” the skeleton in whichever way you like: you may add hands, hats, shoes or whatever you like the most
- Dynamic camera controls: pan, tilt, zoom in the scene using mouse and keyboard
- Graphics additions in general: you may decide to substitute cylinders with meshes of 3D bones, for example, or design a complex surrounding environment using meshes
instead of simple primitives
- A GitHub repository containing the code and the additional reports
- Any additional feature, if well documented, will be considered as a bonus
## 2 FEATURES
### 2.1	PRIMITIVES
There are different kinds of primitives that can be found in this project, including cubes, cylinders, spheres, and lines. Here I will explain how I created them.
#### 2.1.1 CUBES
The cube consists of 6 faces and each face can be created by calling `glBegin(GL_QUADS)`.
#### 2.1.2 CYLINDERS
There is a function `gluCylinder()` which can be used for drawing a cylinder.
#### 2.1.3 SPHERES
There is a function `gluSphere()` which can be used for drawing a sphere. Use `glTranslate()` to move from the center to the point and draw the sphere using the `gluSphere()`.
#### 2.1.4 LINES
Lines are easy to be created by calling `glBegin(GL_LINES)` with the start and end point of the line.
### 2.2 ANIMATION:
The skeleton is able to move continuously thanks to different pose data from JSON files. A while statement and JSON lib help keep reading pose data from predefined files.   
There are 371 JSON files (from `0.json` to `370.json`) containing the pose data in the folder “`animation`”. Inside the while loop, one JSON file is loaded. The skeleton is then rendered depending on the pose data. At the end of each loop, the index indicator variable idx is increased by 1 and it will be set to 0 every time after it is over 370.    
The speed of the animation depends on the variable FrameSpeed which can be changed as needed. The value in the sample is 20 which means the screen will be refreshed and the skeleton will change its pose every 20 milliseconds.  
### 2.3 TEXTURE
A picture is mapped to a cube as a texture. And another skybox picture is mapped as the background of this project.
#### 2.3.1 CUBE WITH TEXTURE
I use the function `loadImageToTexture()` to load the image into the memory and bind them to a texture with `GL_TEXTURE_2D` type. The function `drawCube()` uses this texture map on the 6 faces of the cube.  
This process uses “Fixed Function Pipeline” and it is mor often to implement it with shaders in modern OpenGL. In the function `drawCube()`, `glNormal3f()` is called to set the normal vector of the face. Function `glTexCoord2f()` and `glVertex3f()` are called to map the image to the specific vertex.  

#### 2.3.2 SKYBOX
Skybox technic assumes that the background of the scene is the inner side of a cube and 6 different images can make it feel like a real 3D view. I use function `load_cubemap()` to load six different images into the memory and bind them to a texture with `GL_TEXTURE_CUBE_MAP` type. In this case, `glTexImage2D()` function uses different targets, such as `GL_TEXTURE_CUBE_MAP_POSITIVE_X`, to specify different images.  
Function `loadSkybox()` generates vertex buffers for the next shader step. Function `render()` uses shaders and buffers to draw the skybox by calling function `glDrawArrays()`.  
This process applies vertex and fragment shaders by calling function `load_shaders()`. Shaders are written in GSGL in separate files under the folder “`shaders`”.  
After setting up everything, a skybox texture has a view as the following:  
### 2.4 LIGHTING
A point that indicates the light source is created in the project. The light models I implemented are ambient light and diffuse light.

The function `drawLightBulb()` draws a small grey ball in the scene which is the same location as the source of the diffuse light. This small ball will be fixed in the screen because it is moving with the camera view.

When the odjects are moving closer to the light source (the small grey ball in this case), different lighting effects can be seen as the following:
### 2.5 CAMERA CONTROL 
The keyboard can be used to control the view of the scene in this project. All the active keys are implemented in the function getInput().
Active keys and their usages are listed below:
“u”: rotate the camera view down  
“i”: rotate the camera view up  
“j”: rotate the camera view right  
“k”: rotate the camera view left  
“n”: camera view clockwise tilt  
“m”: camera view counterclockwise tilt  

“w”: move the camera view into the screen (zoom in, go towards the objects)  
“s”: move the camera view out of the screen (zoom out, go backward the objects)  
“a”: move the camera view left horizontally (objects go right)  
“d”: move the camera view right horizontally (objects go left)  

“z”: the skeleton rotates around its x-axis (the red axis)  
“x”: the skeleton rotates around its y-axis (the green axis)  
“c”: the skeleton rotates around its z-axis (the blue axis)  

The control of the camera view is implemented by applying transformations to 3 different view matrices. These matrices are defined as global variables that are viewMatrix_skeleton, viewMatrix_objects, and viewMatrix_sky.  

pygame.key.get_pressed() is used to get the pressed key in order to invoke a callback. In the callback function, different transformations can be applied to different matrices.   

Especially, in order to make the transformation more human-readable and object-oriented, I created a python class matrix in the file “mtx.py”. This class implements 2 different transformations of translation and rotation because the results are different based on the different coordinates (object and eye coordiates).  

### 2.6 GITHUB and demo video
Github: https://github.com/dhao24/cg_project
Demo video: https://youtu.be/hfDZ-DMDJck

## 3 FUTURE IMPROVEMENTS
1.	There are more tutorials using C++ and it is more common to implement OpenGL projects in C++ so I would like to try it in C++ if I want to do it again, although it will be more complicated to set up the environment for compiling and running the program.
2.	Instead of “Fixed Function Pipeline” (for example `glBegin`, `glEnd`, `glTranslate`, `glRotate`), I would use more Shaders that are more modern for GPU.
3.	Complex mesh objects are missing in this project so I would like to use tools, like Blender to create nice mesh adding to this project instead of primitives.

## 4 REFERENCES
https://learnopengl.com/  
https://pythonprogramming.net/opengl-pyopengl-python-pygame-tutorial/  
https://www.youtube.com/watch?v=mOTE_62i5ag&t=126s  
https://www.youtube.com/watch?v=W3gAzLwfIP0&list=PLlrATfBNZ98foTJPJ_Ev03o2oq3-GGOS2  
https://www.opengl-tutorial.org  
https://nehe.gamedev.net

