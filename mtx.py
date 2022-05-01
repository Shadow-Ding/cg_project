from OpenGL.GL import *

class matrix():
    def __init__(self, matrixvalue):
        self.matrixValue = matrixvalue

    def rotate_camera(self, rotate_para=[1, 1, 0, 0]):
       """
       docstring
       """
       glPushMatrix()
       glLoadIdentity()
       glRotate(rotate_para[0], rotate_para[1],
                rotate_para[2], rotate_para[3])  # spin around x axis
       glMultMatrixf(self.matrixValue)
       self.matrixValue = glGetFloatv(GL_MODELVIEW_MATRIX)
       glPopMatrix()
       pass

    def rotate_model(self, rotate_para=[1, 1, 0, 0]):
       """
       docstring
       """
       glPushMatrix()
       glLoadIdentity()
       glMultMatrixf(self.matrixValue)
       glRotate(rotate_para[0], rotate_para[1],
                rotate_para[2], rotate_para[3])  # spin around x axis
       self.matrixValue = glGetFloatv(GL_MODELVIEW_MATRIX)
       glPopMatrix()
       pass

    def translate_camera(self, translate_para=[1, 1, 0, 0]):
       """
       docstring
       """
       glPushMatrix()
       glLoadIdentity()
       glTranslatef(translate_para[0], translate_para[1],
                    translate_para[2], translate_para[3])  # spin around x axis
       glMultMatrixf(self.matrixValue)
       self.matrixValue = glGetFloatv(GL_MODELVIEW_MATRIX)
       glPopMatrix()
       pass

    def translate_model(self, translate_para=[1, 1, 0, 0]):
       """
       docstring
       """
       glPushMatrix()
       glLoadIdentity()
       glMultMatrixf(self.matrixValue)
       glTranslatef(translate_para[0], translate_para[1],
                    translate_para[2], translate_para[3])  # spin around x axis
       self.matrixValue = glGetFloatv(GL_MODELVIEW_MATRIX)
       glPopMatrix()
       pass

    def multiple(self):
        glLoadIdentity()
        glMultMatrixf(self.matrixValue)
        pass

    def update(self):
        self.matrixValue = glGetFloatv(GL_MODELVIEW_MATRIX)
        pass
