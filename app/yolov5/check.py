import torch

from IPython.display import Image, clear_output #to display images
from utils.downloads import attempt_download #to download models

print(torch.version.cuda)
print('Setup Complete. Using torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))