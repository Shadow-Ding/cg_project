# Install requirements:
# pip install pyopengl

import math
import numpy as np
from typing import List
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import shaders

import json
from PIL import Image
import mtx

FrameSpeed=20
lengthRatio=500
lengthRatio_nehe=2
verticies = ((0,0,0),(1,0,0),(0,1,0),(0,0,1))
lineOrder=(
    (0,1),
    (0,4),
    (0,7),
    (1,2),
    (2,3),
    (4,5),
    (5,6),
    (7,8),
    (8,9),
    (8,11),
    (8,14),
    (9,8),
    (9,10),
    (11,12),
    (12,13),
    (14,15),
    (15,16)
    )

skyBoxFiles_path=(
    "skybox/skybox/left.jpg",
    "skybox/skybox/right.jpg",
    "skybox/skybox/bottom.jpg",
    "skybox/skybox/top.jpg",
    "skybox/skybox/back.jpg",
    "skybox/skybox/front.jpg"
)

imageName="Lena.png"

lightPos=[1.5,-2.0,-3.0]
rotation_sky_xp=[1,1,0,0]
rotation_sky_xn=[-1,1,0,0]
rotation_sky_yp=[1,0,1,0]
rotation_sky_yn=[-1,0,1,0]
rotation_sky_zp=[1,0,0,1]
rotation_sky_zn=[-1,0,0,1]

def light():
    """
    lighting test
    """
    glEnable(GL_LIGHT1)
    glLightfv( GL_LIGHT1, GL_AMBIENT, GLfloat_4(0.2, .2, .2, 1.0) )
    glLightfv(GL_LIGHT1, GL_DIFFUSE, GLfloat_3(.8,.8,.8))
    glLightfv(GL_LIGHT1, GL_POSITION, GLfloat_4(lightPos[0],lightPos[1],lightPos[2],1.0))

def loadImageToTexture():
    """Load an image file as a 2D texture using PIL"""
    im= Image.open(imageName)
    ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBX",0,-1)
    ID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, ID)
    glTexImage2D( GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image )
    glShadeModel(GL_SMOOTH)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    # glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL) # help make the texture not affected by glcolor
    glBindTexture(GL_TEXTURE_2D, 0)
    return ID

def setTexture():
    """
    docstring
    """
    glEnable(GL_TEXTURE_2D)
    glShadeModel(GL_SMOOTH)
    # glDisable( GL_LIGHTING) # context lights by default
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL) # help make the texture not affected by glcolor
    # glEnable ( GL_COLOR_MATERIAL ) # color of the polygon
    glDisable(GL_TEXTURE_2D)

def drawCube(ID):
    """Draw a cube with texture coordinates"""
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, ID)
    glEnable ( GL_COLOR_MATERIAL ) # color of the polygon
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL) # help make the texture not affected by glcolor

    glPushMatrix()
    glTranslatef(0, 3, 0)  # Move to the place
    glRotate(90,1,0,0)
    glBegin(GL_QUADS)
    glNormal3f( 0.0, 0.0, 1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)

    glNormal3f( 0.0, 0.0,-1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)

    glNormal3f( 0.0, 1.0, 0.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)

    glNormal3f( 0.0,-1.0, 0.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)

    glNormal3f( 1.0, 0.0, 0.0)
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)

    glNormal3f(-1.0, 0.0, 0.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable ( GL_COLOR_MATERIAL ) # color of the polygon
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)

def nehe_draw():
    """
    from nehe tutorial
    """
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); # Clear The Screen And The Depth Buffer
    # glLoadIdentity();                   # Reset The View
    # glTranslatef(-1.5f,0.0,-6.0);             # Move Left And Into The Screen
    # glRotatef(rtri,0.0,1.0,0.0);             # Rotate The Pyramid On It's Y Axis
    glBegin(GL_TRIANGLES);                  # Start Drawing The Pyramid
    
    glColor3f(1.0,0.0,0.0)          # Red
    glVertex3f( 0.0/lengthRatio_nehe, 1.0/lengthRatio_nehe, 0.0/lengthRatio_nehe)        # Top Of Triangle (Front)
    glColor3f(0.0,1.0,0.0);          # Green
    glVertex3f(-1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe, 1.0/lengthRatio_nehe);          # Left Of Triangle (Front)
    glColor3f(0.0,0.0,1.0);          # Blue
    glVertex3f( 1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe, 1.0/lengthRatio_nehe);          # Right Of Triangle (Front)

    glColor3f(1.0,0.0,0.0);          # Red
    glVertex3f( 0.0/lengthRatio_nehe, 1.0/lengthRatio_nehe, 0.0/lengthRatio_nehe);          # Top Of Triangle (Right)
    glColor3f(0.0,0.0,1.0);          # Blue
    glVertex3f( 1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe, 1.0/lengthRatio_nehe);          # Left Of Triangle (Right)
    glColor3f(0.0,1.0,0.0);          # Green
    glVertex3f(1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe, -1.0/lengthRatio_nehe);         # Right Of Triangle (Right)

    glColor3f(1.0,0.0,0.0);          # Red
    glVertex3f( 0.0/lengthRatio_nehe, 1.0/lengthRatio_nehe, 0.0/lengthRatio_nehe);          # Top Of Triangle (Back)
    glColor3f(0.0,1.0,0.0);          # Green
    glVertex3f( 1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe, -1.0/lengthRatio_nehe);         # Left Of Triangle (Back)
    glColor3f(0.0,0.0,1.0);          # Blue
    glVertex3f(-1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe, -1.0/lengthRatio_nehe);         # Right Of Triangle (Back)

    glColor3f(1.0,0.0,0.0);          # Red
    glVertex3f( 0.0/lengthRatio_nehe, 1.0/lengthRatio_nehe, 0.0/lengthRatio_nehe);          # Top Of Triangle (Left)
    glColor3f(0.0,0.0,1.0);          # Blue
    glVertex3f(-1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe);          # Left Of Triangle (Left)
    glColor3f(0.0,1.0,0.0);          # Green
    glVertex3f(-1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe, 1.0/lengthRatio_nehe);          # Right Of Triangle (Left)

    glColor3f(0.0,0.0,1.0);          # blue
    glVertex3f( 1.0/lengthRatio_nehe, -1.0/lengthRatio_nehe, 1.0/lengthRatio_nehe);          # Top Of Triangle (Left)
    glColor3f(0.0,0.0,1.0);          # Blue
    glVertex3f(-1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe);          # Left Of Triangle (Left)
    glColor3f(0.0,0.0,1.0);          # Green
    glVertex3f(1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe, -1.0/lengthRatio_nehe);          # Right Of Triangle (Left)

    glColor3f(0.0,0.0,1.0);          # blue
    glVertex3f( 1.0/lengthRatio_nehe, -1.0/lengthRatio_nehe, 1.0/lengthRatio_nehe);          # Top Of Triangle (Left)
    glColor3f(0.0,0.0,1.0);          # green
    glVertex3f(-1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe, 1.0/lengthRatio_nehe);          # Left Of Triangle (Left)
    glColor3f(0.0,0.0,1.0);          # blue
    glVertex3f(-1.0/lengthRatio_nehe,-1.0/lengthRatio_nehe, -1.0/lengthRatio_nehe);          # Right Of Triangle (Left)

    glEnd()

#     glLoadIdentity();
    glPushMatrix()

    glTranslatef(1.5,0.0,-3.0);              # Move Right And Into The Screen
 
# glRotatef(rquad,1.0,1.0,1.0);            # Rotate The Cube On X, Y & Z
 
    glBegin(GL_QUADS);                  # Start Drawing The Cube

    glNormal3f( 0.0, 1.0, 0.0)
    glColor3f(0.0,1.0,0.0);          # Set The Color To Green
    glVertex3f( 1.0, 1.0,-1.0);          # Top Right Of The Quad (Top)
    glVertex3f(-1.0, 1.0,-1.0);          # Top Left Of The Quad (Top)
    glVertex3f(-1.0, 1.0, 1.0);          # Bottom Left Of The Quad (Top)
    glVertex3f( 1.0, 1.0, 1.0);          # Bottom Right Of The Quad (Top)

    glNormal3f( 0.0, -1.0, 0.0)
    glColor3f(1.0,0.5,0.0);          # Set The Color To Orange
    glVertex3f( 1.0,-1.0, 1.0);          # Top Right Of The Quad (Bottom)
    glVertex3f(-1.0,-1.0, 1.0);          # Top Left Of The Quad (Bottom)
    glVertex3f(-1.0,-1.0,-1.0);          # Bottom Left Of The Quad (Bottom)
    glVertex3f( 1.0,-1.0,-1.0);          # Bottom Right Of The Quad (Bottom)

    glColor3f(1.0,0.0,0.0);          # Set The Color To Red
    glVertex3f( 1.0, 1.0, 1.0);          # Top Right Of The Quad (Front)
    glVertex3f(-1.0, 1.0, 1.0);          # Top Left Of The Quad (Front)
    glVertex3f(-1.0,-1.0, 1.0);          # Bottom Left Of The Quad (Front)
    glVertex3f( 1.0,-1.0, 1.0);          # Bottom Right Of The Quad (Front)

    glColor3f(1.0,1.0,0.0);          # Set The Color To Yellow
    glVertex3f( 1.0,-1.0,-1.0);          # Bottom Left Of The Quad (Back)
    glVertex3f(-1.0,-1.0,-1.0);          # Bottom Right Of The Quad (Back)
    glVertex3f(-1.0, 1.0,-1.0);          # Top Right Of The Quad (Back)
    glVertex3f( 1.0, 1.0,-1.0);          # Top Left Of The Quad (Back)

    glColor3f(0.0,0.0,1.0);          # Set The Color To Blue
    glVertex3f(-1.0, 1.0, 1.0);          # Top Right Of The Quad (Left)
    glVertex3f(-1.0, 1.0,-1.0);          # Top Left Of The Quad (Left)
    glVertex3f(-1.0,-1.0,-1.0);          # Bottom Left Of The Quad (Left)
    glVertex3f(-1.0,-1.0, 1.0);          # Bottom Right Of The Quad (Left)

    glColor3f(1.0,0.0,1.0);          # Set The Color To Violet
    glVertex3f( 1.0, 1.0,-1.0);          # Top Right Of The Quad (Right)
    glVertex3f( 1.0, 1.0, 1.0);          # Top Left Of The Quad (Right)
    glVertex3f( 1.0,-1.0, 1.0);          # Bottom Left Of The Quad (Right)
    glVertex3f( 1.0,-1.0,-1.0);          # Bottom Right Of The Quad (Right)
    glEnd();                        # Done Drawing The Quad

    glPopMatrix()

def draw_ball():
    glEnable(GL_COLOR_MATERIAL)
    drawSphere(sphere,1.5,0.0,-3.0,0.5)
    glDisable(GL_COLOR_MATERIAL)

def load_shaders(vert_url, frag_url):
    vert_str = "\n".join(open(vert_url).readlines())
    frag_str = "\n".join(open(frag_url).readlines())
    vert_shader = shaders.compileShader(vert_str, GL_VERTEX_SHADER)
    frag_shader = shaders.compileShader(frag_str, GL_FRAGMENT_SHADER)
    program = shaders.compileProgram(vert_shader, frag_shader)
    return program

def initView_sky(width=800, height=600):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, float(width)/height, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)

    # viewMatrix_sky = glGetFloatv(GL_MODELVIEW_MATRIX)
    
    return glGetFloatv(GL_MODELVIEW_MATRIX)

def loadSkybox():
    global width, height, program
    global rotation, cubemap
    global skybox_vbo
    # global viewMatrix_sky

    # glEnable(GL_DEPTH_TEST)
    # glEnable(GL_TEXTURE_2D)
    # glEnable(GL_TEXTURE_CUBE_MAP)

    skybox_right = [1, -1, -1, 1, -1,  1, 1,  1,  1, 1,  1,  1, 1,  1, -1, 1, -1, -1]
    skybox_left = [-1, -1,  1, -1, -1, -1, -1,  1, -1, -1,  1, -1, -1,  1,  1, -1, -1,  1]
    skybox_top = [-1,  1, -1, 1,  1, -1, 1,  1,  1, 1,  1,  1, -1,  1,  1, -1,  1, -1]
    skybox_bottom = [-1, -1, -1, -1, -1,  1, 1, -1, -1, 1, -1, -1, -1, -1,  1, 1, -1,  1]
    skybox_back = [-1,  1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1,  1, -1, -1,  1, -1]
    skybox_front = [-1, -1,  1, -1,  1,  1, 1,  1,  1, 1,  1,  1, 1, -1,  1, -1, -1,  1]

    skybox_vertices = np.array([skybox_right, skybox_left, skybox_top, skybox_bottom, skybox_back, skybox_front], dtype=np.float32).flatten()
    skybox_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, skybox_vbo)
    glBufferData(GL_ARRAY_BUFFER, skybox_vertices.nbytes, skybox_vertices, GL_STATIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

def render():
    global program
    global cubemap
    global skybox_vbo
    global viewMatrix_sky

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_TEXTURE_CUBE_MAP)

    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)

    # glLoadIdentity()
    # glMultMatrixf(viewMatrix_sky.getValue())
    viewMatrix_sky.multiple()
    # glMultMatrixf(getattr(viewMatrix_sky,'matrixValue'))
    glUseProgram(program)
    glDepthMask(GL_FALSE)
    glBindTexture(GL_TEXTURE_CUBE_MAP, cubemap)
    glEnableClientState(GL_VERTEX_ARRAY)
    glBindBuffer(GL_ARRAY_BUFFER, skybox_vbo)
    glVertexPointer(3, GL_FLOAT, 0, None)
    glDrawArrays(GL_TRIANGLES, 0, 36)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glDisableClientState(GL_VERTEX_ARRAY)
    glBindTexture(GL_TEXTURE_CUBE_MAP, 0)
    glDepthMask(GL_TRUE)
    glUseProgram(0)

    # viewMatrix_sky = glGetFloatv(GL_MODELVIEW_MATRIX)
    viewMatrix_sky.update()

    glLoadIdentity()
    glDisable(GL_TEXTURE_2D)
    glDisable(GL_TEXTURE_CUBE_MAP)

def load_cubemap():
    tex_id = glGenTextures(1)
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_CUBE_MAP, tex_id)
    for i, face in enumerate(skyBoxFiles_path):
        face_image = Image.open(face)
        face_width, face_height, face_surface = face_image.size[0],face_image.size[1],face_image.tobytes("raw", "RGBX",0,-1)
        glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X + i, 0, 3, face_width, face_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, face_surface)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE)
    glBindTexture(GL_TEXTURE_CUBE_MAP, 0)
    return tex_id

def cross_product_3(a,b):  
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

def cylinder_2p( cylinder, v1, v2, lengthRatio=1,  color=[1.0,1.0,1.0,1.0],base=0.05, top=0.05):
    # glMaterialfv(GL_FRONT, GL_DIFFUSE, [color[0], color[1], color[2], color[3]])
    glEnable(GL_COLOR_MATERIAL)
    glColor4f(color[0], color[1], color[2], color[3])  # Select color
    v2r = np.subtract(v2,v1)
    z = np.array([0.0, 0.0, 1.0])
    # the rotation axis is the cross product between Z and v2r
    ax = np.cross(z, v2r)
    l = np.sqrt(np.dot(v2r, v2r))
    # get the angle using a dot product
    angle = 180.0 / math.pi * np.arccos(np.dot(z, v2r) / l)
    glPushMatrix()
    glTranslatef(v1[0]/lengthRatio, v1[1]/lengthRatio, v1[2]/lengthRatio)
    #print "The cylinder between %s and %s has angle %f and axis %s\n" % (v1, v2, angle, ax)
    glRotatef(angle, ax[0], ax[1], ax[2])
    # glutSolidCylinder(dim / 10.0, l, 20, 20)
    gluCylinder(cylinder, base,top,l/lengthRatio, 32, 16)
    glPopMatrix()
    glDisable(GL_COLOR_MATERIAL)

def drawCylinder(cylinder, v1,v2, base=0.1, top=0.1):
    ''' This function draws a sphere in coordinates (x,y,z) '''
    glPushMatrix()
    z=(0,0,1)
    v2r = v2 - v1
    # the rotation axis is the cross product between Z and v2r
    ax = cross_product_3(z, v2r)
    # get the angle using a dot product
    angle = 180.0 / math.pi * math.acos(np.dot(z, v2r) / l)
    # gluLookAt(x1,y1,z1,x2,y2,z2,1,1,1)  # Move to the place
    glColor4f(1, 1, 1, 1)  # Select color
    length=math.sqrt(math.pow((v1[0]-v2[0]), 2)+math.pow((v1[1]-v2[1]), 2)+math.pow((v1[2]-v2[2]),2))
    gluCylinder(cylinder, base,top,length/lengthRatio, 32, 16)  # Draw sphere

    glPopMatrix()

def drawSphere(sphere, x=0, y=0, z=0, radius=0.1, color=[1.0,1.0,1.0,1.0]):
    ''' This function draws a sphere in coordinates (x,y,z) '''
    glPushMatrix()
    glEnable(GL_COLOR_MATERIAL)
    glTranslatef(x, y, z)  # Move to the place
    glColor4f(color[0], color[1], color[2], color[3])  # Select color
    # glColor4f(abs(x)+0.2, abs(y)+0.2, abs(z)+0.2, 1)  # Select color (dynamic)
    gluSphere(sphere, radius, 32, 16)  # Draw sphere
    glDisable(GL_COLOR_MATERIAL)
    glPopMatrix()

def initView(width=800, height=600):
    pygame.init()
    display = (width, height)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)
    pygame.display.set_caption("CG Projects")

    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    # gluLookAt(0, 0, 15, 0, 0, 0, 1, 1, 90)
    gluLookAt(10, -2, 0, 0, 0, 0, 0, 0, 1)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    light()
    glLoadIdentity()

    return viewMatrix

def getInput(run):
    global viewMatrix_sky, viewMatrix
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run[0] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN or event.key == pygame.K_q:
                run[0] = False

    if run[0]==False:
        pygame.quit()

    keypress = pygame.key.get_pressed()
    # Movement
    if keypress[pygame.K_w] or keypress[pygame.K_UP]:
        glTranslatef(0, 0, -0.1)
    if keypress[pygame.K_s] or keypress[pygame.K_DOWN]:
        glTranslatef(0, 0, 0.1)
    if keypress[pygame.K_d] or keypress[pygame.K_RIGHT]:
        glTranslatef(0.1, 0, 0)
    if keypress[pygame.K_a] or keypress[pygame.K_LEFT]:
        glTranslatef(-0.1, 0, 0)

    if keypress[pygame.K_z]:
        glPushMatrix()
        glLoadIdentity()
        glMultMatrixf(viewMatrix)
        glRotate(3, 1, 0, 0)#spin around x axis
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        glPopMatrix()
        
    if keypress[pygame.K_x]:
        glPushMatrix()
        glLoadIdentity()
        glMultMatrixf(viewMatrix)
        glRotate(3, 0, 1, 0)#spin around y axis
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        glPopMatrix()

    if keypress[pygame.K_c]:
        glPushMatrix()
        glLoadIdentity()
        glMultMatrixf(viewMatrix)
        glRotate(3, 0, 0, 1)#spin around x axis
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        glPopMatrix()

    # movement for skybox
    if keypress[pygame.K_u] :
        # glPushMatrix()
        # glLoadIdentity()
        # glRotate(1, 1, 0, 0)#spin around x axis
        # glMultMatrixf(viewMatrix_sky)
        # viewMatrix_sky = glGetFloatv(GL_MODELVIEW_MATRIX)
        # glPopMatrix()
        viewMatrix_sky.rotate_camera(rotation_sky_xp)
        #this is used for the skeleton
        glRotate(1, 1, 0, 0)

    if keypress[pygame.K_i] :
        # glPushMatrix()
        # glLoadIdentity()
        # glRotate(-1, 1, 0, 0)#spin around x axis
        # glMultMatrixf(viewMatrix_sky)
        # viewMatrix_sky = glGetFloatv(GL_MODELVIEW_MATRIX)
        # glPopMatrix()
        #this is used for the skeleton
        viewMatrix_sky.rotate_camera(rotation_sky_xn)

        glRotate(-1, 1, 0, 0)

    if keypress[pygame.K_j] :
        # glPushMatrix()
        # glLoadIdentity()
        # glRotate(1, 0, 1, 0)#spin around y axis
        # glMultMatrixf(viewMatrix_sky)
        # viewMatrix_sky = glGetFloatv(GL_MODELVIEW_MATRIX)
        # glPopMatrix()
        viewMatrix_sky.rotate_camera(rotation_sky_yp)

        glRotate(1, 0, 1, 0)

    if keypress[pygame.K_k] :
        # glPushMatrix()
        # glLoadIdentity()
        # glRotate(-1, 0, 1, 0)#spin around y axis
        # glMultMatrixf(viewMatrix_sky)
        # viewMatrix_sky = glGetFloatv(GL_MODELVIEW_MATRIX)
        # glPopMatrix()
        viewMatrix_sky.rotate_camera(rotation_sky_yn)

        glRotate(-1, 0, 1, 0)#spin around y axis

    if keypress[pygame.K_n] :
        # glPushMatrix()
        # glLoadIdentity()
        # glRotate(1, 0, 0, 1)#spin around z axis
        # glMultMatrixf(viewMatrix_sky)
        # viewMatrix_sky = glGetFloatv(GL_MODELVIEW_MATRIX)
        # glPopMatrix()
        viewMatrix_sky.rotate_camera(rotation_sky_zp)

        glRotate(1, 0, 0, 1)#spin around z axis

    if keypress[pygame.K_m] :
        # glPushMatrix()
        # glLoadIdentity()
        # glRotate(-1, 0, 0, 1)#spin around y axis
        # glMultMatrixf(viewMatrix_sky)
        # viewMatrix_sky = glGetFloatv(GL_MODELVIEW_MATRIX)
        # glPopMatrix()
        viewMatrix_sky.rotate_camera(rotation_sky_zn)

        glRotate(-1, 0, 0, 1)#spin around y axis

    return run

# coordinate (Draw the coordinate)
def Coord():
    glEnable(GL_COLOR_MATERIAL)
    glBegin(GL_LINES)
    glColor4f(1, 0, 0, 1)  # Select color RED, Z
    glVertex3fv(verticies[0])
    glVertex3fv(verticies[1])
    glEnd()
    glBegin(GL_LINES)
    glColor4f(0, 1, 0, 1)  # Select color Green, Y
    glVertex3fv(verticies[0])
    glVertex3fv(verticies[2])
    glEnd()
    glBegin(GL_LINES)
    glColor4f(0, 0, 1, 1)  # Select color Blue, X
    glVertex3fv(verticies[0])
    glVertex3fv(verticies[3])
    glEnd()
    glDisable(GL_COLOR_MATERIAL)
    glColor4f(1, 0, 0 , 0)  # Select color white
    # glClear(GL_COLOR_BUFFER_BIT)

def printmatrix4(templist):
    """
    docstring
    """
    for x in range(len(templist)):
        if x%4 == 3:
            print (templist[x])
        else:
            print (templist[x],end=' ')
    pass

def drawLightBulb():
    glLoadIdentity()
    glMultMatrixf(viewMatrix_light)
    drawSphere(sphere,lightPos[0],lightPos[1],lightPos[2],0.15,lightBallColor)

viewMatrix = initView(800, 600)
viewMatrix_sky_tmp = initView_sky(800, 600)
viewMatrix_sky = mtx.matrix(viewMatrix_sky_tmp)
viewMatrix_light=viewMatrix
glEnable(GL_LIGHTING)

sphere = gluNewQuadric()  # Create new sphere
cylinder = gluNewQuadric()  # Create new cylinder

lightBallColor=[1.0,1.0,1.0,1.0]
skeletonJointColor=[1.0,1.0,0.0,1.0]
skeletonLineColor=[27/256, 138/256, 179/256, 1]

program=load_shaders("./shaders/skybox.vert", "./shaders/skybox.frag")
cubemap=load_cubemap()
ID=loadImageToTexture()
loadSkybox()

rotation=0
run = [True, 0]
while run:
    idx=0
    while idx < 370:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen
        render()
        drawLightBulb()
        glLoadIdentity()

        s = str(idx)
        nm='animation/'+ s +'.json'
    
        with open(nm) as f:
            skeleton = json.load(f)

        run = getInput(run)

        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        for joint in skeleton:
            drawSphere(
                sphere,
                (joint[0]-skeleton[0][0])/lengthRatio,
                (joint[1]-skeleton[0][1])/lengthRatio,
                (joint[2]-skeleton[0][2])/lengthRatio,
                0.1,
                skeletonJointColor
            )
        
        for line in lineOrder:
            # print(line)
            v1=skeleton[line[0]]
            v2=skeleton[line[1]]
            cylinder_2p(cylinder,v1,v2,lengthRatio, skeletonLineColor)
        
        Coord()

        # environment
        drawCube(ID)
        # nehe_draw()
        draw_ball()  
        # glRotatef(1, 0, 1, 0)
        # rotation=1

        pygame.display.flip()  # Update the screen
        pygame.time.wait(FrameSpeed)

        idx=idx+1

glDeleteBuffers()
pygame.quit()
