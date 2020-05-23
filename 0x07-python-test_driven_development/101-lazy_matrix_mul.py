#!/usr/bin/python3

"""lazy_matrix_mul"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrix"""
    return(np.matmul(m_a, m_b))
