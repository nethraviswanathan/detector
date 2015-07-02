# -*- coding: utf-8 -*-

import cv2
import numpy as np


def resize(img, w, h):
    '''
    Изменение размера изображения с сохранением пропорций
    Изображение "вписывается" в прямоугольник w*h
    
    :param img - изображение (Image)
    :param w - максимальная ширина результирующего изображения
    :param h - максимальная высота результирующего изображения 
    
    :returns <Image>
    '''
    width, height = getsize(img)
    kw = w/width
    kh = h/height
    k = min((kw,kh))
    return cv2.resize(img, (int(width * k),int(height * k)))

def read(imgPath):
    '''
    Чтение изображения из файла
    
    :param imgPath - путь до изображения
    
    :returns <Image>
    '''
    return cv2.imread(imgPath, 0)

def getsize(img):
    '''
    Получение размера изображения
    
    :param img - изображение (Image)
    
    :returns w - максимальная ширина результирующего изображения
    :returns h - максимальная высота результирующего изображения
    '''
    h, w = img.shape[:2]
    return w, h
  
def anorm(self, a):
    '''
    Нормировка вектора
    '''
    return np.sqrt((a*a).sum(-1))
  
  