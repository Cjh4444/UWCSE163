import os
import tempfile
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np

os.environ["MPLCONFIGDIR"] = tempfile.gettempdir()


def blur_image(file_in, file_out, kernel_size):
    """
    file_in is the name of the file to blur
    file_out is the name of the output file
    kernel_size is >= 3 and is the size of the kernel used to blur
    The method will create a blurred image of the original by
    applying a blur kernel (a convolution). The kernel will be
    applied to each of the 3 color channels. It is a 2D matrix
    of all 1's and averaged by the number of elements. For example,
    a 3x3 kernel will average the 9 elements' values.
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
    file_in is the name of the file to detect edges
    file_out is the name of the output file, in gray scale only.
    Channel is: 0=Red, 1=Green, 2=Blue
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
    Add a green hat to the duck as described in the online lessons.
    The main-hat should be a rectangle with the top-left corner at (20, 85)
    and the bottom-right corner at (75, 135).
    The hat brim should be a rectangle with the top-left corner at (75, 60)
    and the bottom-right corner at (90, 160).
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
