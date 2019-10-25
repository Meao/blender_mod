import bpy

class Kid:
    def __init__(self, name, pelm, comp):
        self.name = name
        self.pelm = int(pelm)
        self.comp = int(comp)

def get_score(kid):
    return kid.pelm+kid.comp*4

# class Column:
#     def __init__(self, kid):
#         self.kid = kid
#         self.width = 2
#     def add_cubes(self):
#         self.add_cube()
#     def add_cube(self, x, z):
#         bpy.ops.mesh.primitive_cube_add(location=(0, 0, z))
#         col = bpy.context.object
#         bpy.ops.object.transform_apply(location = True, scale = False, rotation = False)
#         col.location.x = x

class Hist:
    def __init__(self, kids):
        self.kids = kids
        self.add_chart()
        self.cols = []
    def add_column(self, x, z, w):
        bpy.ops.mesh.primitive_cube_add(
            size=2,
            enter_editmode=False,
            location=(0, 0, 0))
        bpy.ops.transform.resize(
            value=(w, 1, z),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(False, False, True),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff='SMOOTH',
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False)
        bpy.ops.transform.translate(
            value=(0, 0, z),
            orient_type='GLOBAL',
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type='GLOBAL',
            constraint_axis=(False, False, True),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff='SMOOTH',
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False)

        col = bpy.context.object
        bpy.ops.object.transform_apply(
            location = True,
            scale = False,
            rotation = False)
        col.location.x = x
    def add_chart(self):
        ns = len(self.kids)
        col_width = 8 / (ns-1)
        for i in range(ns):
            # x = -4 + 8 / (ns-1) * i
            x = -ns*col_width/2 + i*col_width
            pelm_col_height = self.kids[i].pelm
            comp_col_height = self.kids[i].comp
            self.add_column(x, -pelm_col_height, col_width)
            # self.add_column(x, -1, col_width)
            self.add_column(x, comp_col_height, col_width)



path_data = '/Users/marinakrifcun/Documents/blender_tut/analys1.csv'

def main():
    for mesh in bpy.data.meshes:
        bpy.data.meshes.remove(mesh)
    file = open(path_data, 'r', encoding='utf-8')
    file.readline()

    kids = []

    for line in file:
        line = line[:-1].split(',')

        kids.append(Kid(line[0], line[1], line[2]))

    kids.sort(key=get_score)

    histogramm = Hist(kids)
