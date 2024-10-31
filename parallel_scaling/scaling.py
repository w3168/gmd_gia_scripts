import argparse
import numpy as np
import re
import subprocess
import sys
from pathlib import Path

# Ignore the memory - really this should be 500GB for each node...!
# and dx is structured isostropic so not varying horizontally...!
strong_cases = [
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr26cores_mem4000gb_dx40to200km_nz75a4_weak_iso_nnTru5_2",
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr52cores_mem4000gb_dx40to200km_nz75a4_weak_iso_nnTru5_2",
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr104cores_mem4000gb_dx40to200km_nz75a4_weak_iso_nnTru5_2",
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr208cores_mem4000gb_dx20to200km_nz150a4_weak_iso_nnTru5_2",
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr416cores_mem4000gb_dx20to200km_nz150a4_weak_iso_nnTru5_2",
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr832cores_mem4000gb_dx20to200km_nz150a4_weak_iso_nnTru5_2",
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr1664cores_mem4000gb_dx10to200km_nz300a4_weak_iso_nnTru5_2",
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr3328cores_mem4000gb_dx10to200km_nz300a4_weak_iso_nnTru5_2",
#        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr6656cores_mem4000gb_dx10to200km_nz300a4_weak_iso_nnTru5_2", # Had temporary slowdown possibly due to a set of nodes?
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr6656cores_mem4000gb_dx10to200km_nz300a4_weak_iso_nnTru8_2",
        ]

weak_cases = [
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr104cores_mem4000gb_dx40to200km_nz75a4_weak_iso_nnTru5_2",
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr208cores_mem4000gb_dx31.7to200km_nz94a4_weak_iso_nnTru5_2",
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr416cores_mem4000gb_dx25.2to200km_nz119a4_weak_iso_nnTru5_2",
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr832cores_mem4000gb_dx20to200km_nz150a4_weak_iso_nnTru5_2",
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr1664cores_mem4000gb_dx15.9to200km_nz189a4_weak_iso_nnTru5_2",
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr3328cores_mem4000gb_dx12.6to200km_nz238a4_weak_iso_nnTru5_2",
#        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr6656cores_mem4000gb_dx10to200km_nz300a4_weak_iso_nnTru5_2", # Had temporary slowdown possibly due to a set of nodes?
        "30.10.24_weerdesteijn_1000_dt50yr_dtout10ka_normalsr6656cores_mem4000gb_dx10to200km_nz300a4_weak_iso_nnTru8_2",
        ]
weak_cores = [104, 208, 416, 832, 1664, 3328, 6656]


def get_data(path, base_path=Path("logfiles")):
    """Return the timing and iteration metrics for a given level"""

    base_path = base_path or Path()
    output_path = base_path / path
    profile_path = base_path / path

    if not (output_path.exists() and profile_path.exists()):
        raise FileNotFoundError(f"outputs not found")

    # total time (profile)
    data = {}

    iteration_component_map = {
        "ViscoelasticStokesSolver_fieldsplit_0_": "velocity",
        "ViscoelasticStokesSolver_fieldsplit_1_": "pressure",
    }

    iterations = {
        "velocity": [],
        "pressure": [6], # Plotting hack!!!! I think I forgot to explicitly output number of FS1 its. but it was always consistently 6
    }

    with open(output_path, "r") as f:
        for line in f:
            if m := re.match(r"\s+Linear (\S+) solve converged due to CONVERGED_RTOL iterations (\d+)", line):
                iterations[iteration_component_map[m.group(1)]].append(int(m.group(2)))

    for k, v in iterations.items():
        data[f"{k}_iterations"] = np.mean(np.array(v))

    with open(profile_path, "r") as f:
        for line in f:
            if "stokes_solve:" in line:
                data["stokes_solve"] = float(line.split()[2])

            if "snes_function" not in data and line.startswith("SNESFunctionEval"):
                data["snes_function"] = float(line.split()[3])
            if "snes_jacobian" not in data and line.startswith("SNESJacobianEval"):
                data["snes_jacobian"] = float(line.split()[3])

            # space is important to avoid the PCSetup_GAMG+ entry
            if "pc_setup" not in data and line.startswith("PCSetUp "):
                data["pc_setup"] = float(line.split()[3])

            if line.startswith("Time"):
                data["total_time"] = float(line.split()[4])

    return data


