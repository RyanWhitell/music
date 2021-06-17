# Helpful Links
## Code
* [Music Theory in Python](https://www.mvanga.com/blog/basic-music-theory-in-200-lines-of-python?fbclid=IwAR0qim8mm9PKJkGzTjqJColIjLCa1FpgoES1HzY6hQZHQfjGUF0Zicvv0Io#fnref1)

## Theory
* [Music Theory in 16 Minutes](https://www.youtube.com/watch?v=_eKTOMhpy2w)

## Bass
* [Study Bass](https://www.studybass.com/study-guide/)
* [Bass Music Notation](https://www.halleonard.com/bin/musicNotationBass.pdf)

# How to Setup
1. Install [Conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
1. Install jupypter
    * `conda install jupyterlab`
    * `conda install nb_conda_kernels`
1. Create a new music env
    * `conda create --name music`
    * `conda activate --music`
1. Install required packages
    * `conda install pip`
    * `conda install ipykernel`
1. Install [abjad](http://abjad.mbrsi.org/installation.html)
    * Install abjad:
        * `pip install abjad`
        * `pip install abjad-ext-ipython`
    * Install all [dependancies](http://abjad.mbrsi.org/installation.html) and include:
        * `brew install fluidsynth`
1. Run Jupyter in base using the music kernel:
    * `conda deactivate`
    * `jupyter lab`

The conda environment is also available in _music.yml_
