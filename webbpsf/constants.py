# This file contains constants and data that do not fit in the data
# package for one reason or another. It could be that they are in a
# data structure that doesn't serialize well or they're too small to
# make a separate file.

# It's hard to make anything truly immutable in Python, but here
# tuples are preferred and numpy arrays should have
# flags.writeable = False

import numpy as np

__all__ = (
    'JWST_PRIMARY_SEGMENTS',
    'JWST_PRIMARY_STRUTS',
    'JWST_PRIMARY_SEGMENT_CENTERS',
    'JWST_SEGMENT_RADIUS',
    'JWST_CIRCUMSCRIBED_DIAMETER',
    'SEGNAMES',
    'SEGNAMES_WSS',
)

SEGNAMES = tuple([letter + str(number) for letter in ['A', 'B', 'C'] for number in range(1, 7)])

#
# JWST Primary segment and obscuration shapes and centers
#
# Provenance:
#
# Segment coordinates from "2010.03.16 Transmission X Area Budget.xls"
# spreadsheet by Paul Lightsey, which was based in turn on
# Ball Aerospace drawing # 2220169 Rev B and the OTE Cryogenic Optics
# Interface Control Document, Ball Aerospace doc # C327693

JWST_PRIMARY_SEGMENTS = (
    (
        'A1-1',
        np.array(
            [
                [-0.38101, 0.667604],
                [-0.758826, 1.321999],
                [-0.38101, 1.976407],
                [0.38101, 1.976407],
                [0.758826, 1.321999],
                [0.38101, 0.667604],
            ]
        ),
    ),
    (
        'A2-2',
        np.array(
            [
                [0.38765702, 0.66376634],
                [0.76547172, 1.31816209],
                [1.52111367, 1.31816784],
                [1.90212367, 0.65823916],
                [1.52429772, 0.00383691],
                [0.76866702, 0.00383766],
            ]
        ),
    ),
    (
        'A3-3',
        np.array(
            [
                [0.76866702, -0.00383766],
                [1.52429772, -0.00383691],
                [1.90212367, -0.65823916],
                [1.52111367, -1.31816784],
                [0.76547172, -1.31816209],
                [0.38765702, -0.66376634],
            ]
        ),
    ),
    (
        'A4-4',
        np.array(
            [
                [0.38101, -0.667604],
                [0.758826, -1.321999],
                [0.38101, -1.976407],
                [-0.38101, -1.976407],
                [-0.758826, -1.321999],
                [-0.38101, -0.667604],
            ]
        ),
    ),
    (
        'A5-5',
        np.array(
            [
                [-0.38765702, -0.66376634],
                [-0.76547172, -1.31816209],
                [-1.52111367, -1.31816784],
                [-1.90212367, -0.65823916],
                [-1.52429772, -0.00383691],
                [-0.76866702, -0.00383766],
            ]
        ),
    ),
    (
        'A6-6',
        np.array(
            [
                [-0.76866702, 0.00383766],
                [-1.52429772, 0.00383691],
                [-1.90212367, 0.65823916],
                [-1.52111367, 1.31816784],
                [-0.76547172, 1.31816209],
                [-0.38765702, 0.66376634],
            ]
        ),
    ),
    (
        'B1-7',
        np.array(
            [
                [0.38101, 3.279674],
                [0.758826, 2.631791],
                [0.38101, 1.98402],
                [-0.38101, 1.98402],
                [-0.758826, 2.631791],
                [-0.38101, 3.279674],
            ]
        ),
    ),
    (
        'B2-9',
        np.array(
            [
                [3.030786, 1.30987266],
                [2.65861086, 0.65873291],
                [1.90871672, 0.66204566],
                [1.52770672, 1.32197434],
                [1.89978486, 1.97305809],
                [2.649776, 1.96980134],
            ]
        ),
    ),
    (
        'B3-11',
        np.array(
            [
                [2.649776, -1.96980134],
                [1.89978486, -1.97305809],
                [1.52770672, -1.32197434],
                [1.90871672, -0.66204566],
                [2.65861086, -0.65873291],
                [3.030786, -1.30987266],
            ]
        ),
    ),
    (
        'B4-13',
        np.array(
            [
                [-0.38101, -3.279674],
                [-0.758826, -2.631791],
                [-0.38101, -1.98402],
                [0.38101, -1.98402],
                [0.758826, -2.631791],
                [0.38101, -3.279674],
            ]
        ),
    ),
    (
        'B5-15',
        np.array(
            [
                [-3.030786, -1.30987266],
                [-2.65861086, -0.65873291],
                [-1.90871672, -0.66204566],
                [-1.52770672, -1.32197434],
                [-1.89978486, -1.97305809],
                [-2.649776, -1.96980134],
            ]
        ),
    ),
    (
        'B6-17',
        np.array(
            [
                [-2.649776, 1.96980134],
                [-1.89978486, 1.97305809],
                [-1.52770672, 1.32197434],
                [-1.90871672, 0.66204566],
                [-2.65861086, 0.65873291],
                [-3.030786, 1.30987266],
            ]
        ),
    ),
    (
        'C1-8',
        np.array(
            [
                [0.765201, 2.627516],
                [1.517956, 2.629178],
                [1.892896, 1.976441],
                [1.521076, 1.325812],
                [0.765454, 1.325807],
                [0.387649, 1.980196],
            ]
        ),
    ),
    (
        'C2-10',
        np.array(
            [
                [2.6580961, 0.651074495],
                [3.03591294, 5.42172989e-07],
                [2.65809612, -0.651075523],
                [1.90872487, -0.654384457],
                [1.53090954, 8.90571587e-07],
                [1.90872454, 0.654384118],
            ]
        ),
    ),
    (
        'C3-12',
        np.array(
            [
                [1.8928951, -1.97644151],
                [1.51795694, -2.62917746],
                [0.76520012, -2.62751652],
                [0.38764887, -1.98019646],
                [0.76545554, -1.32580611],
                [1.52107554, -1.32581188],
            ]
        ),
    ),
    (
        'C4-14',
        np.array(
            [
                [-0.765201, -2.627516],
                [-1.517956, -2.629178],
                [-1.892896, -1.976441],
                [-1.521076, -1.325812],
                [-0.765454, -1.325807],
                [-0.387649, -1.980196],
            ]
        ),
    ),
    (
        'C5-16',
        np.array(
            [
                [-2.6580961, -0.651074495],
                [-3.03591294, -5.42172990e-07],
                [-2.65809612, 0.651075523],
                [-1.90872487, 0.654384457],
                [-1.53090954, -8.90571587e-07],
                [-1.90872454, -0.654384118],
            ]
        ),
    ),
    (
        'C6-18',
        np.array(
            [
                [-1.8928951, 1.97644151],
                [-1.51795694, 2.62917746],
                [-0.76520012, 2.62751652],
                [-0.38764887, 1.98019646],
                [-0.76545554, 1.32580611],
                [-1.52107554, 1.32581188],
            ]
        ),
    ),
)

for name, arr in JWST_PRIMARY_SEGMENTS:
    arr.flags.writeable = False

# A1-6,B1-6,C1-6
SEGNAMES_WSS = tuple(name for name, arr in JWST_PRIMARY_SEGMENTS)

# Sort same names by another order: A1-6,B1,C1,B2,C2,etc
SEGNAMES_WSS_ORDER = tuple(np.asarray(SEGNAMES_WSS)[np.argsort([int(a.split('-')[1]) for a in SEGNAMES_WSS])])

# Coordinates for primary obscuration. This information is used in the
# WebbPrimaryAperture class, which is used to create the (static) pupil models as
# FITS files in the WEBBPSF_DATA directory.
JWST_PRIMARY_STRUTS = (
    # the first three components are derived from coordinates in the
    # OTE cryogenic optical ICD,  Ball Aerospace doc # C327693
    (
        'strut1',
        np.array(
            [
                [-0.05301375, -0.0306075],
                [1.59698625, -2.88849133],
                [1.70301375, -2.82727633],
                [0.05301375, 0.0306075],
                [-0.05301375, -0.0306075],
            ]
        ),
    ),
    (
        'strut2',
        np.array(
            [
                [-0.05301375, 0.0306075],
                [-1.70301375, -2.82727633],
                [-1.59698625, -2.88849133],
                [0.05301375, -0.0306075],
                [-0.05301375, 0.0306075],
            ]
        ),
    ),
    # The vertical strut is made slightly narrower than the optical ICD'scut-out allocation,
    # to better match the observed diffraction pattern width in the horizontal spikes
    # which diffracts due to this strut.,
    ('SMSS +v3 strut', np.array(
            [
             [ 5.52745500e-02, -1.45573765e-17],
             [ 5.52745500e-02,  3.30000000e+00],
             [-5.52745500e-02,  3.30000000e+00],
             [-5.52745500e-02,  1.45573765e-17],
             [ 5.52745500e-02, -1.45573765e-17]
            ]
        ),
    ),
    # the next two comonents are derived from estimates made from NIRCam pupil imaging
    # in flight. These coordinates attempt to trace out the somehwat irregular edges of the
    # obscuration from the +v3 SMSS mid-hinge and associated hardware,
    # and the surrounding insulation. This is inherently of at best moderate fidelity, since
    # this is modeling a soft structure simplified as a polygon.
    ('flight +V3 SMSS hinge, right side', np.array([
         [0.0, 2.0],
         [0.06, 2.03],
         [0.09, 2.23430962],
         [0.09, 2.3],
         [0.085, 2.31],
         [0.085, 2.35],
         [0.09, 2.36],
         [0.095, 2.45],
         [0.09, 2.47],
         [0.09, 2.51],
         [0.095, 2.52],
         [0.09, 2.565],
         [0.087, 2.574],
         [0.06, 2.6],
         [0.0, 2.6],
         [0.0, 2.07531381]])),
     ('flight +V3 SMSS hinge, left side', np.array([
         [-0.    ,  2.    ],
         [-0.054 ,  2.03  ],
         [-0.081 ,  2.234 ],
         [-0.081 ,  2.25  ],
         [-0.0765,  2.27  ],
         [-0.0765,  2.35  ],
         [-0.081 ,  2.36  ],
         [-0.095 ,  2.45  ],
         [-0.09  ,  2.47  ],
         [-0.09  ,  2.51  ],
         [-0.095 ,  2.52  ],
         [-0.09  ,  2.565 ],
         [-0.087 ,  2.574 ],
         [-0.06  ,  2.6   ],
         [-0.    ,  2.6   ],
         [-0.    ,  2.075 ]])),
    # The next two components represent the tuned mass dampers on the lower SMSS
    # struts, and their surrounding insulation. The coordinates are computed from
    # simplified elliptical models that approximate the obscurations seen in the
    # pupil camera images. Left is a regular ellipse, offset. Right is an ellipse that
    # has been tapered to better match the observed shape.
    ('lower SMSS obscuration, right', np.array([
         [ 0.97794229, -1.555     ],
         [ 0.954165  , -1.52255587],
         [ 0.92958552, -1.49139882],
         [ 0.90479515, -1.46199671],
         [ 0.88036645, -1.43479905],
         [ 0.85683372, -1.4102344 ],
         [ 0.83467652, -1.3887067 ],
         [ 0.81430685, -1.37059052],
         [ 0.79606061, -1.35622507],
         [ 0.7801936 , -1.34590701],
         [ 0.76688188, -1.3398823 ],
         [ 0.75622626, -1.33833738],
         [ 0.74826022, -1.34139029],
         [ 0.74296042, -1.34908209],
         [ 0.74025891, -1.36136935],
         [ 0.74005586, -1.37811828],
         [ 0.7422319 , -1.39910101],
         [ 0.74665895, -1.42399462],
         [ 0.75320886, -1.45238326],
         [ 0.76175921, -1.48376353],
         [ 0.77219587, -1.51755326],
         [ 0.78441231, -1.55310344],
         [ 0.79830582, -1.58971311],
         [ 0.81377118, -1.62664659],
         [ 0.83069236, -1.66315243],
         [ 0.84893327, -1.69848344],
         [ 0.86832835, -1.73191678],
         [ 0.88867421, -1.76277344],
         [ 0.90972307, -1.79043621],
         [ 0.93117902, -1.81436543],
         [ 0.95269763, -1.83411189],
         [ 0.97388936, -1.84932641],
         [ 0.9943269 , -1.85976585],
         [ 1.0135563 , -1.86529545],
         [ 1.0311114 , -1.86588756],
         [ 1.0465309 , -1.86161706],
         [ 1.05937711, -1.85265401],
         [ 1.06925531, -1.83925389],
         [ 1.07583253, -1.82174629],
         [ 1.07885467, -1.80052257],
         [ 1.07816072, -1.7760233 ],
         [ 1.07369325, -1.74872598],
         [ 1.0655044 , -1.71913365],
         [ 1.05375689, -1.6877648 ],
         [ 1.03871996, -1.6551448 ],
         [ 1.02076035, -1.62179895],
         [ 1.00032869, -1.58824716],
         [ 0.97794229, -1.555     ]])),
 ('lower SMSS obscuration, left', np.array([
     [-0.82839746, -1.66      ],
         [-0.80917713, -1.62492491],
         [-0.79184521, -1.58958348],
         [-0.77671099, -1.55460639],
         [-0.76404454, -1.52061779],
         [-0.7540719 , -1.48822422],
         [-0.74697102, -1.45800375],
         [-0.74286862, -1.43049565],
         [-0.74183791, -1.40619081],
         [-0.74389728, -1.38552295],
         [-0.74900999, -1.36886089],
         [-0.75708479, -1.35650197],
         [-0.76797759, -1.34866672],
         [-0.78149401, -1.34549497],
         [-0.79739284, -1.34704331],
         [-0.81539038, -1.35328413],
         [-0.83516546, -1.36410605],
         [-0.85636518, -1.37931595],
         [-0.87861125, -1.39864241],
         [-0.90150667, -1.42174055],
         [-0.92464288, -1.44819819],
         [-0.94760701, -1.47754319],
         [-0.96998928, -1.50925188],
         [-0.99139025, -1.54275842],
         [-1.01142804, -1.57746489],
         [-1.02974507, -1.61275195],
         [-1.04601447, -1.6479899 ],
         [-1.05994592, -1.68254992],
         [-1.0712908 , -1.71581529],
         [-1.07984667, -1.74719238],
         [-1.08546084, -1.77612127],
         [-1.08803314, -1.80208572],
         [-1.08751766, -1.82462239],
         [-1.08392359, -1.84332913],
         [-1.07731508, -1.8578721 ],
         [-1.06781006, -1.86799179],
         [-1.05557813, -1.8735076 ],
         [-1.04083759, -1.87432112],
         [-1.02385147, -1.87041782],
         [-1.00492289, -1.86186736],
         [-0.98438964, -1.84882232],
         [-0.96261812, -1.83151549],
         [-0.93999686, -1.81025571],
         [-0.91692953, -1.78542237],
         [-0.89382777, -1.7574586 ],
         [-0.87110383, -1.72686344],
         [-0.84916322, -1.69418284],
         [-0.82839746, -1.66      ]]))
)

for name, arr in JWST_PRIMARY_STRUTS:
    arr.flags.writeable = False

JWST_PRIMARY_SEGMENT_CENTERS = (
    ('A1-1', (0.000000, 1.323500)),
    ('A2-2', (1.146185, 0.661750)),
    ('A3-3', (1.146185, -0.661750)),
    ('A4-4', (0.000000, -1.323500)),
    ('A5-5', (-1.146185, -0.661750)),
    ('A6-6', (-1.146185, 0.661750)),
    ('B1-7', (0.000000, 2.634719)),
    ('B2-9', (2.281734, 1.317360)),
    ('B3-11', (2.281734, -1.317359)),
    ('B4-13', (0.000000, -2.634719)),
    ('B5-15', (-2.281734, -1.317360)),
    ('B6-17', (-2.281734, 1.317360)),
    ('C1-8', (1.142963, 1.979670)),
    ('C2-10', (2.285926, 0.000000)),
    ('C3-12', (1.142963, -1.979670)),
    ('C4-14', (-1.142963, -1.979670)),
    ('C5-16', (-2.285926, -0.000000)),
    ('C6-18', (-1.142963, 1.979670)),
)

# TODO - add in V1 positions to the above? 0.055154 for As, 0.218578 Bs, 0.164535 Cs

JWST_SEGMENT_RADIUS = 1.517 / 2
JWST_CIRCUMSCRIBED_DIAMETER = 6.603464  # meters. Outer corners of B segments
JWST_INSCRIBED_DIAMETER = 5.47334  # meters. Middle corners of C segments

JWST_TYPICAL_LOS_JITTER_PER_AXIS = 0.0008  # milliarcseconds jitter, 1 sigma per axis. = approx 1 mas rms radial, typically


# ad hoc, highly simplified models for charge diffusion within detectors
# These values are PLACEHOLDERS and should be updated based on comparisons with data and ePSFs (ongoing)
# Note, these are parameterized as arcseconds for convenience (and consistency with the jitter paramater)
# but the underlying physics cares more about detector pixel pitch.
INSTRUMENT_DETECTOR_CHARGE_DIFFUSION_DEFAULT_PARAMETERS = {
    'NIRCAM_SW': 0.0062,  # Fit by Marcio to WFS TA ePSFs, and by Marshall to prelim NIRCam SW ePSFs by J. Anderson
    'NIRCAM_LW': 0.018,  # Fit by Marshall to prelim LW ePSFs by J. Anderson
    'NIRISS': 0.0202,  # Fit by Marcio to MIMF-3 F158M (ePSF), and by Marshall to NIRISS ePSFs by Anderson & Libralato
    'FGS': 0.07,  # Fit by Marcio to FGS_ID images
    'NIRSPEC': 0.036,
    'MIRI': 0.001,  # Fit by Marshall + Marcio to ePSFs, after adding IPC
    #  0.070 Based on user reports, see issue #674. However, this was before adding IPC effects
}
# add Interpixel capacitance (IPC) effects. These are the parameters for each detector kernel
# For NIRCam we  use CV3/Flight convolution kernels from Jarron Leisenring, see detectors.apply_detector_ipc for details
# NIRISS has different kernels provided by Kevin Volk (STScI), see detectors.apply_detector_ipc for details
INSTRUMENT_IPC_DEFAULT_KERNEL_PARAMETERS = {
    'MIRI': (0.033, 0.024, 0.013),  # Based on JWST-STScI-002925 by Mike Engesser
}

# How many detector pixels to mask out for the inner "hole" in the cruciform?
# See Gaspar et al. 2021 for illustrative figures.
# This is a rough approximation of a detector-position-dependent phenomenon
MIRI_CRUCIFORM_INNER_RADIUS_PIX = 12
MIRI_CRUCIFORM_RADIAL_SCALEFACTOR = 0.005   # Brightness factor for the diffuse circular halo
