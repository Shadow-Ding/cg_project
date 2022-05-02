# Install requirements:
# pip install pyopengl
# pip install pygame
# pip install Pillow
# pip install numpy

import math
import numpy as np
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
rotation_skeleton_x=[3, 1, 0, 0]
rotation_skeleton_y=[3, 0, 1, 0]
rotation_skeleton_z=[3, 0, 0, 1]
translation_skeleton_zp=[0,0,0.1]
translation_skeleton_zn=[0,0,-0.1]
translation_skeleton_yp=[0,0.1,0]
translation_skeleton_yn=[0,-0.1,0]
translation_skeleton_xp=[0.1,0,0]
translation_skeleton_xn=[-0.1,0,0]

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

    viewMatrix_sky.apply()
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

def cylinder_2p( cylinder, v1, v2, lengthRatio=1,  color=[1.0,1.0,1.0,1.0],base=0.05, top=0.05):
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
    gluCylinder(cylinder, base,top,l/lengthRatio, 32, 16)
    glPopMatrix()
    glDisable(GL_COLOR_MATERIAL)

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
        viewMatrix_skeleton.translate_camera(translation_skeleton_zp)
        viewMatrix_objects.translate_camera(translation_skeleton_zp)
    if keypress[pygame.K_s] or keypress[pygame.K_DOWN]:
        viewMatrix_skeleton.translate_camera(translation_skeleton_zn)
        viewMatrix_objects.translate_camera(translation_skeleton_zn)
    if keypress[pygame.K_d] or keypress[pygame.K_RIGHT]:
        viewMatrix_skeleton.translate_camera(translation_skeleton_xn)
        viewMatrix_objects.translate_camera(translation_skeleton_xn)
    if keypress[pygame.K_a] or keypress[pygame.K_LEFT]:
        viewMatrix_skeleton.translate_camera(translation_skeleton_xp)
        viewMatrix_objects.translate_camera(translation_skeleton_xp)

    if keypress[pygame.K_z]:
        viewMatrix_skeleton.rotate_model(rotation_skeleton_x)
        
    if keypress[pygame.K_x]:
        viewMatrix_skeleton.rotate_model(rotation_skeleton_y)

    if keypress[pygame.K_c]:
        viewMatrix_skeleton.rotate_model(rotation_skeleton_z)

    # movement for skybox
    if keypress[pygame.K_u] :
        viewMatrix_sky.rotate_camera(rotation_sky_xp)
        viewMatrix_skeleton.rotate_camera(rotation_sky_xp)
        viewMatrix_objects.rotate_camera(rotation_sky_xp)

    if keypress[pygame.K_i] :
        viewMatrix_sky.rotate_camera(rotation_sky_xn)
        viewMatrix_skeleton.rotate_camera(rotation_sky_xn)
        viewMatrix_objects.rotate_camera(rotation_sky_xn)

    if keypress[pygame.K_j] :
        viewMatrix_sky.rotate_camera(rotation_sky_yp)
        viewMatrix_skeleton.rotate_camera(rotation_sky_yp)
        viewMatrix_objects.rotate_camera(rotation_sky_yp)

    if keypress[pygame.K_k] :
        viewMatrix_sky.rotate_camera(rotation_sky_yn)
        viewMatrix_skeleton.rotate_camera(rotation_sky_yn)
        viewMatrix_objects.rotate_camera(rotation_sky_yn)

    if keypress[pygame.K_n] :
        viewMatrix_sky.rotate_camera(rotation_sky_zp)
        viewMatrix_skeleton.rotate_camera(rotation_sky_zp)
        viewMatrix_objects.rotate_camera(rotation_sky_zp)

    if keypress[pygame.K_m] :
        viewMatrix_sky.rotate_camera(rotation_sky_zn)
        viewMatrix_skeleton.rotate_camera(rotation_sky_zn)
        viewMatrix_objects.rotate_camera(rotation_sky_zn)

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

def drawLightBulb():
    viewMatrix_light.apply()
    drawSphere(sphere,lightPos[0],lightPos[1],lightPos[2],0.15,lightBallColor)

viewMatrix = initView(800, 600)
viewMatrix_light=mtx.matrix(viewMatrix)
viewMatrix_skeleton=mtx.matrix(viewMatrix)
viewMatrix_objects=mtx.matrix(viewMatrix)
viewMatrix_sky = mtx.matrix(initView_sky(800, 600))
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
    while idx < 371:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen
        render()
        drawLightBulb()
        glLoadIdentity()

        s = str(idx)
        nm='animation/'+ s +'.json'
    
        with open(nm) as f:
            skeleton = json.load(f)

        run = getInput(run)

        viewMatrix_skeleton.apply()
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
        viewMatrix_objects.apply()
        drawCube(ID)
        draw_ball()  

        pygame.display.flip()  # Update the screen
        pygame.time.wait(FrameSpeed)

        idx+=1

glDeleteBuffers()
pygame.quit()
