# ECG_inversion_classification_api

## Detecting electrode inversion in an ECG

The ECG is a time series that records the heart's electrical activity and serves as a primary tool for diagnosing heart diseases. Capturing an ECG is a straightforward process involving the placement of 3 electrodes at the limb ends and 6 on the front chest. This setup generates 12 time series known as leads, with each representing the potential difference between electrode pairs.

The accurate positioning of electrodes is crucial for correctly interpreting the ECG results. Inverting electrodes can lead to misinterpretations, causing the leads to explore unexpected areas and resulting in errors in hypertrophia index measurements or ST segment analysis. Additionally, false abnormalities like fake Q waves or errors in the heart's axis can be generated.

Inversion errors are relatively common, occurring in around 5% of ECGs. Only experts like cardiologists can typically identify them. However, the majority of ECGs are not examined by experts, with only 30% being interpreted by nurses or general practitioners. To address this issue and improve diagnostic quality, it is essential to develop an algorithm capable of automatically detecting electrode inversion in ECGs.

This project aims to create a method for detecting electrode inversion in ECGs using a dataset containing ECGs from a cardiology center. Each ECG in the dataset will be labeled as correctly realized (0) or inverted (1).

## Inversions

Electrode inversions can involve more than just the inversion of two leads. For example, in the precordial leads (V1, ..., V6), the inversion can occur differently, where V1 becomes V6 and V2 becomes V5, and so on. Moreover, when certain pairs of electrodes are exchanged, it affects multiple leads such as I, II, III, AVF, AVR, and AVL differently. For instance, if the electrodes of the right and left arms are inverted, then I becomes -I, II and III are inverted, AVL and AVR are inverted, while AVF remains unchanged. More information about the relationships between different leads and how they are affected by inversion can be found here: <https://litfl.com/ecg-limb-lead-reversal-ecg-library/>
