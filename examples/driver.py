import numpy as np

from fem_1d_heat.element import (
        global_to_local,
        shape_matrix,
        gradient_matrix
        )


def main():
    print('successfully imported fem_1d_heat')

    z = 3
    z_e = np.array([1, 4])
    print(f'testing global_to_local({z}, {z_e}): {global_to_local(z, z_e)}')

    s = 0.9
    print(f'testing shape_matrix({s}): {shape_matrix(s)}')

    dz = 3
    print(f'testing gradient_matrix({s}): {gradient_matrix(s,dz)}')


if __name__ == '__main__':
    main()
