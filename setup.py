# Hunyuan 3D is licensed under the TENCENT HUNYUAN NON-COMMERCIAL LICENSE AGREEMENT
# except for the third-party components listed below.
# Hunyuan 3D does not impose any additional limitations beyond what is outlined
# in the repsective licenses of these third-party components.
# Users must comply with all terms and conditions of original licenses of these third-party
# components and must ensure that the usage of the third party components adheres to
# all relevant laws and regulations.

# For avoidance of doubts, Hunyuan 3D means the large language models and
# their software and algorithms, including trained model weights, parameters (including
# optimizer states), machine-learning model code, inference-enabling code, training-enabling code,
# fine-tuning enabling code and other elements of the foregoing made publicly available
# by Tencent in accordance with TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT.

from setuptools import setup, find_packages

setup(
    name="hy3dgen",
    version="2.0.2",
    url="https://github.com/Tencent/Hunyuan3D-2",
    packages=find_packages(),
    include_package_data=True,
    package_data={"hy3dgen": ["assets/*", "assets/**/*"]},
    install_requires=[
        'gradio',
        "tqdm>=4.66.3",
        'numpy',
        'ninja',
        'diffusers',
        'pybind11',
        'opencv-python',
        'einops',
        "transformers>=4.48.0",
        'omegaconf',
        'trimesh',
        'pymeshlab',
        'pygltflib',
        'xatlas',
        'accelerate',
        'gradio',
        'fastapi',
        'uvicorn',
        'rembg',
        'onnxruntime'
    ]
)
# from setuptools import setup
# from torch.utils.cpp_extension import BuildExtension, CUDAExtension, CppExtension
# import pybind11

# print("this ran")
# ext_modules = [
#     CUDAExtension(
#         name="custom_rasterizer",
#         sources=[
#             "hy3dgen/texgen/custom_rasterizer/lib/custom_rasterizer_kernel/rasterizer.cpp",
#             "hy3dgen/texgen/custom_rasterizer/lib/custom_rasterizer_kernel/grid_neighbor.cpp",
#             "hy3dgen/texgen/custom_rasterizer/lib/custom_rasterizer_kernel/rasterizer_gpu.cu"
#         ],
#     ),
#     CppExtension(
#         name="mesh_processor",
#         sources=["hy3dgen/texgen/differentiable_renderer/mesh_processor.cpp"],
#         include_dirs=[pybind11.get_include(), pybind11.get_include(user=True)],
#         extra_compile_args={
#             "cxx": ["-O3", "-std=c++14", "-fPIC", "-Wall", "-Wextra"]
#         },
#         extra_link_args=["-fPIC"]
#     )
# ]

# setup(
#     cmdclass={"build_ext": BuildExtension},
#     ext_modules=ext_modules,