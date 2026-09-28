# CS225 PA2 — Convolution Primitives and CIFAR-10

Implement the functions in `student.py`, then complete the experiment and report in
`PA2_ConvNets.ipynb`. Keep both files in the same folder. Task instructions and grading
details are in the notebook.

**Release:** 20 September 2026 · **Due:** 27 September 2026 (see Blackboard for the exact cutoff).

## Colab (recommended)

1. Upload the notebook and `student.py`. Select **Runtime → Change runtime type → T4 GPU**.
2. Run the dependency installation cell under **Setup**. It includes all required
   packages; you do not need to upload `requirements.txt`. Keep Colab's compatible
   preinstalled packages and do not add `--upgrade`. Restart the runtime if packages change.
3. Complete the TODOs in `student.py`, reload the module, and run the self-checks.
   Re-upload the file if you edit it outside Colab.
4. Run the notebook with **`DEBUG=False`** for the full 10-epoch experiment, answer
   the four report questions, and save all outputs.

Self-checks work on CPU. The full experiment requires CUDA; `DEBUG=True` runs only
a small CPU check and is not a submission run.

## Local setup

Use **Python 3.11+**. In the folder containing the notebook:

```bash
python -m venv .venv
```

Activate with `.venv\Scripts\Activate.ps1` on Windows PowerShell or
`source .venv/bin/activate` on macOS/Linux. For a local NVIDIA GPU, first install a
compatible CUDA-enabled torch/torchvision pair using the
[PyTorch installer](https://pytorch.org/get-started/locally/), then run:

```bash
python -m pip install -r requirements.txt
python -m jupyter lab
```

Select the notebook kernel for this environment. A tested local combination is
Python **3.12.10**, torch **2.8.0+cu128** and torchvision **0.23.0+cu128**; Colab does
not need to match these exact versions. Before full training, this check must print
`True`; if no compatible local GPU is available, use Colab:

```python
import torch
print(torch.cuda.is_available())
```

## Dataset

Reuse the CIFAR-10 dataset from PA1. Set `DATA_DIR` in Part 5 to the folder containing
`cifar-10-batches-py/` (default: `data`). Alternatively, place your saved
`cifar-10-python.tar.gz` in that folder; the loader extracts it automatically.
In Colab, upload the saved archive or access your PA1 data through Google Drive,
then set `DATA_DIR` accordingly.

## Submit

Restart the kernel, run the full notebook, complete the four responses, and submit:

- `student.py`
- `PA2_LastName_FirstName_V1.ipynb`, with outputs saved

Do not submit data, checkpoints or archives. Download both submission files before
ending a Colab session.
