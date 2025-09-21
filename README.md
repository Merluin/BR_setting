# 🧠 VR-Based Binocular Rivalry (BR) Setup

This repository contains all the resources needed to build and test a **VR-based binocular rivalry display**, adapted from a commercially available headset using a **4K HDMI screen** and **3D-printed mounts**. The setup is optimized for experiments involving **binocular rivalry** (BR), with support for **PsychoPy** stimuli presentation.

> 🛠️ This is a DIY research tool. Use at your own risk and only in appropriate research contexts.

---

## 📦 Features

- 🔄 Physically separated left/right visual input
- 📺 Uses a 60Hz 4K HDMI screen (BestView S5 or similar)
- 🧲 Mounts directly inside a dual-lens VR headset
- 🧩 Includes custom 3D-printed support files (`.stl`)
- 🎯 Compatible with PsychoPy experiments
- 🧪 BR stimuli can be shown side-by-side on screen halves

---

## 🧱 Materials List

| Component        | Description / Link |
|------------------|--------------------|
| 🥽 VR Headset    | [Naxa NA-4011 HoloVue](https://www.ubuy.sn/fr/product/2EMBZGRW-naxa-na-4011-holovue-vr-glasses) |
| 🖥️ HDMI Monitor  | [Best View S5 - 4K, 60Hz](https://www.amazon.it/dp/B07PLDDZBY) |
| 🔌 Power Supply  | [12V 5A Adapter](https://www.amazon.it/dp/B07XDSR4DK) |
| 🔗 HDMI Cable    | Standard, 2m (or length as needed) |

> 🧾 *Note: Not a sponsored post — these are the components actually used.*

---

## 🧩 Included Files

- `VRMAX.stl`: 3D model for head-mounting screen
- `vrpivot.stl`: 3D model for alignment and pivot support
- `psychopy_BR_test/`: Example PsychoPy script to test left/right field presentation
- `Schermata 2022-02-21 alle 19.57.37.jpeg`: Assembly preview image

---

## 🔧 Assembly Overview

- Replace the phone slot in the headset with the 4K screen
- Use 3D-printed parts to secure and align the screen inside the headset
- Each optical chamber ensures one eye sees only one half of the screen
- Connect the screen via HDMI to the experimental PC

> The 4K screen acts as a **standard secondary display**. Set your OS to mirror or extend it and run BR stimuli targeting left/right halves of the screen.

---

## 🎯 Using with PsychoPy

- Open and configure the provided `.psyexp` file
- Set the window size to half-screen width per eye
- Use monitor settings to adjust alignment
- Present rival stimuli on left/right halves (e.g., red vs. green gratings)

---

## ⚠️ Disclaimer

This is a **research prototype**, not a commercial device. Ensure:
- Electrical safety of components
- Proper calibration for optical alignment
- Ethical use in compliance with institutional guidelines

---

## 📬 Contact

For questions or collaboration:

- **Thomas Quettier** — [thomas.quettier2@unibo.it](mailto:thomas.quettier2@unibo.it)

---

## 📄 License

This project is shared under the **MIT License**. See the [`LICENSE`](LICENSE) file for details.

---

## 🙏 Acknowledgements

Developed within a behavioral neuroscience context to support open, low-cost, and customizable solutions for high-resolution vision research.

---

## 🔗 Related Projects

- [PsychoPy](https://www.psychopy.org/)
- [BestView S5](https://www.amazon.it/dp/B07PLDDZBY)

---
