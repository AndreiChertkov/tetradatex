# tetradatex


## Description

Package `tetradatex` (**TE**nsor **TR**ain **AD**versarial **AT**tacks; **ex**periments) for generation of adversarial examples for artificial neural networks from computer vision domain using tensor train (TT) decomposition and PROTES optimizer based on it. Please, see [teneva](https://github.com/AndreiChertkov/teneva) and [PROTES](https://github.com/anabatsh/PROTES) repositories for details.


## Installation

1. Install [anaconda](https://www.anaconda.com) package manager with [python](https://www.python.org) (version 3.8);

2. Create a virtual environment:
    ```bash
    conda create --name tetradatex python=3.10 -y
    ```
    > You may need to run `source ~/miniconda3/etc/profile.d/conda.sh` before.

3. Activate the environment:
    ```bash
    conda activate tetradatex
    ```

4. Download this repo (optional):
    ```bash
    git clone https://github.com/AndreiChertkov/tetradatex.git && cd tetradatex
    ```

5. Install [LLaVA](https://github.com/haotian-liu/LLaVA) framework:
    ```bash
    git clone https://github.com/haotian-liu/LLaVA.git && cd LLaVA && pip install -e . && pip install aiohttp fsspec[http]==2024.2.0 pyarrow tensorboardx && pip install transformers==4.37.2 && cd ./../
    ```
    > In the case of problems, remove in llava/model/__init__.py `try` block before installing

6. Install other dependencies:
    ```bash
    pip install sentence-transformers
    ```

7. Delete virtual environment at the end of the work (optional):
    ```bash
    conda activate && conda remove --name tetradatex --all -y
    ```
 

## Usage

Run `test_llava.py` and `test_sim.py`.


## Authors

- [Andrei Chertkov](https://github.com/AndreiChertkov)
- [Ivan Oseledets](https://github.com/oseledets)