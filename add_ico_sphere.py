def add_ico_sphere(location=(0, 0, 0),
                   name='Ico_Sphere',
                   subdivisions=3):
    # Add ico sphere
    bpy.ops.mesh.primitive_ico_sphere_add(
        location=location,
        subdivisions=subdivisions)
    # Set names
    bpy.context.object.name = name
    bpy.context.object.data.name = name
    # Return object
    return bpy.context.object

#За добавление сферы с нужными мне параметрами отвечает вот такая функция:
#bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3, enter_editmode=False, location=(0, 0, 0))

#А я хочу писать в коде так:
add_ico_sphere()

ball = add_ico_sphere(location=(1, 0, 0))

sphere = add_ico_sphere(name='My_Sphere')



def add_cube(location=(0, 0, 0),
                   name='Cube'):
    # Add cube
    bpy.ops.mesh.primitive_cube_add(
        location=location)
    # Set names
    bpy.context.object.name = name
    bpy.context.object.data.name = name
    # Return object
    return bpy.context.object

def add_plane(location=(0, 0, 0),
                   name='Plane'):
    # Add plane
    bpy.ops.mesh.primitive_plane_add(
        location=location)
    # Set names
    bpy.context.object.name = name
    bpy.context.object.data.name = name
    # Return object
    return bpy.context.object

def add_cylinder(location=(0, 0, 0),
                   name='Cylinder',
                   vertices=32,
                   end_fill_name='NGON'):
    # Add cylinder
    bpy.ops.mesh.primitive_cylinder_add(
        location=location,
        vertices=vertices,
        end_fill_name=end_fill_name)
    # Set names
    bpy.context.object.name = name
    bpy.context.object.data.name = name
    # Return object
    return bpy.context.object

def add_cone(location=(0, 0, 0),
                   name='Cone',
                   vertices=32,
                   end_fill_name='NGON'):
    # Add cone
    bpy.ops.mesh.primitive_cone_add(
        location=location,
        vertices=vertices,
        end_fill_name=end_fill_name)
    # Set names
    bpy.context.object.name = name
    bpy.context.object.data.name = name
    # Return object
    return bpy.context.object
