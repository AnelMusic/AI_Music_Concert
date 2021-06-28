

# AI_Music_Concert

# Camvid_Semantic_Segmentatation_TF2
[![Ubuntu](https://github.com/ptheywood/cuda-cmake-github-actions/workflows/Ubuntu/badge.svg)](https://github.com/ptheywood/cuda-cmake-github-actions/actions?query=workflow%3AUbuntu)
[![Travis](https://img.shields.io/badge/language-Python-red.svg)]()
[![Travis](https://badges.aleen42.com/src/tensorflow.svg)]()
![coverage](https://img.shields.io/badge/coverage-100%25-green)

> This project was created more or less out of boredom on a Sunday afternoon. The goal is to read a video stream or play a recorded video thereby classifying the movements of the user and play a corresponding piece of music according to the recognized musical instrument (guitar, piano, violin). 
The training data was generated with the help of a smartphone. For the classification I use a pre-trained CNN backbone (MobileNetV2). At the next possible time I will provide a detailed instruction on how to train the model with own data. In the checkpoints you will find the weights for a model that achieves about 99% accuracy on the training and validation data set.

Note: The model was not finetuned. After fine tuning even better results should be expected.

![](segmentation_overlay.gif)

## Prerequisite
The code was tested on:

| OS        | Tensorflow           | Cuda Version  | Cuda Compilation Tools| Cudnn|
| ------------- |:-------------:|:-------------:|:-------------:|-----:|
| Ubuntu 18.04      | 2.5 | 11.2 | release 9.1, V9.1.85|  8.1.0|

### Sample Demo (Please turn on your volume)

https://user-images.githubusercontent.com/32487291/123714256-4167e300-d876-11eb-8ff1-1c83970267bf.mp4

## Meta

Anel Music– [@LinkedIn](https://www.linkedin.com/in/anelmusic/) – anel.music@web.de

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/AnelMusic/](https://github.com/AnelMusic/)

## Contributing

1. Fork it (<https://github.com/AnelMusic/ai_music_concert/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
