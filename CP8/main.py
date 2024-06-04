"""
Camden Harris
CSE 163 AX
Image processing and augmentation
"""

import os
import tempfile
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np

os.environ["MPLCONFIGDIR"] = tempfile.gettempdir()


def blur_image(file_in: str, file_out: str, kernel_size: int):
    """
    Uses a sliding window algorithm with a
    provided kernel size to blur an image
    Keyword arguments:
    file_in - location of file to blur
    file_out - location to save file
    kernel_size - side length of kernel
    """
    duck = imageio.imread(file_in).copy()

    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (
        kernel_size**2
    )

    blurred_img = duck.copy()

    oob_prevention = kernel_size // 2

    for i in range(oob_prevention, duck.shape[0] - oob_prevention):
        for j in range(oob_prevention, duck.shape[1] - oob_prevention):
            for c in range(3):  # Assuming the image has 3 channels (RGB)
                avg_pixel = int(
                    np.sum(
                        duck[
                            i - oob_prevention : i + oob_prevention + 1,
                            j - oob_prevention : j + oob_prevention + 1,
                            c,
                        ]
                        * kernel
                    )
                )
                print(f"{avg_pixel=}")
                blurred_img[i, j, c] = avg_pixel

    blurred_img = blurred_img / 255.0

    plt.imshow(blurred_img)
    plt.savefig(file_out)
    pass


def edge_detect(file_in, file_out, channel):
    """
    Uses a 3x3 kernel to detect edges on a given color channel
    Keyword arguments:
    file_in - location of file to edge detect
    file_out - location to save edge file
    channel - color channel (red = 1, green = 2, blue = 3)
    """
    # The input file will have 3 color channels. Instead of averaging
    # the 3 colors (RGB), use only a single channel as the input.
    # Use the edge detection kernel of size 3x3.
    # If the resulting value <=127 then make it 0, else 255.
    duck = imageio.imread(file_in).copy()

    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    edge_img = np.ones((duck.shape[0], duck.shape[1], 3))

    oob_prevention = 1

    for i in range(oob_prevention, duck.shape[0] - oob_prevention):
        for j in range(oob_prevention, duck.shape[1] - oob_prevention):
            avg_pixel = int(
                np.sum(
                    duck[
                        i - oob_prevention : i + oob_prevention + 1,
                        j - oob_prevention : j + oob_prevention + 1,
                        channel,
                    ]
                    * kernel
                )
            )
            avg_pixel = 1 if avg_pixel <= 127 else 0
            for c in range(3):
                edge_img[i, j, c] = avg_pixel

    plt.imshow(edge_img)
    plt.savefig(file_out)

    pass


def duckie_hat():
    """
    Adds a green top hat to the duck
    """
    duck_with_hat = imageio.imread("duck.jpg").copy()

    # main hat
    duck_with_hat[20:75, 85:135, 0] = 0
    duck_with_hat[20:75, 85:135, 1] = 255
    duck_with_hat[20:75, 85:135, 2] = 0

    # hat brim
    duck_with_hat[75:90, 60:160, 0] = 0
    duck_with_hat[75:90, 60:160, 1] = 255
    duck_with_hat[75:90, 60:160, 2] = 0

    plt.imshow(duck_with_hat)
    plt.savefig("duck_with_hat.png")

    pass


def main():
    duckie_hat()
    edge_detect("duck.jpg", "edge.jpg", 0)
    blur_image("duck.jpg", "blur.jpg", 5)


if __name__ == "__main__":
    main()
