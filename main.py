from gl import *
from shaders import *
from obj import *


r = Render(1300, 1077)
r.light = V3(0, 1, 1)

#Fondo
print('Creando fondo')
t = Texture('./textures/ciudad.bmp')
r.buffer = t.pixels
r.active_texture = t
r.active_shader = shadow
r.lookAt(V3(1, 0, 100), V3(0, 0, 0), V3(0, 1, 0))
r.finish('scene.bmp')
print('Fondo creado')

#Carro
print('Añadiendo carro')
t = Texture('./textures/camaro.bmp')
r.active_texture = t
r.active_shader = shadow
r.lookAt(V3(1, 0, 3), V3(0, 0, 0), V3(0, 1, 0))
r.load('./models/camaro.obj', translate=(-0.45, -0.95, 0), scale=(0.1,0.1,0.1), rotate=(0, -1, 0))
r.draw_arrays('TRIANGLES')
r.finish('scene.bmp')

#Ovni
print('Añadiendo ovni')
t = Texture('./textures/binary.bmp')
r.active_texture = t
r.active_shader = shadow
r.lookAt(V3(1, 0, 3), V3(0, 0, 0), V3(0, 1, 0))
r.load('./models/alien.obj', translate=(0, 0.7, 0), scale=(0.07,0.07,0.07), rotate=(0, 0, 0))
r.draw_arrays('TRIANGLES')
r.finish('scene.bmp')

#Gato
print('Añadiendo gato')
t = Texture('./textures/cat.bmp')
r.active_texture = t
r.active_shader = shadow
r.lookAt(V3(1, 0, 3), V3(0, 0, 0), V3(0, 1, 0))
r.load('./models/gato.obj', translate=(-1, -0.3, 0), scale=(0.2,0.2,0.2), rotate=(0, 0.9, 0))
r.draw_arrays('TRIANGLES')
r.finish('scene.bmp')

#Avion
print('Añadiendo avion')
t = Texture('./textures/Albedo.bmp')
r.active_texture = t
r.active_shader = simple
r.lookAt(V3(1, 0, 3), V3(0, 0, 0), V3(0, 1, 0))
r.load('./models/F-104.obj', translate=(-0.7, 0.7, 0), scale=(0.03,0.03,0.03), rotate=(0, 0.9, 0))
r.draw_arrays('TRIANGLES')
r.finish('scene.bmp')

#Spiderman
print('Añadiendo Spiderman')
t = Texture('./textures/spiderman.bmp')
r.active_texture = t
r.active_shader = simple
r.lookAt(V3(1, 0, 5), V3(0, 0, 0), V3(0, 1, 0))
r.load('./models/spiderman-scene.obj', translate=(0.2, 0.3, 0), scale=(0.15,0.15,0.15), rotate=(0, 0.5, 0))
r.draw_arrays('TRIANGLES')
r.finish('scene.bmp')

print('Escena terminada')
