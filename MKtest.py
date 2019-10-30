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
            size=1,
            enter_editmode=False,
            location=(0, 0, 0))
        bpy.ops.transform.resize(
            value=(w, 1, 1),
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

        col = bpy.context.object #Set active object to variable
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].width = 0.03
        bpy.context.object.modifiers["Bevel"].segments = 3
        orange_material = bpy.data.materials.new(name="Orange") #set new material to variable
        col.data.materials.append(orange_material) #add the material to the object
        bpy.context.object.active_material.diffuse_color = (0.8, 0.03, 0.005, 1) #change color
        bpy.context.object.active_material.metallic = 0.9
        bpy.context.object.active_material.roughness = 0.1

        # get the nodes
        # nodes = orange_material.node_tree.nodes
        # bpy.data.materials["Orange"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.0289448, 0.00477547, 1)
        # bpy.data.materials["Orange"].node_tree.nodes["Principled BSDF"].inputs[3].default_value = (0.8, 0.368263, 0.0024313, 1)
        # bpy.data.materials["Orange"].node_tree.nodes["Principled BSDF"].inputs[7].default_value = 0.062212
        # bpy.data.materials["Orange"].node_tree.nodes["Principled BSDF"].inputs[1].default_value = 0.0599078
        #
        # bpy.context.object.lock_scale[0] = True
        # bpy.context.object.lock_scale[1] = True
        #

        # to animate scaling
        # import mathutils

        # selected_scale = [mathutils.Vector((w, 1, z)) for z in range(z)]
        # selected_location = [mathutils.Vector((x, 0, z/2)) for z in range(z)]

        frame_num = 0
        if z>0:
            for z in range(z):
                bpy.context.scene.frame_set(frame_num)
                col.scale = (w, 1, z)
                col.keyframe_insert(data_path = 'scale')
                col.location = (x, 0, z/2)
                col.keyframe_insert(data_path = 'location')

                frame_num += 2
        else:
            for z in range(0, z, -1):
                bpy.context.scene.frame_set(frame_num)
                col.scale = (w, 1, z)
                col.keyframe_insert(data_path = 'scale')
                col.location = (x, 0, z/2)
                col.keyframe_insert(data_path = 'location')

                frame_num += 2

        # for i, scale in enumerate(selected_scale):
        #     bpy.context.scene.frame_set(frame_num)
        #     col.scale = scale
        #     col.keyframe_insert(data_path = 'scale')
        #     col.location = scale
        #     col.keyframe_insert(data_path = 'location')
        #
        #     frame_num += 2


        # bpy.ops.object.transform_apply(
        #     location = True,
        #     scale = False,
        #     rotation = False)
        # col.location.x = x


        """

        # bpy.context.scene.active = bpy.data.scenes["Scene"].(null)
        bpy.ops.anim.keyframe_insert()
        bpy.ops.transform.resize(
            value=(1, 1, z),
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
            value=(0, 0, z/2),
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
        bpy.ops.anim.keyframe_insert()


    def grow_columns(self, x, z, w):

        # to animate scaling
        import mathutils

        selected_scale = [mathutils.Vector((0, 0, z)) for z in range(z)]
        print(selected_scale)
        # growing_object = bpy.data.objects['Cube']
        growing_object = bpy.context.active_object

        frame_num = 0
        for i, scale in enumerate(selected_scale):
            bpy.context.scene.frame_set(frame_num)
            # bpy.data.scenes["Scene"].frame_set(i * 4 + 1)
            growing_object.scale = scale
            # f = bpy.context.object.animation_data.action.fcurves.find('scale', index=1)
            # growing_object.animation_data.action.fcurves.find('scale', index=1)
            # growing_object.location = loc
            # growing_object.keyframe_insert(data_path = 'location')
            # if growing_object.rotation_mode == "QUATERNION":
                # growing_object.keyframe_insert(data_path = 'rotation_quaternion')
            # else:
                # growing_object.keyframe_insert(data_path = 'rotation_euler')
            growing_object.keyframe_insert(data_path = 'scale', index=-1)

            frame_num += 2
        """

    def confetti(self, number):
        import mathutils

        positions = [mathutils.Vector((0.4*i, 0.2*i, 30+5*i)) for i in range(number)]
        # positions = (0,0,2),(0,1,2),(3,2,1),(3,4,1),(1,2,1)
        start_pos = (0,0,0)

        bpy.ops.mesh.primitive_uv_sphere_add(segments=32, radius=0.15, location=start_pos)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.active_object

        # glowing_material = bpy.data.materials.new(name="Glowing") #set new material to variable
        # ob.data.materials.append(glowing_material) #add the material to the object
        # obj_mat = bpy.context.object.active_material
        # obj_mat.diffuse_color = (1, 1, 1, 1) #change color
        # obj_mat.metallic = 0.9
        # obj_mat.roughness = 0.1
        # # obj_mat.emit = 100
        # bpy.data.materials['Glowing'].use_nodes = True
        # bpy.data.materials['Glowing'].node_tree.nodes["Emission"].inputs[1].default_value = 3
        # get the nodes
        # nodes = glowing_material.node_tree.nodes
        # nodes["Principled BSDF"].inputs[17].default_value = (0.999956, 0.999956, 0.999956, 1)
        mat_n = "Glow1"
        bpy.data.materials.new(mat_n)
        bpy.data.materials[mat_n].use_nodes = True

        bpy.data.materials[mat_n].node_tree.nodes["Principled BSDF"].inputs[0].default_value =(1, 1, 1, 1)
        # bpy.data.materials[mat_n].node_tree.nodes["Emission"].inputs[1].default_value = 3

        in_1 = bpy.data.materials[mat_n].node_tree.nodes["Material Output"].inputs["Surface"]
        out_1 = bpy.data.materials[mat_n].node_tree.nodes["Principled BSDF"].outputs["BSDF"]

        bpy.data.materials[mat_n].node_tree.links.new(in_1,out_1)

        bpy.data.objects["Sphere"].active_material = bpy.data.materials[mat_n]

        frame_num = 110 + 2*number

        for position in positions:
            bpy.context.scene.frame_set(frame_num)
            ob.location = position
            ob.keyframe_insert(data_path="location", index=-1)
            frame_num += 2

        # bpy.context.space_data.context = 'PARTICLES'
        # bpy.ops.object.particle_system_add()
        # bpy.data.particles["ParticleSettings"].count = 100
        # bpy.context.scene.objects.active = bpy.data.objects[edge_name]
        # object = bpy.data.objects['Sphere']
        # object.type = "HALO"
        ob.modifiers.new(name='particles',type='PARTICLE_SYSTEM')
        # object.particle_systems[0].count = 100

        # ob = bpy.context.active_object
        # bars = 1
        startframe = 128
        endframe = 131
        # c = 1

        pss = ob.particle_systems.active.settings

        pss.count = 500
        pss.frame_start = startframe
        pss.frame_end = endframe
        pss.normal_factor = 6
        pss.factor_random = 5
        pss.lifetime_random = 1
        pss.material = 1
        pss.particle_size = 30


        pss.keyframe_insert("lifetime", frame=128)
        pss.lifetime = 20
        pss.keyframe_insert("lifetime", frame=250)
        # pss.show_instancer_for_render = False
        # pss.show_instancer_for_viewport = False


        # Changes the first key interpolation from bezier to linear.
        # pss_fcurves = pss.animation_data.action.fcurves
        #
        # for curve in pss_fcurves:
        #     if curve.data_path == "lifetime":
        #         break;
        #
        # curve.keyframe_points[0].interpolation = "LINEAR"

        # c += 1
        # bpy.data.objects.remove(ob)

        # ob.location = start_pos
        # ob.keyframe_insert(data_path="location", index=-1)


    def add_chart(self):
        number_kids = len(self.kids)
        hist_width = 8
        col_width = hist_width / (number_kids)
        for i in range(number_kids):
            # x = -4 + 8 / (ns-1) * i
            x = -hist_width/2 + i*col_width
            pelm_col_height = self.kids[i].pelm
            comp_col_height = self.kids[i].comp
            self.add_column(x, -comp_col_height, col_width)
            # self.add_column(x, -1, col_width)
            self.add_column(x, pelm_col_height, col_width)

            # self.grow_columns(x, -comp_col_height, col_width)
            # self.add_column(x, -1, col_width)
            # self.grow_columns(x, pelm_col_height, col_width)

        for i in range(number_kids+7):
            self.confetti(i)



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
