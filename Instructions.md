## Training
### Training Buckets

There are four training buckets with 3 cases per training bucket. Each case was identified for having at least one lesion meeting the IOS ranking for the training bucket, but each case may have more targets identified. Within each training case exists a set of previously identified ARFI targets and identified cancer as well as labels for other benign findings like BPH, hemorrhage, Cysts, Calcifications, Prostatitis, Atrophy, and Fibrosis.

Volume Labels: (Walk through with Kathy from beginning again and review previous cases with questions, then do new cases and identify any new lesions. Still to do = IOS5, Multiple Lesions, IOS4 (Specifically Pt 78), IOS3. Then, after, label all lesions with IOS number or F-IOS number)
1. F Node: Matched Histology Lesions
2. Lesions: IOSX Identified mpUS Lesions, either positive or negative
3. GleasonScoreX: Unidentified Lesions
    **THESE NEED TO BE RELABELED AS IOSX LESIONS WHICH CAN REMOVE CANCER.mrk.json**

- IOS 3: 
  - Patient91 ?? Any other lesions???
    Notes: 
    1. Left Lateral Mid-Gland PZ (Region 10p)
       - Benign
       - ARFI IOS 3
    2. Left Medio-lateral Mid-Gland PZ (Region 9p)
       - Malignant: Gleason Score 7, Gleason Grade 2, Focal ECE Extent
       - MR Pi-Rads 5
       - SWEI IOS 4
    3. Benign Features include BPH

  - 2-09 Any other lesions ???
    - Notes:
    1. F-1-IOS3: Right Medio-lateral Mid-Gland PZ
       1. Reasonable IOS3, but Benign
    2. F-2-IOS3: Left Medial Apex TZ
       1. Reasonable IOS3, but Benign
    3. ?? Do we identify this ?? Right Medial Apex
       - Malignant: Gleason Score 6, Gleason Grade 1
    4. Benign Features include Blood Vessel, BPH, Calc

  - Patient79 Any other lesions???
    - Notes: 
    1. IOS3: Left Lateral Mid-Gland PZ (Region 10p + 11p)
       1. Gleason Score 7, Gleason Grade 2
    2. Benign Features Include Calc, BPH
    
- IOS 4:

  - Patient89 (IOS5 Bucket)
    - Notes:
    1. IOS5: 
       1. Same as Alternate IOS4. Chose here as can even see it in Bmode
       2. This is 3+4 Lesion. 
    2. IOS3: 
       1. Clear in coronal, not super visible in the other dimensions like axial, but it is smooth, hypointense
       2. This is also a 3+4 lesion. 
    3. IOS2:
       1. Moderate hypointense. In coronal plane, it looks like it may be closer to the transition zone, but in axial you can see it is clearly in PZ.
    4. IOS2: 
       1. Likely BPH. It is near the other BPH nodules, it looks encapsulated, especially in coronal view, but you can easily get tricked. I think because it looks encapsulated, more near central gland, are less suspicious, so maybe an IOS2. Also gets stiffer near the edge as if it is a nodule
    5. IOS2: 
       1. You can lightly see it in 2 views, but it is so diffuse. It falls apart as you scroll coronally. 
    6. IOS3: 
       1. In the TZ. So therefore less symmetric. Unclear boundary. Variable texture, high contrast. We do not normally look this far near the base. There is also a lot of BPH all around it. IOS3 because it is so dark and asymmetric.

  - Patient108 Most difficult case, not indicative of other cases. (IOS3 Bucket)
    - Notes: This case I want to walk through more for the purpose of workflow than lesion. There are lesions, but we adjusted something specific to this case that did not work and gave us poor image quality. 
    1. IOS3: 
       1. Just the part that is in the prostate, moderately hypointense, homogenous, moderate contrast, PZ
    2. IOS3: Right Medio-Lateral Mid-Gland PZ 
       1. Main thing going for it is hypointense. It is hard to judge based on the rest of the criteria, but in comparison to the contralateral side, it is dark, it is a different texture at least. Moderate contrast, heterogenous. 
       2. This is cancer - 3+4, Gleason Grade 2, established ECE Extent
    3. IOS2: 
       1. Heterogenous, moderately hypointense, variable boundary.

  - Patient78 (IOS5 Bucket)
    - Notes:
    1. IOS4:
       1. Highly suspicioius and in PZ
       2. BPH:
       1. If scroll coronally, can see the encapsulated 
    3. IOS4: 
       1. If you scroll coronally, you can see it is well defined boudary, hypointense, though heterogenous, it looks like a clearly defined lesion in PZ
       2. It is also asymmetric in coronal view. 
       3. We also debated whether this would be a 3 or 4. Either way, we would target it. 
    4. IOS3
       1. Hetergoenous, on the border of the PZ/TZ. Visible in 3 views, Moderately hypoechoic - medium contrast. Something about it extends into the PZ which is why it is a 3. Otherwise would thnk it is part of the TZ compressing out. 
       2. Same as Alternate Lesion IOS3. But would place it in a more suspicious spot
       3. Similar also as Alternate IOS2. Looks like edge of transition zone, maybe BPH. 
    5. IOS2
       1. In TZ, moderately echoic.
    6. Segmentation is unidentified 3+4 lesion. 
    
- IOS 5: 

  - Patient114 (IOS4 Bucket)
    - Notes: BPH contiguous with outer ring. There is a ring around the TZ because when BPH there 
      There is a lot of BPH and when you see those encapsulating darker regions, you know that is the TZ pushing out into the PZ creating that ring. 
    1. IOS2: Left Medial Mid-Apex PZ
       1. The IOS2 first is suspicious originally, but then you might thing it is part of the TZ pushing out, so becomes less weighted. Temp-1 = IOS2
       2. This would not be sampled, and Histology showed us is also not cancer
    2. IOS4: Left Medio-Lateral Base PZ
       1. Was Cancer, 3+4, Gleason Grade 2. 
       2. Dark in all views, Homogenous mainly in axial and coronal, Well defined boundary, PZ, maybe could argue it is a bit diffuse in boundary therefore a 3, but it is so hypoechoic. 
    3. IOS3: 
       1. is in the TZ, so if were in PZ, would be a 5, but this more likely a 4 as a result of the TZ. It's from our knowledge of where we have previously seen cancer would push this maybe to a 4. 
    4. IOS2: 
       1. IOS2 because we think it looks a little like BPH, but a darker BPH compared to the rest of the BPH in the gland, so hedge more towards a 2 as do not think it is cancer. It is also not that clear in the other views. Also in TZ, likely stromal BPH
       2. There is a lot of BPH in there, but it is round and circumscribed, it is encapsulated nodules. 
       
  - Patient115 (IOS3 Bucket)
    - Notes: A lot of calcs on patient right. Ignore all the saturated white stuff, that is really image artifact
    1. IOS3: 
       1. This is the same location as 4+4 alternate lesion, this is cancer. This is a positive. It is small, but mildly hypointense, medium contrast, in 2 views boundary is defined, largely homogenous.
       2. Alternate lesion is IOS2 and where cancer was truly identified. 
    2. IOS3. 
       1. We debated whether this would be a 3 or 4, it fits both well. Considering it is in the PZ, it has clear margins, though it is heterogenous. In all situations might put this at a 4, but it is hard to gauge asymmetry given the artifact, so we downgrade it to a 3. 
    3. IOS3: 
       1. Boundary is clear, but axial it is not well defined, heterogenous, only moderate hypointensity and moderate contrast. It is in PZ
    4. BPH:
       1. This might be an IOS2. If you look closely, you could see it is darker than the other side, especially the capsule itself, but this is clearly encapsulating something that is normal intensity, if not slightly darker, and in the central gland so likely BPH.
       2. Clearer in Axial view it gets bigger and more oval
    5. 3+3:
       1. Right apical lesion you can slightly see it, but difficult. Can see it coronally more, though symmetric in axial.

  - Patient109 (IOS4 Bucket)
    - Notes:
    1. IOS4: Right Lateral Mid-Gland PZ
       1. Right lesion as you begin scrolling coronally you can see the lesion early. 
       2. It is in PZ
       3. You could have placed the fiducial earlier (more posterior) where Temp-1 is. Here, it is not in all views, is in PZ, and does not have well defined boundary, heterogenous with variable texture, low contrast. 
       4. IOS4 marking in this instance was cancer. 3+4, so gleason grade 2, with established ECE Extent. This is a positive.
    2. IOS3: Right Medio-Lateral Apex PZ
       1. In PZ, small, but heterogenous. Has clear margins, but is so round, and we are less suspicious of such round lesions.
       2. There was no cancer here. This would be another miss, but as an IOS3 we still wanted to sample it. 
    3. IOS3: 
       1. It is more asymmetric, but are concerned that it is on the border of TZ. Not encapsulated, variable dark, asymmetric, hypointense, low medium contrast heterogeous with variable texture.
       2. This was initially thought as an IOS3 and we marked it as such. However, in hindsight, it looks to be part of the ring around the TZ (as the central gland pushes out, especially if there is BPH, then it creates a stiffer, dark boundary surrounding the central gland), especially when you align all three views with it and as calcs on the other side impair our ability to compare and the gland may simply have been cockeyed in the image. We would still put this at a 3, but the important thing here is to pay attention to symmetry and context of the gland. Anything in the TZ especially that might seem part of the border of the TZ would be less suspicious. 
    4. Urethra: 
       1. Urethra is central with many calcs (and when there are so many cannot really see past them)
    5. Calc: 
       1. Same thing. In axial and sagittal, it is hard often to see anterior of these
    6. 3+4:
       1. Unidentified Cancer. This was initially labeled as IOS3 when we had ARFI images, but non of us saw things when scrolling through so we would not relable this as an area of suspicion. This is unfortunately a miss.

  - Patient 62 (IOS5 Bucket)
    - Notes: 
    1. IOS4
    2. IOS5
       1. Matched Gleason 7, 3+4
    3. IOS3
       1. Matched Gleason 6, 3+3
    4. IOS3 
       1. Maybe or most likely BPH. Unsure
    5. IOS2
       1. You only see this coronally. Nothing too serious or interesting. 

### Training Instructions

1. Navigate to _ReaderStudy/Training/_ 
    >cd ReaderStudy\Training

2. Navigate through each training bucket folder. There are 3 cases within each folder meeting the IOS training criteria. Within each folder is a folder _slicer_ which contains the scene information for the case. 

3. Navigate through each case within each training bucket and open the slicer scenes to review the case data. 

4. In Slicer: 
   1. The ARFI and Bmode volumes are loaded. You can toggle between the two volumes as needed
   2. For the ARFI 2 cases (those with 2-#), the targets are labeled with fiducial markers. You can navigate to these by clicking on the fiducial in the 3D view
   3. For the RALP cases (those with Patient#), the segmentations are loaded. You can toggle the visibility of these segmentations under the _Data_ module
   
## Testing
### Instructions

1. Open the Reader Study Application on the desktop. This will open a command window which will update the platform and open the reader interface


2. Click on your name or add a new name if you are a new reader. If you accidentally remove a reader, hit the refresh button to bring the reader back. (Removing a reader will notify us that a reader was indicated for removal, and we will separately store that reader's case status before resetting the interface.)
   1. New Readers will add to the list.


3. Once you click on your name, a new interface will open populating the case information, your reader ID, and allowing inputs of any ARFI targets. The corresponding slicer scene will automatically open. An explanation of the interface is below:
    - _Case Number_: Folder name of the case you are reviewing
    - _Reader Name_: Your information
    - _Patient Review Notes_: Completed after you have reviewed the case and want to mark any additional information
    - **Load Case**: Loads any different / previous cases for editing or review
    - **Clear Case**: Resets the interface, deleting all present information
    - **Refresh**: Check all cores and entry boxes to determine if you are able to submit the case
    - **Submit Case**: Initially unavailable, but updated or refreshed to allow saving of case information
    - **Add ARFI Core**: Allows populating information for an additional target
      - New core entries start as red. Selecting the core will open a new window requiring entry of location and IOS information. Submitting this core will turn the core box green.
        - For each core, select the options describing the location of the core
        - Once all location descriptors or selected, Press the **Populate** button to populate the location notes entry
        - Select the IOS ranking for the target
        - Submit the Core
    - **Remove ARFI Core**: Deletes the most recent ARFI Core entry
    

4. Scan through the Slicer Scene to identify targets. Once you identify the targets you would like to biopsy, populate the interface.
   1. Adjust the window level / volume as necessary. Do so separately on ARFI and Bmode volumes. 
   2. Toggle between the ARFI and Bmode volumes as necessary
   3. Scroll through the volumes coronally. Identify any regions of suspicion. 
   4. Align all 3 views with regions of suspicion to confirm or deny suspicion. 
   5. Place a fiducial marker on the most suspicious lesions, if present. 


5. Before submitting the case, save the slicer scene. To do this, click the 'X' button on the slicer scene.
   1. **SAVE THE SLICER SCENE**. Ensure the **F.mrk.json** and **Scene.mrml** files are checked
   2. Change the folder where your Slicer scene will save to your folder's name. 
   3. Hit **Save**


6. Submit the case through the custom interface. This will open two file boxes. Select *Save* to both automatically opened file boxes. 


7. Once the Slicer scene is saved and the case is submitted, the **NEXT CASE** button will open and allow you to progress to a new case. 


## IOS Ranking System
 - IOS 1 / Very Low = Clinically significant cancer is highly unlikely to be present 
   - Hyperintense signal intensity 
   - Indistinct margin 


- IOS 2 / Low = Clinically significant cancer is unlikely to be present
  - Contralateral symmetry 
  - Hypointense, low or medium contrast 
 - Heterogeneous, variable texture
- Peripheral, Transition, or Central Zone 
  - in PZ, symmetric,
`in TZ, uniform dark rim

- IOS 3 / Intermediate = Clinically significant cancer is equivocal 
  - Contralaterally asymmetric or medial
  - Hypointense, low contrast mass 
  - Heterogeneous, variable texture  
  - Peripheral, Transition, or Central Zone 
  - in PZ, ill-defined boundary
  - in TZ, variable dark rim 


- IOS 4 / High = Clinically significant cancer is likely to be present 
  - Contralaterally asymmetric 
  - Hypointense, medium contrast focus / mass 
  - Homogenous or slightly variable texture
  - Peripheral or Transition Zone 
  - in PZ, variable boundary, any size
  - in TZ, variable boundary, > 1 cm


- IOS 5 / Very High = Clinically significant cancer is highly likely to be present 
  - Contralaterally asymmetric 
  - Hypointense, high contrast focus / mass 
  - Homogenous, uniform, smooth texture
  - Peripheral Zone 
  - Well defined boundary, any size
  - extraprostatic extension 


MRI Pi-Rads V2: https://www.acr.org/-/media/ACR/Files/RADS/Pi-RADS/PIRADS-V2.pdf

IOS 1-3: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4860099/

