"""Runtime package for DAViD pixelwise estimators.

Copyright (c) Microsoft Corporation.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    
try:        
    from .soft_foreground_segmenter import SoftForegroundSegmenter
    from .utils import composite_model_output_to_image, prepare_image_for_model
    from .visualize import visualize_relative_depth_map
except ImportError as e:
    from runtime.soft_foreground_segmenter import SoftForegroundSegmenter
    from runtime.utils import composite_model_output_to_image, prepare_image_for_model
    from runtime.visualize import visualize_relative_depth_map
    __all__ = [
        "visualize_relative_depth_map",
        "SoftForegroundSegmenter",    
    ]

try:
    from .depth_estimator import RelativeDepthEstimator
except ImportError as e:
    print("Failed to import RelativeDepthEstimator:", e)
    
try:
    from .multi_task_estimator import MultiTaskEstimator
except ImportError as e:
    print("Failed to import RelativeDepthEstimator:", e)
    
try:
    from .pixelwise_estimator import PixelwiseEstimator, RuntimeSession, preprocess_img
except ImportError as e:
    print("Failed to import RelativeDepthEstimator:", e)
    
try:
    from .surface_normal_estimator import SurfaceNormalEstimator
except ImportError as e:
    print("Failed to import RelativeDepthEstimator:", e)

# __all__ = [
#     "PixelwiseEstimator",
#     "preprocess_img",
#     "RuntimeSession",
#     "prepare_image_for_model",
#     "composite_model_output_to_image",
#     "ONNX_EP",
#     "ModelNotFoundError",
#     "ModelError",
#     "RelativeDepthEstimator",
#     "visualize_relative_depth_map",
#     "SoftForegroundSegmenter",
#     "SurfaceNormalEstimator",
#     "MultiTaskEstimator",
# ]
