import bpy
import math
import os
from mathutils import Vector

# Reset scene
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

# Render configuration
scene = bpy.context.scene
scene.render.engine = "BLENDER_EEVEE"
scene.render.resolution_x = 1024
scene.render.resolution_y = 1024
scene.render.resolution_percentage = 100

# Materials def
def create_material(name, color, metallic=0.0, roughness=0.35, emission=0.0):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = (*color, 1)
        bsdf.inputs["Metallic"].default_value = metallic
        bsdf.inputs["Roughness"].default_value = roughness
        if emission > 0:
            emission_node = mat.node_tree.nodes.get("Emission")
            if emission_node:
                emission_node.inputs["Color"].default_value = (*color, 1)
                emission_node.inputs["Strength"].default_value = emission
    return mat

pearl = create_material(
    "MICHO Pearl",
    (0.78, 0.84, 0.95),
    0.28, 0.24
)

blue = create_material(
    "MICHO Electric Blue",
    (0.10, 0.45, 1.0),
    0.35, 0.2, 0.7
)

violet = create_material(
    "MICHO Violet",
    (0.42, 0.16, 0.95),
    0.3, 0.22, 0.5
)

dark = create_material(
    "MICHO Dark Face",
    (0.025, 0.035, 0.065),
    0.15, 0.18
)

eye_material = create_material(
    "MICHO Eyes",
    (0.35, 0.85, 1.0),
    0.15, 0.15, 1.5
)

# Smooth object helper
def smooth(obj, material):
    obj.data.materials.append(material)
    if obj.type == "MESH":
        for poly in obj.data.polygons:
            poly.use_smooth = True
    return obj

# Sphere helper
def make_sphere(name, location, scale, material):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=32, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return smooth(obj, material)

# Main head
head = make_sphere("MICHO_Head", (0, 0, 1.65), (0.85, 0.72, 0.95), pearl)

# Face panel
face = make_sphere("MICHO_Face", (0, -0.61, 1.65), (0.64, 0.19, 0.65), dark)

# Eyes
left_eye = make_sphere("MICHO_LeftEye", (-0.25, -0.78, 1.78), (0.105, 0.045, 0.15), eye_material)
right_eye = make_sphere("MICHO_RightEye", (0.25, -0.78, 1.78), (0.105, 0.045, 0.15), eye_material)

# Small central forehead accent
forehead = make_sphere("MICHO_ForeheadAccent", (0, -0.66, 2.23), (0.12, 0.06, 0.12), blue)

# Neck
neck = make_sphere("MICHO_Neck", (0, 0, 0.75), (0.28, 0.28, 0.38), violet)

# Body
body = make_sphere("MICHO_Body", (0, 0, 0.15), (0.68, 0.48, 0.85), pearl)

# Decorative chest accent
chest = make_sphere("MICHO_ChestCore", (0, -0.43, 0.35), (0.22, 0.08, 0.22), blue)

# Create a light
def add_area_light(name, location, energy, color, size):
    bpy.ops.object.light_add(type="AREA", location=location)
    light = bpy.context.object
    light.name = name
    light.data.energy = energy
    light.data.color = color
    light.data.shape = "DISK"
    light.data.size = size
    light.rotation_euler = (math.radians(25), 0, math.radians(20))

add_area_light("MICHO_KeyLight", (3, -4, 5), 450, (0.55, 0.75, 1.0), 4)
add_area_light("MICHO_FillLight", (-3, -2, 2), 250, (0.5, 0.3, 1.0), 3)

# Camera
bpy.ops.object.camera_add(location=(3, -7, 2.5))
camera = bpy.context.object
camera.name = "MICHO_Camera"

direction = Vector((0, 0, 1)) - camera.location
camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
scene.camera = camera
camera.data.lens = 55

# World lighting
scene.world.color = (0.12, 0.12, 0.12)

# Animation: subtle floating idle
scene.frame_start = 1
scene.frame_end = 60
for frame in (1, 30, 60):
    head.location.z = 1.65 if frame == 1 else (1.60 if frame == 30 else 1.70)
    head.keyframe_insert(data_path="location", frame=frame)

# Save Blender project
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
avatar_dir = os.path.join(project_root, "assets", "avatar")
os.makedirs(avatar_dir, exist_ok=True)
blend_path = os.path.join(avatar_dir, "micho_master.blend")
bpy.ops.wm.save_as_mainfile(filepath=blend_path)

# Export GLB
glb_path = os.path.join(avatar_dir, "micho_avatar.glb")
bpy.ops.object.select_all(action="SELECT")
bpy.ops.export_scene.gltf(filepath=glb_path, export_format="GLB", use_selection=True)

print("MICHO avatar generated:", glb_path)
