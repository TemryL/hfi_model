features = ['accelerometerAccelerationX(G)', 
            'accelerometerAccelerationY(G)',
            'accelerometerAccelerationZ(G)', 
            'motionYaw(rad)', 
            'motionRoll(rad)',
            'motionPitch(rad)', 
            'motionRotationRateX(rad/s)',
            'motionRotationRateY(rad/s)', 
            'motionRotationRateZ(rad/s)',
            'motionUserAccelerationX(G)', 
            'motionUserAccelerationY(G)',
            'motionUserAccelerationZ(G)', 
            'motionQuaternionX(R)',
            'motionQuaternionY(R)', 
            'motionQuaternionZ(R)', 
            'motionQuaternionW(R)',
            'motionGravityX(G)', 
            'motionGravityY(G)', 
            'motionGravityZ(G)'
]
normalize = False

lr = 5e-4
batch_size = 16

model_name = 'Transformer'
pretrained_model = None
model_cfgs = dict(
    encoder_cfgs = dict(
        learning_rate = lr,
        feat_dim = 19, 
        max_len = 150, 
        d_model = 128, 
        num_heads = 4,
        num_layers = 4, 
        dim_feedforward = 512, 
        dropout = 0.1,
        pos_encoding = 'learnable', 
        activation = 'gelu',
        norm = 'BatchNorm', 
        freeze = False
    ),
    classifier_cfgs = dict(
        learning_rate = lr,
        warmup = 200,
        weight_decay = 1e-6
    )
)

# Directories
data_dir = "data/"
train_path = "data/supervised/train"
val_path = "data/supervised/val"
out_dir = "v1_scratch/"

# Compute related
accelerator = "cpu"
num_workers = 8
pin_memory = False