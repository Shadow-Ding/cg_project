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

import json

FrameSpeed=20
lengthRatio=2
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

def nehe_draw():
    """
    from nehe tutorial
    """
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); # Clear The Screen And The Depth Buffer
    # glLoadIdentity();                   # Reset The View
    # glTranslatef(-1.5f,0.0,-6.0);             # Move Left And Into The Screen
    # glRotatef(rtri,0.0,1.0,0.0);             # Rotate The Pyramid On It's Y Axis
    glBegin(GL_TRIANGLES);                  # Start Drawing The Pyramid
    
    glColor3f(1.0,0.0,0.0)          # Red
    glVertex3f( 0.0/lengthRatio, 1.0/lengthRatio, 0.0/lengthRatio)        # Top Of Triangle (Front)
    glColor3f(0.0,1.0,0.0);          # Green
    glVertex3f(-1.0/lengthRatio,-1.0/lengthRatio, 1.0/lengthRatio);          # Left Of Triangle (Front)
    glColor3f(0.0,0.0,1.0);          # Blue
    glVertex3f( 1.0/lengthRatio,-1.0/lengthRatio, 1.0/lengthRatio);          # Right Of Triangle (Front)

    glColor3f(1.0,0.0,0.0);          # Red
    glVertex3f( 0.0/lengthRatio, 1.0/lengthRatio, 0.0/lengthRatio);          # Top Of Triangle (Right)
    glColor3f(0.0,0.0,1.0);          # Blue
    glVertex3f( 1.0/lengthRatio,-1.0/lengthRatio, 1.0/lengthRatio);          # Left Of Triangle (Right)
    glColor3f(0.0,1.0,0.0);          # Green
    glVertex3f(1.0/lengthRatio,-1.0/lengthRatio, -1.0/lengthRatio);         # Right Of Triangle (Right)

    glColor3f(1.0,0.0,0.0);          # Red
    glVertex3f( 0.0/lengthRatio, 1.0/lengthRatio, 0.0/lengthRatio);          # Top Of Triangle (Back)
    glColor3f(0.0,1.0,0.0);          # Green
    glVertex3f( 1.0/lengthRatio,-1.0/lengthRatio, -1.0/lengthRatio);         # Left Of Triangle (Back)
    glColor3f(0.0,0.0,1.0);          # Blue
    glVertex3f(-1.0/lengthRatio,-1.0/lengthRatio, -1.0/lengthRatio);         # Right Of Triangle (Back)

    glColor3f(1.0,0.0,0.0);          # Red
    glVertex3f( 0.0/lengthRatio, 1.0/lengthRatio, 0.0/lengthRatio);          # Top Of Triangle (Left)
    glColor3f(0.0,0.0,1.0);          # Blue
    glVertex3f(-1.0/lengthRatio,-1.0/lengthRatio,-1.0/lengthRatio);          # Left Of Triangle (Left)
    glColor3f(0.0,1.0,0.0);          # Green
    glVertex3f(-1.0/lengthRatio,-1.0/lengthRatio, 1.0/lengthRatio);          # Right Of Triangle (Left)
    glEnd()

#     glLoadIdentity();
    glPushMatrix()

    glTranslatef(1.5,0.0,-7.0);              # Move Right And Into The Screen
 
# glRotatef(rquad,1.0,1.0,1.0);            # Rotate The Cube On X, Y & Z
 
    glBegin(GL_QUADS);                  # Start Drawing The Cube
    glColor3f(0.0,1.0,0.0);          # Set The Color To Green
    glVertex3f( 1.0, 1.0,-1.0);          # Top Right Of The Quad (Top)
    glVertex3f(-1.0, 1.0,-1.0);          # Top Left Of The Quad (Top)
    glVertex3f(-1.0, 1.0, 1.0);          # Bottom Left Of The Quad (Top)
    glVertex3f( 1.0, 1.0, 1.0);          # Bottom Right Of The Quad (Top)

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



def cross_product_3(a,b):  
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

def temp_drawCylinder():
    ''' This function draws a sphere in coordinates (x,y,z) '''
    glPushMatrix()
    # glRotatef(45,0,0,1)
    glTranslatef(1,0,0)  # Move to the place
    glRotatef(45,0,0,1)
    # glMultMatrixf(viewMatrix)
    glColor4f(1, 1, 1, 1)  # Select color
    
    gluCylinder(cylinder, 0.1,0.1,1, 32, 16)

    glPopMatrix()

def cylinder_2p( cylinder, v1, v2, lengthRatio=1, base=0.05, top=0.05, color=[(1,0,0),(1,0,0),(1,0,0),(1,0,0)]):
    # glMaterialfv(GL_FRONT, GL_DIFFUSE, [color[0], color[1], color[2], color[3]])
    glColor4f(1, 1, 1, 0)  # Select color
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

def drawSphere(sphere, x=0, y=0, z=0, radius=0.1):
    ''' This function draws a sphere in coordinates (x,y,z) '''
    glPushMatrix()

    glTranslatef(x, y, z)  # Move to the place
    glColor4f(0, 1, 0, 1)  # Select color
    # glColor4f(abs(x)+0.2, abs(y)+0.2, abs(z)+0.2, 1)  # Select color (dynamic)
    gluSphere(sphere, radius, 32, 16)  # Draw sphere

    glPopMatrix()

def initView(width=800, height=600):
    pygame.init()
    display = (width, height)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    # gluLookAt(0, 0, 15, 0, 0, 0, 1, 1, 90)
    gluLookAt(10, -2, 0, 0, 0, 0, 1, 1, 0)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()

    return viewMatrix

def getInput(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run[0] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN or event.key == pygame.K_q:
                run[0] = False

    keypress = pygame.key.get_pressed()

    # init model view matrix
    glLoadIdentity()

    # init the view matrix
    glPushMatrix()
    # glLoadIdentity()

    # Movement
    if keypress[pygame.K_w] or keypress[pygame.K_UP]:
        # currentMatrix=glGetInteger(GL_MATRIX_MODE)
        # print(currentMatrix)
        glTranslatef(0, 0, 0.1)
    if keypress[pygame.K_s] or keypress[pygame.K_DOWN]:
        glTranslatef(0, 0, -0.1)
    if keypress[pygame.K_d] or keypress[pygame.K_RIGHT]:
        glTranslatef(-0.1, 0, 0)
    if keypress[pygame.K_a] or keypress[pygame.K_LEFT]:
        glTranslatef(0.1, 0, 0)

    if keypress[pygame.K_z]:
        if run[1]!=0:
            run[1]=0
        else:
            run[1]=1
    if keypress[pygame.K_x]:
        if run[1]!=0:
            run[1]=0
        else:
            run[1]=2
    if keypress[pygame.K_c]:
        if run[1]!=0:
            run[1]=0
        else:
            run[1]=3

    return run

# coordinate (Draw the coordinate)
def Coord():
    glBegin(GL_LINES)
    glColor4f(1, 0, 0, 1)  # Select color: red, X axis
    glVertex3fv(verticies[0])
    glVertex3fv(verticies[1])
    glEnd()
    glBegin(GL_LINES)
    glColor4f(0, 1, 0, 1)  # Select color: green, Y axis
    glVertex3fv(verticies[0])
    glVertex3fv(verticies[2])
    glEnd()
    glBegin(GL_LINES)
    glColor4f(0, 0, 1, 1)  # Select color: blue, Z axis
    glVertex3fv(verticies[0])
    glVertex3fv(verticies[3])
    glEnd()

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

viewMatrix = initView(800, 600)
# initView(800, 600)
sphere = gluNewQuadric()  # Create new sphere
cylinder = gluNewQuadric()  # Create new cylinder

run = [True, 0]
while run:
    
        run = getInput(run)
        if run[0]==False:
            pygame.quit()
            break
        else:
            pass
        
        # a = (GLfloat * 16)()
        # b = (GLfloat * 16)()
        # c = (GLfloat * 16)()

        # glRotatef(2, 0, 0, 1)
        # glGetFloatv(GL_MODELVIEW_MATRIX)
        # glTranslatef(0.01,0,0)
        # multiply the current matrix by the new view matrix and store the final view matrix
        glMultMatrixf(viewMatrix)
        # glGetFloatv(GL_MODELVIEW_MATRIX)
        # printmatrix4(a)
        # printmatrix4(b)
        if run[1]==1:
            glRotatef(2, 1, 0, 0) # rotate model axis X
        else:
            if run[1]==2:
                glRotatef(2, 0, 1, 0) # rotate model axis Y
            else:
                if run[1]==3:
                    glRotatef(2, 0, 0, 1) # rotate model axis Z
                else:
                    pass

        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # printmatrix4(c)

        # apply view matrix
        glPopMatrix()

        glMultMatrixf(viewMatrix)
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen

        nehe_draw()
        
        Coord()
        # drawSphere(sphere, -1.5, 0, 0)
        # drawSphere(sphere, 1.5, 0, 0)

        # glRotatef(1, 0, 1, 0)

        pygame.display.flip()  # Update the screen
        pygame.time.wait(FrameSpeed)

pygame.quit()
