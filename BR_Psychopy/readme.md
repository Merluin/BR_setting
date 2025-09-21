# 📘 Binocular Rivalry VR Setup 

## 🧠 Objective

This PsychoPy script sets up a binocular rivalry (BR) experiment using a custom VR headset. It allows the participant to:

1. Adjust focus using the headset knobs (*molette*).
2. Align the image via keyboard controls.
3. Run two 30-second BR trials with visual stimuli presented to both eyes.

---

## 🗓️ Timeline of the Experiment

| **Phase**                | **Duration**  | **What Happens**                        | **Participant Action**                    |
|--------------------------|---------------|------------------------------------------|-------------------------------------------|
| 1. Right Eye Image       | Until keypress| Image shown to **right eye only**       | Adjust headset focus using molette        |
| 2. Left Eye Image        | Until keypress| Image shown to **left eye only**        | Adjust headset focus using molette        |
| 3. Both Eyes — Alignment | Until SPACE   | Image shown to **both eyes**            | Use ⬆️ / ⬇️ to align image on X-axis       |
| 4. BR Trial 1            | 30 seconds    | Rivalry stimulus presented              | Passive viewing                           |
| 5. BR Trial 2            | 30 seconds    | Rivalry stimulus repeated               | Passive viewing                           |

---

## 🕹️ Navigation & Controls

### During Alignment Phase:

- Press **⬆️ UP arrow**: Move stimulus **rightward** along the X-axis
- Press **⬇️ DOWN arrow**: Move stimulus **leftward** along the X-axis
- Press **SPACE**: Confirm alignment and begin BR trials

### During BR Trials:

- No input is needed — participants passively view the rivalry stimuli

---

## 🧾 Logging Output

- The **final X-axis position** of the aligned stimulus is logged in the PsychoPy `.log` file when the SPACE key is pressed
- This value can be used to assess or adjust for individual differences in visual alignment

---

## 📂 Folder & Resource Requirements

Ensure the following are correctly set up:

- `VR_setting.py` – the main experiment script
- Stimulus image files – properly referenced in the code (e.g., for left/right/both eyes)
- PsychoPy installed (run from Builder or Coder)

---

## 🛠️ Hardware Requirements

- A **binocular rivalry VR headset** (with:
  - Separate display paths for left and right eye
  - Manual **focus adjustment knobs** ("moletta")
- Standard keyboard (for UP, DOWN, SPACE inputs)

---

## 🧪 Quick Start

1. Run the script using PsychoPy
2. Follow the phases:
   - Adjust focus with the molette when image is shown to one eye at a time
   - Use arrow keys to align images shown to both eyes
   - Press SPACE to confirm alignment
   - Passively view two BR trials of 30 seconds each

---

## 📌 Notes

- This setup assumes correct hardware calibration and user familiarity with the headset
- Ideal for calibration-based BR protocols or perceptual alignment studies

