from distutils.core import setup

setup(
      name = 'GPUtil',
      packages = ['GPUtil'],
      version = '1.2.0',
      description = 'GPUtil is a Python module for getting the GPU status from NVIDA GPUs using nvidia-smi.',
      author = 'Anders Krogh Mortensen',
      author_email = 'anderskroghm@gmail.com',
      url = 'https://github.com/anderskm/gputil',
      download_url = 'https://github.com/anderskm/gputil/tarball/v1.2.0',
      keywords = ['gpu','utilization','load','memory','available','usage','free'],
      install_requires = ['numpy'],
      classifiers = [],
)
