import sys
import pandas
import numpy
import seaborn
import scipy
import subprocess

print('Versão do Python ->', sys.version)
try:
    pip_version = subprocess.check_output(
        ['pip', '--version'], universal_newlines=True)
    print("Versão do pip:", pip_version.strip())
except subprocess.CalledProcessError:
    print("O comando pip não pôde ser executado. \
          Verifique se o pip está instalado.")
print('Versão do pandas -> %s' % pandas.__version__)
print('Versão do numpy -> %s' % numpy.__version__)
print('Versão do seaborn -> %s' % seaborn.__version__)
print('Versão do scipy -> %s' % scipy.__version__)