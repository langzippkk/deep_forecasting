import torch

opts = {
    # data
    'data_path': '../data',
    'data_filename': 'ts_data.csv',

    # file names
    'vae_state': 'vae_ckpt.pth',
    'nn_state': 'nn_ckpt.pth',

    # configuration
    'visdom': False,      # whether plotting is desired
    'plot': 99,           # at which epoch to plot graphs

    # splits
    'train_per': 0.75,    # training split
    'valid_per': 0.05,    # validation split (rest is testing)

    # training
    'batch_size': 1,      # batch size
    'epochs': 100,        # number of epochs to train
    'frame': 7,           # length of time series data to consider
    'test_frequency': 5,  # how often to evaluate test set
    'lr': 1e-3,           # learning rate
    'b1': 0.95,           # Adam beta1 parameter
    'dropout': 0.5,       # probability of dropout

    # other
    'fudge': 1e-7,        # fudge factor for numerical stability

    # gpu
    'use_cuda': True and torch.cuda.is_available()
}
