# Albumentations (NRTK Fork)

[![CI](https://github.com/Kitware/nrtk-albumentations/workflows/CI/badge.svg)](https://github.com/Kitware/nrtk-albumentations/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

This is a fork of [Albumentations](https://github.com/albumentations-team/albumentations) maintained by Kitware in direct support of [NRTK (Natural Robustness Toolkit)](https://github.com/Kitware/nrtk).

**Fork Information:**

- Last upstream version: Albumentations v2.0.8
- Forked: October 2025

## About

Albumentations is a Python library for fast and flexible image augmentation. This fork is maintained specifically for integration with NRTK and includes modifications to support NRTK's natural robustness evaluation workflows.

Image augmentation is used in deep learning and computer vision tasks to increase the quality of trained models by creating new training samples from existing data through various transformations.

## Key Features

- **Complete Computer Vision Support**: Works with all major CV tasks including classification, segmentation (semantic & instance), object detection, and pose estimation
- **Simple, Unified API**: One consistent interface for all data types - RGB/grayscale/multispectral images, masks, bounding boxes, and keypoints
- **Rich Augmentation Library**: 70+ high-quality augmentations to enhance your training data
- **Fast**: Optimized for production use with consistently high performance
- **Deep Learning Integration**: Works with PyTorch, TensorFlow, and other frameworks
- **3D Support**: Volumetric data transformations for medical imaging and other 3D applications

## Installation

This package is designed to be installed as a dependency of NRTK. For standalone installation, use:

```bash
pip install nrtk-albumentations
```

## A Simple Example

This package is intended for use with NRTK's [AlbumentationPerturber](https://nrtk.readthedocs.io/en/latest/_implementations/nrtk.impls.perturb_image.generic.albumentations_perturber.AlbumentationsPerturber.html#albumentationsperturber). For direct usage:

```python
import albumentations as A
import cv2

# Declare an augmentation pipeline
transform = A.Compose([
    A.RandomCrop(width=256, height=256),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
])

# Read an image with OpenCV and convert it to the RGB colorspace
image = cv2.imread("image.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Augment an image
transformed = transform(image=image)
transformed_image = transformed["image"]
```

## Documentation

For detailed documentation on available transforms and usage patterns, see:

- [Albumentations (NRTK Fork) Documentation](https://nrtk-albumentations.readthedocs.io/)
- [NRTK Documentation](https://nrtk.readthedocs.io/)

## Available Transformations

Albumentations provides 70+ transforms across several categories:

### Pixel-level Transforms

Transforms that modify pixel values without changing image geometry (masks, bboxes, keypoints remain unchanged):

- Color adjustments: `RandomBrightnessContrast`, `HueSaturationValue`, `ColorJitter`
- Noise addition: `GaussNoise`, `ISONoise`, `MultiplicativeNoise`
- Blur effects: `GaussianBlur`, `MotionBlur`, `MedianBlur`, `Defocus`
- Compression: `ImageCompression`
- And many more...

### Spatial-level Transforms

Transforms that modify image geometry (automatically applied to masks, bboxes, keypoints):

- Cropping: `RandomCrop`, `CenterCrop`, `RandomResizedCrop`
- Flipping: `HorizontalFlip`, `VerticalFlip`
- Rotation: `Rotate`, `RandomRotate90`, `SafeRotate`
- Resizing: `Resize`, `LongestMaxSize`, `SmallestMaxSize`
- Distortions: `ElasticTransform`, `GridDistortion`, `OpticalDistortion`
- And many more...

### 3D Transforms

Transforms for volumetric data (medical imaging, etc.):

- `RandomCrop3D`, `CenterCrop3D`
- `Pad3D`, `PadIfNeeded3D`
- `CoarseDropout3D`
- `CubicSymmetry`

For a complete list with detailed parameters, see the [transform reference](https://nrtk-albumentations.readthedocs.io/).

## Maintainer

**Kitware, Inc.** <nrtk@kitware.com>

## Original Authors

This library was originally created by:

- Vladimir I. Iglovikov
- Alexander Buslaev
- Alex Parinov
- Eugene Khvedchenya
- Mikhail Druzhinin

## Contributing

This fork is maintained specifically for NRTK integration. We are not accepting general contributions at this time. For issues or questions related to NRTK integration, please open an issue on the [NRTK repository](https://github.com/Kitware/nrtk/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this library in your research, please consider citing the original Albumentations paper:

```bibtex
@Article{info11020125,
    AUTHOR = {Buslaev, Alexander and Iglovikov, Vladimir I. and Khvedchenya, Eugene and Parinov, Alex and Druzhinin, Mikhail and Kalinin, Alexandr A.},
    TITLE = {Albumentations: Fast and Flexible Image Augmentations},
    JOURNAL = {Information},
    VOLUME = {11},
    YEAR = {2020},
    NUMBER = {2},
    ARTICLE-NUMBER = {125},
    URL = {https://www.mdpi.com/2078-2489/11/2/125},
    ISSN = {2078-2489},
    DOI = {10.3390/info11020125}
}
```
