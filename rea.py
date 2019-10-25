import bpy

f = open("/Users/marinakrifcun/Documents/blender_tut/chiffres.txt", "r")
f = f.read()
print("f")

divide_by = 10

for n, line in enumerate(f.split("\n")):
    try:
        line = int(line)
        
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(0, n*2, 0))
        bpy.ops.transform.resize(value=(1, 1, line/divide_by), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.translate(value=(0, 0, line/divide_by), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        bpy.ops.transform.translate(value=(-0, -n/2, -0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

    except:
        pass
    
        