# Style Transfer Project
This project uses deep learning to compose one image in the style of another image. This is known as neural style transfer and the technique will be outlined in A Neural Algorithm of Artistic Style (Gatys et al.) This project will demonstrate the original style-transfer algorithm. It optimizes the image content to a particular style. Modern approaches train a model to generate the stylized image directly (similar to cyclegan). This approach is much faster (up to 1000x).
Neural style transfer is an optimization technique used to take two images—a content image and a style reference image (such as an artwork by a famous painter)—and blend them together so the output image looks like the content image, but “painted” in the style of the style reference image. This is implemented by optimizing the output image to match the content statistics of the content image and the style statistics of the style reference image. These statistics are extracted from the images using a convolutional network.

## Insight On Style Transfer using Convolutional Neural Networks
Convolutional neural networks have proven to be tremendous in image classification and recognition tasks. CNNs have been shown to be able to replicate and optimize image representations in a unified framework and learn hierarchical representations directly from raw images.

## Project Requirements
- A code editor
- Numpy
- Matplotlib
- Pytorch
- pytorch vision
- scipy
- Streamlit

## Methodology
- Getting the pre-trained model.
- Downloading the saved model.
- Creating the style file.
- Creating Streamlit file/[transfer.py](https://github.com/Alexelofu/Style-Transfer-Project/blob/main/style/neural_style/transfer.py)
- Deploying to docker.

## References
* [Wikipedia NST](https://en.wikipedia.org/wiki/Neural_Style_Transfer#NST)
* [A Neural Algorithm of Artistic Style (Gatys et al.)](https://arxiv.org/pdf/1508.06576.pdf)
* [Pytorch-Style-Transfer](https://modelzoo.co/model/pytorch-style-transfer)
* [Neural Style Transfer with Pytorch](https://pytorch.org/tutorials/advanced/neural_style_tutorial.html)

