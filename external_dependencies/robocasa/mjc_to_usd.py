import mujoco
from mujoco.usd import exporter
import os

# 1. Path Setup
xml_path = '/home/zijun/zxp/Isaac-GR00T-N1.5/external_dependencies/robocasa/robocasa/models/assets/objects/objaverse/cup/cup_4/model.xml'
output_path = '/home/zijun/zxp/Isaac-GR00T-N1.5/external_dependencies/robocasa/robocasa/models/assets/objects/usd_ver/cup/cup.usd'

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# 2. Load Model
model = mujoco.MjModel.from_xml_path(xml_path)
data = mujoco.MjData(model)

# 3. Initialize Exporter
usd_exporter = exporter.USDExporter(model)

# 4. Step & Export
mujoco.mj_forward(model, data)
usd_exporter.update_scene(data)

# 5. Save via the Stage attribute
# The .stage is a pxr.Usd.Stage object
usd_exporter.stage.Export(output_path)

print(f"✅ Success! USD exported to: {output_path}")